"""
ORLANDO ALVES DE ALENCAR NETO
2021017630
HIPERMIDIA - TRAB 1
"""

import xml.etree.ElementTree as ET
from collections import defaultdict
import time
tree = ET.parse("D:\\Usuario\\Cliente\\Downloads\\verbetesWikipedia.xml")
root = tree.getroot()
cache = {}
arrayTablesPages = []

def count_consecutive_positions(list1, list2):
    count = 0
    set2 = set(list2)
    for num1 in list1:
        if ((num1 + 1 in set2) or (num1 - 1 in set2)):
            count += 1
    #Quando duas palavras aparecem consecutivamente, atribui-se peso 10
    return count * 10

def search_one_word(search):
    listResult = [] #[id, title, search_occurrences]
    indexPage = 0

    for table in arrayTablesPages:
        if (search in table):
            title = root[indexPage][1].text
            search_occurrences = table[search][0]
            id = table[search][2]
            listTemp = [id, title, search_occurrences]
            listResult.append(listTemp)
        indexPage += 1
    return listResult


def search_two_words(search):
    listResult = [] #[id, title, search_occurrences]
    indexPage = 0
    array_words = search.split(" ")

    for table in arrayTablesPages:
        if ((array_words[0] in table) and (array_words[1] in table)):
            title = root[indexPage][1].text
            #soma em search_occurrences as ocorrencias das duas palavras, individualmente
            search_occurrences = table[array_words[0]][0]
            search_occurrences += table[array_words[1]][0]

            #listas das posições das palavras buscadas na página
            index_list1 = table[array_words[0]][1]
            index_list2 = table[array_words[1]][1]

            #Denota numero de vezes em que as duas palavras aparecem consecutivamente
            # quase o mesmo que a própria variável "search"
            count_search = count_consecutive_positions(index_list1, index_list2)
            search_occurrences += count_search

            id = table[array_words[0]][2]
            listTemp = [id, title, search_occurrences]
            listResult.append(listTemp)
        elif((array_words[0] in table) and (array_words[1] not in table)):
            title = root[indexPage][1].text
            search_occurrences = table[array_words[0]][0]
            id = table[array_words[0]][2]
            listTemp = [id, title, search_occurrences]
            listResult.append(listTemp)
        elif ((array_words[0] not in table) and (array_words[1] in table)):
            title = root[indexPage][1].text
            search_occurrences = table[array_words[1]][0]
            id = table[array_words[1]][2]
            listTemp = [id, title, search_occurrences]
            listResult.append(listTemp)
        indexPage += 1
    return listResult


def get_table_page (page):
    #agora, a tabela é dada com o seguinte valor: [ocorrencias, posição das ocorrencias, id]
    tablePage = defaultdict(lambda: [0, [],0])
    for indexWord, wordInText in enumerate(page[2].text.split(" ")):
        if(len(wordInText) > 3):
            tablePage[wordInText.upper()][0] += 1
            tablePage[wordInText.upper()][1].append(indexWord)
            tablePage[wordInText.upper()][2] = page.find('id').text
    for wordInTitle in page[1].text.split(" "):
        if (len(wordInTitle) > 3):
            tablePage[wordInTitle.upper()][0] += 10
            tablePage[wordInTitle.upper()][2] = page.find('id').text
    return dict(tablePage)


def print_results(listResult):
    if (len(listResult) == 0):
        print("Sem resultados para a palavra inserida!\n")

    for item in listResult[0:20]:
        print(f"ID ({item[0]}) ::: {item[1]} ::: OCORRÊNCIAS ({item[2]})\n")


def add_tables_to_array(root):
    for page in root:
        table = get_table_page(page)
        arrayTablesPages.append(table)

time_ini = time.time()

add_tables_to_array(root)

time_final = time.time()
print(f"{(time_final-time_ini):.2f} segundos de processamento!")
while True:
    search = input("Faça uma busca: ").upper()

    if search in cache:
       print_results(cache[search])

    else:

        if(len(search.split(" ")) == 1):
            listResult = search_one_word(search)
        else:
            listResult = search_two_words(search)
        # [id, title, search_occurrences]
        listResult.sort(key=lambda list: list[2], reverse=True)
        cache[search] = listResult
        print_results(cache[search])

    question = input("Deseja fazer mais uma busca? [1] -> SIM ")

    if question != "1":
        break

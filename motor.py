import xml.etree.ElementTree as ET
from collections import defaultdict
tree = ET.parse("D:\\Usuario\\Cliente\\Downloads\\verbetesWikipedia.xml")
root = tree.getroot()
cache = {}
arrayTablesPages = []

def get_table_page (page):
    tablePage = defaultdict(int)

    for wordInText in page[2].text.split(" "):
        if(len(wordInText) > 3):
            tablePage[wordInText.upper()] += 1

    for wordInTitle in page[1].text.split(" "):
        if (len(wordInTitle) > 3):
            tablePage[wordInTitle.upper()] += 10

    return dict(tablePage)


def print_results(listResult):
    if (len(listResult) == 0):
        print("Sem resultados para a palavra inserida!\n")

    for item in listResult[0:20]:
        print(f"{item[0]} ::: {item[1]}\n")


def delete_little_words(text):
    stringTemp = ""
    for word in text.split(" "):
        if (len(word) > 3):
            stringTemp += word + " "
    return stringTemp


def add_tables_to_array(root):
    for page in root:
        table = get_table_page(page)
        arrayTablesPages.append(table)


add_tables_to_array(root)

while True:
    search = input("Faça uma busca: ").upper()

    if search in cache:
       print_results(cache[search])

    else:
        listResult = []
        indexPage = 0

        for table in arrayTablesPages:
            if (search in table):
                title = delete_little_words(root[indexPage][1].text)
                search_occurrences = table[search]
                listTemp = [search_occurrences, title]
                listResult.append(listTemp)
            indexPage += 1

        listResult.sort(key=lambda list: list[0], reverse=True)
        cache[search] = listResult
        print_results(cache[search])

    question = input("Deseja fazer mais uma busca? [1] -> SIM ")

    if question != "1":
        break

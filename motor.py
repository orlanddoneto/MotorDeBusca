import xml.etree.ElementTree as ET
tree = ET.parse("D:\\Usuario\\Cliente\\Downloads\\verbetesWikipedia.xml")
root = tree.getroot()

def count_occurrences (name, page):
    count = 0
    for wordInText in page[2].text.split(" "):
        if(name.upper() == wordInText.upper()):
            count +=1
    for wordInTitle in page[1].text.split(" "):
        if (name.upper() == wordInTitle.upper()):
            count += 10

    return count


def printResults(listResult):
    for item in listResult[0:20]:
        print(f"{item[0]} ::: {item[1]}")

def delete_little_words(text):
    stringTemp = ""
    for word in text.split(" "):
        if (len(word) > 3):
            stringTemp += word + " "

    return stringTemp;


cache = {}
while True:
    search = input("Faça uma busca: ").upper()

    if search in cache:
       printResults(cache[search])

    else:
        listResult = []
        for page in root:
            result = count_occurrences(search, page)
            if (result != 0):
                title = delete_little_words(page[1].text)
                listTemp = [result, title]
                listResult.append(listTemp)

        listResult.sort(key=lambda list: list[0], reverse=True)

        if (len(listResult) == 0):
            listResult.append("Sem resultados para a palavra inserida!")

        cache[search] = listResult

        printResults(cache[search])

    question = input("Deseja fazer mais uma busca? [1] -> SIM ")

    if question != "1":
        break;

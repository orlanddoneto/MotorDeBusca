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
    for item in listResult:
        print(item)

def delete_little_words(text):
    newList = []
    for word in text.split(" "):
        if (len(word) > 4):
            newList.append(word)
    stringTemp = ""
    for i in newList:
        stringTemp += i+" "

    return stringTemp;


cache = {}
while True:
    findWord = input("Faça uma busca: ").upper()

    if findWord in cache:
       printResults(cache[findWord])

    else:
        listResult = []
        countPageResults = 0
        for page in root:
            if (countPageResults == 20):
                break
            result = count_occurrences(findWord, page)
            if (result != 0):
                countPageResults+=1
                title = delete_little_words(page[1].text)
                listTemp = [result, title]
                listResult.append(listTemp)

        listResult.sort(key=lambda list: list[0], reverse=True)

        if (len(listResult) == 0):
            listResult.append("Sem resultados para a palavra inserida!")

        cache[findWord] = listResult

        printResults(cache[findWord])

    question = input("Deseja fazer mais uma busca? [1] -> SIM")

    if question != "1":
        break;

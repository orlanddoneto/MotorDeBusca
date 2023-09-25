import xml.etree.ElementTree as ET
tree = ET.parse("D:\\Usuario\\Cliente\\Downloads\\verbetesWikipedia.xml")
root = tree.getroot()

def function (nome, page):
    count = 0
    for wordInText in page[2].text.split(" "):
        if(nome.upper() == wordInText.upper()):
            count +=1
    for wordInTitle in page[1].text.split(" "):
        if (nome.upper() == wordInTitle.upper()):
            count += 10

    return count

listResult = []

for page in root:
    result = function("computer",page)
    if(result != 0):
        listTemp = [result,page[1].text]
        listResult.append(listTemp)

listResult.sort(key=lambda list: list[0], reverse=True)

for item in listResult:
    print(item)

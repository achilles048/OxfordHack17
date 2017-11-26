import xml.etree.ElementTree as ET
import requests
import database

def findrelevantpapers(disease):
    relevant_papers = []
    x = requests.get('https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=' + disease + '&retmax=50')
    with open('test.xml','wb' ) as file:
        file.write(x.content)
    tree = ET.parse('test.xml')
    root = tree.getroot()
    for line in root.iter('count'):
        no_relevant_papers = (line.text)
    for line in root.iter('document'):
        relevant_papers.append(line.attrib['url'])

    print(relevant_papers)
    return (relevant_papers)

def updatepapers(disease):
    original_papers = database.findDisease(disease)
    current_papers = findrelevantpapers(disease)
    for paper in current_papers:
        if not (paper in original_papers):
            database.addPaper(disease,paper)



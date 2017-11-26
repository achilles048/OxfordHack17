import json
import paperRank

global data
data = {}


def retrieveData():
    global data
    # open current store of diseases
    with open('dataStore.txt') as json_file:
        d = json.load(json_file)
    data = d


def saveData():
    global data
    with open('dataStore.txt', 'w') as outfile:
        json.dump(data, outfile)


def isInData(disease):
    global data
    return disease in data.keys()  # bool that records if in data


def findDisease(disease):
    """

    :param disease: the disease that is being searched for
    :return: papers (with their rankings) that are related
    """
    global data
    if isInData(disease):
        return data[disease]
    else:
        return []


def findPaper(disease, p):
    papers = findDisease(disease)
    if not(p in papers):
        return False
    return True

def addPaper(disease, p):
    global data
    data[disease].append([p, 5, 0])


def updatePaper(disease, paper, rank):
    global data
    index = data[disease].index(paper)
    updatedPaper = paperRank.update_rating(paper, rank)
    data[disease][index] = updatedPaper

'''
{[[title, rating, views]]}

diabetes
    paper 1 rating 5 views 
    paper 2 rating 7
    ...


'''


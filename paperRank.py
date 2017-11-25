

def add_paper(ratedPapers, paperName):
    """
    :param ratedPapers: list of already rated papers
    :param paperName: the name of the paper to be added with the default ratings
    :return:
    """
    ratedPapers[paperName] = []
    ratedPapers[paperName].append(5)  # add rating to paper
    ratedPapers[paperName].append(1)  # add number of ratings to paper



'''
def default_rank(paperNames):
    papers = []
    for p in paperNames:
        papers.append((p, 5))
    return papers
'''


def weigh_rating(rating, ratingData):
    """

    :param rating: the new rating to be considered for the paper
    :param ratingData: a tuple with the current overall rating and the umber of ratings
    :return:
    """
    ratingNum = ratingData[1]
    lastRating = ratingData[0]

    weightedRating = rating + (ratingNum / 100) - 0.01

    newRating = (lastRating * ratingNum + weightedRating) / (ratingNum + 1)

    # weigh the ratings by adding to their score
    # the amount added is reduced the more ratings there are to give new papers and advantage
    newRating = min(newRating, 10)

    return newRating, ratingNum + 1


def update_rating(paperData, rating):
    """
    :param paperData: list with paper name, rating, and number of ratings
    :param rating: the new rating given to the paper by the user
    :return: list with updated values for the overall rating and number of ratings
    """

    newRatingData = weigh_rating(rating, (paperData[1], paperData[2]))
    paperData[1] = newRatingData[0]
    paperData[2] = newRatingData[1]

    return paperData


def get_top_papers(papers):
    """

    :param papers: the whole list of rated papers that is to be used for recommendations
    :return: list of the top papers from the list
    """
    topPapers = []
    newPapers = []
    oldPapers = []

    # separate old and new papers using the number of ratings they have
    for p in papers:
        if p[2] < 5:
            newPapers.append(p)
        else:
            oldPapers.append(p)

    # if there are no old papers, pick up to 5 random new papers
    if len(oldPapers) < 1:
        i = 0
        while len(topPapers) < 5 and i < len(newPapers):
            topPapers.append(oldPapers[i])
            i = i + 1
        return topPapers
    # add up to 3 of the top rated old papers
    oldTops = 3
    topPapers = topPapers + getTops(oldPapers, oldTops)

    # fill tops until you have top 5 (or as close as you can get)
    k = 0
    while len(topPapers) < 5 and k < len(newPapers):
        topPapers.append(newPapers[k])
        k = k + 1

    return topPapers


def getTops(papers, podiums):
    if len(papers) <= podiums:
        return podiums
    tops = []
    while len(tops) < podiums:
        maxRating = 0
        for p in papers:
            if p[1] > maxRating:
                maxRating = p[1]
        for p in range(0, len(papers)):
            if papers[p][1] == maxRating:
                tops.append(papers[p])
                papers.pop(p)
                break
    return tops


testPapers = [["test1", 5, 3],
              ["test2", 4, 10],
              ["test3", 8, 20],
              ["test4", 5, 15],
              ["test5", 2, 1],
              ["test6", 1, 3],
              ["test7", 8, 5],
              ["test8", 4, 15], 
              ["test9", 1, 20],
              ["test10", 10, 10]]
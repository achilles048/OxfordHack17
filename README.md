# OxfordHack17

distionary={}

dis="diabetes"

def oldd(dis):
    tempap = relpapers(dis)
    finalpap= get_top_papers(tempap)
    #send to raiyyan once hes worked out Django Unchained
def newd(dis):
    tempap = relpapers(dis)
    distionary[dis] = [tempap]
    finalpap = get_top_papers(tempap)
    # send to raiyyan once hes worked out Django Unchained

if dis in distionary:
    oldd(dis)
else:
    newd(dis)


#collect ratings from the thing calling it newr
newrat=update_rating(distionary(dis), newr)

distionary[dis] = [newrat]

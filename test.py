from settings import *

def ppt():
    global MAPS
    for pr in MAPS:
        plt.scatter ([x for (x, _) in pr], [y for (_, y) in pr])
    plt.show ()

    pr = MAPS[0]
    plt.plot([pr[0][0], pr[JOIN_ID[0]][0]], [pr[0][1], pr[JOIN_ID[0]][1]])
    plt.plot([pr[JOIN_ID[0]+1][0], pr[JOIN_ID[1]][0]], [pr[JOIN_ID[0]+1][1], pr[JOIN_ID[1]][1]])
    plt.plot([pr[JOIN_ID[1] + 1][0], pr[JOIN_ID[2]][0]], [pr[JOIN_ID[1] + 1][1], pr[JOIN_ID[2]][1]])
    plt.plot([pr[JOIN_ID[2] + 1][0], pr[-1][0]], [pr[JOIN_ID[2] + 1][1], pr[-1][1]])
    plt.show()
    # print pr[0]
    
    
ppt()
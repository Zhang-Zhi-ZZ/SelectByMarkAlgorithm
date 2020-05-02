import numpy as np
from distanceBetweenCoords import*

def neibouringNodes(stations,nodes):
    stationRanking = {}
    nbStationsT = np.zeros((len(stations), len(nodes)))
    for i in stations:
        for j in nodes:
            pos1 = stations[i]
            pos2 = nodes[j]

            if isNeighbour(pos1, pos2):
                nbStationsT[i - 1, j - 1] = 1
    for i in range(len(stations)):
        stationRanking[i + 1] = int(np.sum(nbStationsT, axis=1)[i])
    # sorted_rank = sorted(stationRanking.items(), key=lambda x: -x[1])
    # print(nbStationsT)

    nbofS = {}

    for i in range(len(stations)):
        temp = []
        for j in range(len(nodes)):
            if nbStationsT[i][j] == 1:
                temp.append(j + 1)
        nbofS[i + 1] = temp

    #print(nbofS)
    return nbofS
    # print(sorted_rank)
    # print(stationRanking)


def neibouringStations(stations,nodes):
    nodesRanking = {}
    nbNodesT = np.zeros((len(nodes), len(stations)))
    for i in nodes:
        for j in stations:
            pos1 = nodes[i]
            pos2 = stations[j]

            if isNeighbour(pos1, pos2):
                nbNodesT[i - 1, j - 1] = 1
    for i in range(len(nodes)):
        nodesRanking[i + 1] = int(np.sum(nbNodesT, axis=1)[i])
    # sorted_rank = sorted(nodesRanking.items(), key=lambda x: -x[1])
    # print(nodesRanking)

    nbofN = {}

    for i in range(len(nodes)):
        temp = []
        for j in range(len(stations)):
            if nbNodesT[i][j] == 1:
                temp.append(j + 1)
        nbofN[i + 1] = temp
    return nbofN



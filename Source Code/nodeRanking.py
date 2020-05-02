import collections
from OD import *
from neighbouringSets import *
from nodeCoord import *


def tripspernode(fileName):
    dtype = [('node',int),('trips',int)]
    values = []
    matrix = od(fileName)
    depart = np.sum(matrix, axis=0)
    arrival = np.sum(matrix, axis=1)
    i = 0
    while i < 90:
        values.append((i+1,depart[i]+arrival[i]-matrix[i,i]))
        i+=1
    nodes = np.array(values,dtype = dtype)
    return nodes



def ranking(fileName):
    unranked = tripspernode(fileName)
    ranked = np.sort(unranked,order='trips')
    fromlargest = ranked[::-1]
    return fromlargest


def marksForNodes(rankedList):
    marks = rankedList
    highestMark = rankedList[0][1]
    for i in range(0,90):
        tmp = rankedList[i][1]/highestMark*100
        rankedList[i][1] = tmp
    #print(rankedList)
    #print(marks)
    return marks

def nodeRanking():

    fileList = ["9-15.txt",
                "15-19.txt", "19-24.txt",
                "24-6.txt"]

    ranks = np.sort(marksForNodes(ranking("6-9.txt")),order = 'node')
    for f in fileList:
        a = ranking(f)
        b= marksForNodes(a)
        unsorted = np.sort(b,order='node')
        for i in range(0,90):
            tmp = ranks[i][1]
            ranks[i][1] = tmp+unsorted[i][1]

    return ranks

global all_station_marks

def stationRanking():
    marksofNodes = nodeRanking()
    neighbouringnodesOfaStation = neibouringStations(allstations,allnodes)
    marks = {}
    for i in range(1,len(allstations)):
        mark = 0
        nodes = neighbouringnodesOfaStation[i]
        for j in nodes:
            mark += marksofNodes[j-1][1]
        marks[i] = mark
    sorted_marks = sorted(marks.items(), key=lambda kv: kv[1])
    sorted_dict = collections.OrderedDict(sorted_marks)

    #print(sorted_dict)

    keyList = []
    for i in sorted_dict.keys():
        keyList.append(i)

    group1 = keyList[0:18]
    group2 = keyList[18:37]
    group3 = keyList[37:]

    all_station_marks= {}
    station1, station2, station3 = {}, {}, {}
    for i in group1:
        station1[i] = sorted_dict[i]
    for i in group2:
        station2[i] = sorted_dict[i]
    for i in group3:
        station3[i] = sorted_dict[i]
    for i in keyList:
        all_station_marks[i] = sorted_dict[i]

    return keyList
    #return all_station_marks


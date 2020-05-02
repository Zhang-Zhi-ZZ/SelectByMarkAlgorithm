from nodeRanking import *
from distanceBetweenCoords import *
from nodeCoord import *
import random



def selectStaions(number):   # depend on the budget, company choose the number of stations
    station_marks = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 2: 48, 1: 57, 44: 74, 45: 74, 47: 74, 39: 176, 41: 284, 12: 289, 54: 311, 32: 338, 38: 346, 20: 414, 21: 418, 49: 426, 33: 500, 34: 500, 35: 500, 36: 500, 37: 514, 19: 550, 30: 564, 11: 595, 22: 646, 52: 710, 43: 751, 51: 772, 27: 773, 29: 773, 46: 807, 23: 872, 31: 872, 40: 882, 48: 886, 53: 886, 42: 900, 50: 900, 55: 900, 24: 935, 25: 994, 28: 994, 14: 1145, 18: 1169, 26: 1192, 15: 1343, 17: 1343, 13: 1352, 16: 1458}
    station_marks = stationRanking()
    sCoord = allstations
    # sCoord[k] returns coords for station k
    #stations = [station_marks.popitem()]
    start_point = len(allstations)-number-1
    selected_stations = station_marks[start_point:]
    stations = {}
    num = 1
    for i in selected_stations:
        stations[num] = allstations[i]
        num +=1

    '''    
    while len(stations) < n:
        is_valid = True
        newStation = station_marks.popitem()
        for s in stations:
            if isNeighbour(sCoord[newStation[0]],sCoord[s[0]]) <= 0.1:
                is_valid = False
        if is_valid:
            stations.append(newStation)
    '''
    #return stations
    f = open('selectedStations.txt', 'w')
    for s in selected_stations:
        tmp = sCoord[s]
        a = str(tmp)
        c = a.replace('[','')
        d = c.replace(']', '')
        #f.write(str(num1)+':')
        f.write(d)
        f.write('\n')
    f.close()


    f = open('parkingSpaces.txt','w')
    num = number
    third = num//3
    parkingspaces = {}
    for i in range(num):
        if i <= third:
            f.write(str(i)+':')
            f.write('3')
            f.write(',')
            parkingspaces[i] = 3
        elif third<i<=2*third:
            f.write(str(i) + ':')
            f.write('2')
            f.write(',')
            parkingspaces[i] = 2
        else:
            f.write(str(i) + ':')
            f.write('1')
            f.write(',')
            parkingspaces[i] = 1

    return neibouringNodes(stations, allnodes), neibouringStations(stations, allnodes), parkingspaces


def selectRandomStations(n):
    sCoord = allstations
    rangeofstations = [i for i in range(1,56)]
    stations = random.sample(rangeofstations,n)
    print(stations)
    # return stations
    f = open('RandomlySelectedStations.txt', 'w')
    num = 0
    for s in stations:
        tmp = sCoord[s]
        a = str(tmp)
        # c = a.replace('[','')
        # d = c.replace(']', '')
        #f.write(str(num) + ':')
        f.write(a)
        f.write('\n')
        num = num + 1

    f.close()

    f = open('parkingSpaces.txt', 'w')
    num = len(stations)
    third = num // 3
    parkingspaces = {}
    for i in range(num):
        if i <= third:
            f.write(str(i) + ':')
            f.write('3')
            f.write(',')
            parkingspaces[i] = 3
        elif third < i <= 2 * third:
            f.write(str(i) + ':')
            f.write('2')
            f.write(',')
            parkingspaces[i] = 2
        else:
            f.write(str(i) + ':')
            f.write('1')
            f.write(',')
            parkingspaces[i] = 1
    f.close()

    #return neibouringNodes(stations, allnodes), neibouringStations(stations, allnodes), parkingspaces

selectRandomStations(20)
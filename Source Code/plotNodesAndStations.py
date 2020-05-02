import numpy as np
from matplotlib import pyplot as plt
from OP import *
def plotAll(nodes,stations):
    f = open(nodes, 'rU')
    temp = []
    try:
        for line in f:
            lst = line.split(",")
            x = float(lst[0])
            y = float(lst[1])
            temp.append([x, y])
    finally:
        f.close()
    nodes = np.array(temp)

    f = open(stations, 'rU')
    temp2 = []
    numberOfStations = 0
    try:
        for line in f:
            lst = line.split(",")
            x = float(lst[0])
            y = float(lst[1])
            temp2.append([x, y])
            numberOfStations+=1
    finally:
        f.close()
    stations = np.array(temp2)

    x1,y1 = nodes.T
    plt.scatter(x1,y1,color='red',label = 'nodes')
    x2,y2 = stations.T
    plt.scatter(x2,y2,color = 'blue',label = 'stations')
    plt.legend(loc = 'upper right')
    title = 'Station Number: ' + str(numberOfStations + ": " + OP)
    plt.suptitle(title, fontsize=16)
    plt.show()

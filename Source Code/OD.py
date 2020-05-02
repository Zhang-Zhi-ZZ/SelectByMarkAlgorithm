# get ODt matrix from txt file
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


def od(fileName):
    OD = np.zeros((90, 90))
    f = open(fileName, 'rU')
    try:
        for line in f:
            lst = line.split(" ")
            tmp0 = list(filter(None, lst))
            o = int(tmp0[0])
            d = int(tmp0[1])
            n = int(tmp0[2])
            OD[o - 1, d - 1] = n
    finally:
        f.close()

    return OD
    # print(OD)

def outwardFlow(matrixODt):
    outward = np.sum(matrixODt, axis=0)
    return list(outward)


def inwardFlow(matrixODt):
    inward = np.sum(matrixODt, axis=1)
    return list(inward)


def odt():
    fileList = ["6-9.txt", "9-15.txt",
                "15-19.txt", "19-24.txt",
                "24-6.txt"]
    inward = []
    outward = []
    odt = []
    for f in fileList:
        '''
        print(f)

        print()

        print(od(f))
        '''
        temp = od(f)
        outward.append(outwardFlow(temp))
        inward.append(inwardFlow(temp))
        odt.append(temp)
    return inward, outward, odt
    # return od(f)


'''
97586.0
124637.0
164575.0
65257.0
423886.0
'''

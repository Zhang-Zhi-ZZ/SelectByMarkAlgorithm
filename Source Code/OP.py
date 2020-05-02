import pulp as plp
import numpy as np
from OD import*
import numpy
from selectStations import *
numpy.set_printoptions(threshold=sys.maxsize)
from plotNodesAndStations import *
from matplotlib import pyplot as plt
import timeit
import sys



def OP(numberOfStations):
    start = timeit.default_timer()
    global percent, comptime_in_mintues
    #define known variables

    #fnt+, inwardFlow
    #fnt-, outwardFlow
    #ODt, originDestination
    #n = 90, t = 5

    N = range(90)
    T = range(5)
    S = range(numberOfStations)
    inwardFlow = {}
    outwardFlow = {}
    originDestination = {}
    inward,outward,ODt = odt()

    for t in T:
        for n in N:
            tmp = inward[t][n]
            inwardFlow[n,t] = tmp
            tmp1 = outward[t][n]
            outwardFlow[n, t] = tmp1

    for t in T:
        tmp = ODt[t]
        tmp_row = 0
        for i in tmp:
            for j in N:
                originDestination[tmp_row,j,t] = i[j]
            tmp_row+=1


    neibouringNodes,neibouringStations,zs = selectStaions(numberOfStations)

    #vt
    vt = {0:6684,1:13496,2:8946,3:11120,4:13418}

    #zs: number of pairs of parking spaces to install at station s
    #zs = parkingspaces

    #Et   E(n,n,t)
    Et = plp.LpVariable.dicts(name="Et", indexs=(N,N,T),cat=plp.LpInteger,lowBound=0)




    #Ft+    F+(s,n,t)
    Ft_arriving = plp.LpVariable.dicts(name= "Ft_arriving", indexs = (S,N,T),cat=plp.LpInteger,lowBound=0)


    #Ft-    F-(s,n,t)
    Ft_departing = plp.LpVariable.dicts(name= "Ft_departing", indexs = (S,N,T),cat=plp.LpInteger,lowBound=0)


    #e

    e = [1]*90

    #create the problem

    prob = plp.LpProblem("OP", plp.LpMinimize)

    #constraints

    #OP1
    for t in T:
        for s in S:
            prob += plp.lpSum(Ft_arriving[s][n-1][t]+Ft_departing[s][n-1][t] for n in neibouringNodes[s+1]) <= \
                    vt[t]*zs[s]

    #OP2
    for t in T:
        for n1 in N:
            for n in N:
                prob += plp.lpSum(Ft_arriving[s-1][n][t] + plp.lpSum(Et[n1][n][t] for n1 in N) for s in neibouringStations[n+1]) == \
                        inwardFlow[n,t]


    #OP3
    for t in T:
        for n in N:
            for n1 in N:
                prob += plp.lpSum(Ft_departing[s-1][n][t] + plp.lpSum(Et[n][n1][t] for n1 in N) for s in neibouringStations[n+1]) == \
                        outwardFlow[n,t]


    #OP4
    for t in T:
        for s in S:
            prob += plp.lpSum(Ft_arriving[s][n-1][t] - Ft_departing[s][n-1][t] for n in neibouringNodes[s+1]) == 0


    #OP5

    '''
    
    for s in S:
        for n in N:
            for t in T:
                prob += Ft_arriving[s][n][t] <= originDestination[s,n,t]
                prob += Ft_departing[s][n][t] <= originDestination[n,s,t]

    '''

    for n1 in N:
        for n in N:
            for t in T:
                prob += Et[n1][n][t] <= originDestination[n1,n,t]

    #objective
    #OP
    #prob += plp.lpSum(Ft_arriving[s][n][t] for s in S for n in N for t in T)
    prob += plp.lpSum(Et[n][n1][t] for n in N for n1 in N for t in T)
    prob.solve()
    stop = timeit.default_timer()
    compute_time = int(stop-start)
    comptime_in_mintues = compute_time/60
    unsatisfiedTrips = 0
    for t in T:
        tmp1 = np.zeros((90, 90))
        for n in N:
            for n1 in N:
                tmp1[n,n1] = plp.value(Et[n][n1][t])
                unsatisfiedTrips+=tmp1[n,n1]


    totalTrips = sum(originDestination.values())
    satisfiedTrips = totalTrips - unsatisfiedTrips
    percent = satisfiedTrips/totalTrips*100
    #print('Total Trips:' + str(totalTrips))
    #print('Satisfied Trips:' + str(satisfiedTrips))
    #print('Unsatisfied Trips:' + str(unsatisfiedTrips))
    #print("Satisfied Trips/Total Trips = % 5.2f" % percent + '%' )

    plot('nodes.txt','selectedStations.txt')

def plot(nodes,stations):
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
    plt.title('Station Number: ' + str(numberOfStations)+'\nSatisfied Trips/Total Trips = % 5.2f' % percent + '%'
              +'\n Compute Time: %5.2f min' % comptime_in_mintues)
    plt.tight_layout()
    plt.show()


def main():
    OP(10)
    sys.exit()

main()

'''
Created on Oct 25, 2015

@author: Kevin
'''
import time

# Calculates the shortest distance between two attractions
# Inputs:
#    dist - list of distances between adjacent attractions
#    start - start point
#    stop - stop point
def calcDist(dists,start,stop):
    if start>stop:
        [start,stop] = [stop,start]
    oneWay = sum(dists[start:stop])
    otherWay = sum(dists[:start])+sum(dists[stop:])
    return(min([oneWay,otherWay]))

f2 = open('ans1.txt','w')
f = open('testcase.txt')
timeStart = time.time()
ignoreText = f.readline()
distances = [int(x) for x in f.readline().split()]
testN = int(f.readline())
for testI in range(testN):
    ignoreText = f.readline()
    path = [int(x) for x in f.readline().split()]
    pathLength = 0
    for ind in range(len(path)-1):
        pathLength += calcDist(distances,path[ind],path[ind+1])
    f2.write(str(pathLength) + '\n')
print(time.time()-timeStart)
'''
ignoreText = input()
distances = [int(x) for x in input().split()]
testN = int(input())
for testI in range(testN):
    ignoreText = input()
    path = [int(x) for x in input().split()]
    pathLength = 0
    for ind in range(len(path)-1):
        pathLength += calcDist(distances,path[ind],path[ind+1])
    print(pathLength)
'''
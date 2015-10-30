'''
Created on Oct 26, 2015

@author: Kevin
'''
import time

def shortestTime(waitTimes,plan,startTime,endHour):
    n = len(plan)
    visited = {tuple([0 for x in range(n)]):startTime}
    # Loop through each step
    for i in range(n):
        #print('index: ' + str(i+1) + ' out of ' + str(n))
        visiting = {}
        # Loop through visited sets of attractions
        for curKey in visited.keys():  
            curTime = visited[curKey]
            curHour = int(curTime/60)
            # Only continue if park hasn't closed
            if curHour<endHour:
                # Loop through unvisited attractions
                for nextI in range(n):
                    if curKey[nextI]==0: 
                        nextSite = plan[nextI]
                        
                        nextList = list(curKey)
                        nextList[nextI] = 1
                        nextKey = tuple(nextList)   # finds the next key to store
                        
                        minute = curTime%60
                        nextTime = curTime + waitTimes[nextSite][curHour]
                        maxHourCheck = min([curHour + int((minute+nextTime)/60),endHour-1]) # Latest hour to check if waiting is better
                        
                        for waitHour in range(curHour + 1,maxHourCheck+1):  # Loop through possible wait times to see if next hour times are fast
                            nextTimeWait = waitHour*60 + waitTimes[nextSite][waitHour]
                            if nextTimeWait < nextTime:
                                nextTime = nextTimeWait 
                        try:
                            if nextTime < visiting[nextKey]:
                                visiting[nextKey] = nextTime
                        except KeyError:
                            visiting[nextKey] = nextTime
        # If nothing recorded, then all times are past
        if len(visiting) == 0:
            return -1
        # Update set of attractions visited
        visited = visiting
    finalTime = visited[tuple([1 for x in range(n)])]
    if finalTime/60 <= endHour:
        return finalTime - startTime
    else:
        return -1
        
f = open('PlannerTestCase.txt')

beginTime = time.time()
[R,H] = [int(x) for x in f.readline().split()]
waitTimes = []
for i in range(R):
    waitTimes.append([int(x) for x in f.readline().split()])
Q = int(f.readline())
for query in range(Q):
    print('query: ' + str(query+1) + ' out of ' + str(Q))
    startTime = int(f.readline())
    planLen = int(f.readline())
    plan = [int(x) for x in f.readline().split()]
    if planLen == 0:
        print(0)
    elif startTime > 60*H:
        print('IMPOSSIBLE')
    else:
        answer = shortestTime(waitTimes,plan,startTime,H)
        if answer < 0:
            print('IMPOSSIBLE')
        else:
            print(answer)
        
print(time.time()-beginTime)
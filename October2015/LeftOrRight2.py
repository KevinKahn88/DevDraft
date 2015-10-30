'''
Created on Oct 25, 2015

@author: Kevin
'''
import time

def allTimes(adjTimes):
    circleTime = sum(adjTimes)
    n = len(adjTimes)
    walkTimes = [[0 for x in range(n)] for y in range(n)]
    for col in range(1,n):
        for row in range(col):
            # 'Forward' path time stored where col > row
            # Calculated by adding to previous step
            walkTimes[row][col] = walkTimes[row][col-1] + adjTimes[col-1]
            
            # Shortest path time checked and stored where row > col
            otherWay = circleTime - walkTimes[row][col]
            if walkTimes[row][col] > otherWay:
                walkTimes[col][row] = otherWay
            else:
                walkTimes[col][row] = walkTimes[row][col]
                
    # Copy shortest time to rest of matrix
    for col in range(1,n):
        for row in range(col):
            walkTimes[row][col] = walkTimes[col][row]
    return walkTimes 

f = open('testcase.txt')
f2 = open('ans2.txt','w')
startTime = time.time()
ignoreText = f.readline()
adjTimes = [int(x) for x in f.readline().split()]
walkTimes = allTimes(adjTimes)
testN = int(f.readline())
for testI in range(testN):
    ignoreText = f.readline()
    pathTime = 0
    path = [int(x) for x in f.readline().split()]
    
    # Sum each step's time for pathTime
    for step in range(len(path)-1):
        pathTime += walkTimes[path[step]][path[step+1]]
    f2.write(str(pathTime)+'\n')
print(time.time()-startTime)
f2.close()
f.close()
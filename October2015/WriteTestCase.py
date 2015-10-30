'''
Created on Oct 25, 2015

@author: Kevin
'''
import numpy.random as random

waitTimes = [3,6,9,12,15,20,25,30,45,60]
f = open('PlannerTestCaseShort.txt','w')
f.write('999 5\n')

for i in range(999):
    for j in range(5):
        f.write(str(waitTimes[int(random.random()*10)]) + ' ')
    f.write('\n')
    
f.write('99\n')
for i in range(99):
    f.write(str(int(random.random()*5*60)) + '\n')
    d = int(random.random()*21)
    f.write(str(d) + '\n')
    plan = random.permutation(999)
    f.write(' '.join([str(plan[x]) for x in range(d)]) + '\n')

f.close()
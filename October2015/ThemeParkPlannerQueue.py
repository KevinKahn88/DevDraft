'''
Created on Oct 27, 2015

@author: Kevin
'''

# Calculates the order of the roots
def calcOrder(roots):
    return [len(rootNode.nextNodes) for rootNode in roots]

# Returns index of first minvalue
def minIndex(nums):
    minValue = nums[0]
    ind = 0
    for i in range(len(nums)):
        if nums[i]<minValue:
            minValue = nums[i]
            ind = i
    return ind


class ParkPlanner(object):
    '''
    Models the Park Attraction Wait Times Across the Day
    
    Calculates shortest time to see all attractions
    '''

    def __init__(self, waitTimes,endHour):
        '''
        Constructor
        '''
        self.waitTimes = waitTimes
        self.endHour = endHour
        
    def bestTime(self,startTime,plan):
        finalState = [1 for x in range(len(plan))]
        startNode = Node(startTime,[0 for x in range(len(plan))])
        planPQ = PriorityQueue([startNode])
        while
        
        
class Node(object):
    '''
    Node to be used in priority queue
    '''
    
    def __init__(self, priority, data, parent = None):
        self.priority = priority
        self.data = data
        self.parent = None
        self.nextNodes = []
        self.mark = False
        
    
class PriorityQueue(object):
    '''
    Priority queue to track optimal order for Dijkstra algorithms_available
    '''
    
    def __init__(self,roots=None):
        self.roots = roots
        self.order = calcOrder(roots)
        self.dataDict = {}
        for node in roots:
            self.dataDict[node.data] = node
        
    def findMin(self):
        try:
            return self.roots[0]
        except IndexError:
            print('PQ Empty')
            return -1
        
    def insert(self,newNode):
        self.dataDict[newNode.data]=newNode
        if newNode.priority < self.roots[0].priority:
            self.roots = [newNode] + self.roots
            self.order = [len(newNode.nextNodes)] + self.order
        else:
            self.roots.append([newNode])
            self.order.append(len(newNode.nextNodes))
        self.parent = None
    
    def delete(self,oldNode):
        self.roots = [oldNode] + 
    
    def extractMin(self):
        #Extract info from min priority node
        minNodeInfo = [self.roots[0].data, self.roots[0].priority]
        del self.dataDict[self.roots[0].data]
        
        #Delete min node and move all children to root
        for node in self.roots[0].nextNodes:
            node.parent = None
        self.roots = self.roots[1:] + self.roots[0].nextNodes
        self.order = self.order[1:] + calcOrder(self.roots[0].nextNodes)
        
        #Update the heap
        self.updateQueue()
        
        #Move min node to 0 index and update order
        ind = minIndex([root.priority for root in self.roots])
        [self.roots[0],self.roots[ind]] = [self.roots[ind],self.roots[0]]
        [self.order[0],self.order[ind]] = [self.order[ind],self.order[0]]
        
        return minNodeInfo
            
    def decreaseKey(self,changeNode,newPriority):
        changeNode.priority = newPriority
        
        if changeNode.priority < changeNode.parent.priority:
            cutFlag = True
            childNode = changeNode
            parentNode = childNode.parent
            
            while cutFlag:
                if parentNode is None:
                    cutFlag = False
                else:
                    self.insert(childNode)
                    parentNode.nextNodes.remove(childNode)
                    if parentNode.parent is None:
                        ind = self.order.index(parentNode)
                        self.order[ind] -= 1
                    if parentNode.mark is False:
                        parentNode.mark = True
                        cutFlag = False
                    childNode = parentNode
                    parentNode = parentNode.parent

    def findMinOrderDup(self):
        orderHash = {}
        order = self.order
        for i in range(len(self.order)):
            try:
                orderHash[order[i]].append(i)
            except KeyError:
                orderHash[order[i]] = [i]
        keyList = list(orderHash.keys())
        keyList.sort()
        for key in keyList: 
            if len(orderHash[key]) > 1:
                return orderHash[key]
        return []
    
    def updateQueue(self):
        minOrderDup = self.findMinOrderDup()
        # Loop while there are duplicate orders
        while len(minOrderDup) > 0:
            minOrderDup.reverse()
            ind = 0
            print(minOrderDup)
            # Loop through duplicated orders from end to beginning
            while ind + 1 < len(minOrderDup):
                rootA = minOrderDup[ind+1]
                rootB = minOrderDup[ind]
                
                print(str(rootA) + ' ' + str(rootB))
                
                # Ensure rootA priority is lower or equal
                if self.roots[rootA].priority > self.roots[rootB].priority:
                    [self.roots[rootA],self.roots[rootB]] = [self.roots[rootB],self.roots[rootA]] 
                      
                # Move nodeB to children of node A
                self.roots[rootA].nextNodes.append(self.roots[rootB])
                self.roots[rootB].parent = self.roots[rootA]
                
                # Delete original node B
                del self.roots[rootB]
                
                # Update orders
                self.order[rootA] += 1
                del self.order[rootB]
                
                ind += 2
            
            # Find new duplicated orders
            minOrderDup = self.findMinOrderDup()
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
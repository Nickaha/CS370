import math
import os
import random
import re
import sys

class Node:
    def __init__(self,dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
        self.parent = None

class Slinked:
    def __init__(self):
        self.headval = None
        self.size = 0
    
    def find(self,val):
        checkval=self.headval
        while checkval is not None: 
            if(checkval.dataVal == val):
                return True
        return False

    def insert(self,data):
        checkval = self.headval
        if(checkval is None):
            self.headval = Node(data)  
        while checkval is not None:
            if(data<checkval.dataVal):
                newNode = Node(data)
                newNode.nextVal=checkval
                newNode.parent = checkval.parent
                checkval.parent.nextVal=newNode
                checkval.parent=newNode
                size+=1

    




# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

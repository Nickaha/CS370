#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self,data=1,level=1):
        self.data=data
        self.left=None
        self.right=None
        self.level=level
    def insertLeft(self,data):
        self.left=Node(data,self.level+1)
    def insertRight(self,data):
        self.right=Node(data,self.level+1)

def swap(node):
    temp = node.left
    node.left=node.right
    node.right=temp
def insert(node,nodes):
    left = nodes[0]
    right = nodes[1]
    if(left!=-1):
        node.insertLeft(left)
    if(right!=-1):
        node.insertRight(right)
    return node
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    a=Node()
    a=insert(a,indexes[0])
    for i in range(1,len(indexes),2):
        a=a.left
        b=a.right
        a=insert(a,indexes[i])
        b=insert(b,indexes[i+1])
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
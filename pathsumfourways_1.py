# Hannah Radom, Alexander Lu, Ryan Qin
# I pledge my honor that I have abided by the Stevens Honor System.
import math
import sys

#takes in the input matrix, height of matrix, and width of matrix
def minPath(input, height, width):
    #candidate dictionary matches cost to coords
    candidates = dict()
    for i in range(height):
        for j in range(width):
            #set all path lens in array to inf
            candidates[(i,j)] = math.inf
    
    #set the first thing in cost table to the top left item
    candidates[(0,0)] = input[0][0]
    visited = set()

    #current position in table
    cur = (0,0)
    unvisited = set()
    path = []
    
    
    while(True):

        #check each direction, as long as you are inside the bounds and you haven't visited the item before
        #set the cost to be the minimum between the current cost and potential cost 
        
        #check bottom
        if(cur[0] < height-1):
            if((cur[0]+1,cur[1]) not in visited):
                unvisited.add((cur[0]+1,cur[1]))
                candidates[(cur[0]+1,cur[1])] = min(candidates[(cur[0]+1,cur[1])], input[cur[0]+1][cur[1]] + candidates[(cur[0],cur[1])])
        #check top
        if(cur[0] > 0):
            if((cur[0]-1,cur[1]) not in visited):
                unvisited.add((cur[0]-1,cur[1]))
                candidates[(cur[0]-1,cur[1])] = min(candidates[(cur[0]-1,cur[1])], input[cur[0]-1][cur[1]] + candidates[(cur[0],cur[1])])
        #check right
        if(cur[1] < width-1):
            if((cur[0],cur[1]+1) not in visited):
                unvisited.add((cur[0],cur[1]+1))
                candidates[(cur[0],cur[1]+1)] = min(candidates[(cur[0],cur[1]+1)], input[cur[0]][cur[1]+1] + candidates[(cur[0],cur[1])])
        #check left
        if(cur[1] > 0):
            if((cur[0],cur[1]-1) not in visited):
                unvisited.add((cur[0],cur[1]-1))
                candidates[(cur[0],cur[1]-1)] = min(candidates[(cur[0],cur[1]-1)], input[cur[0]][cur[1]-1] + candidates[(cur[0],cur[1])])

        #after checking the neighbors, add current position to visited
        visited.add(cur)

        #reached the end state in the bottom right
        if(cur[0] == height-1 and cur[1] == width-1 and (cur[0],cur[1]) in visited):
            #call backtracking algo to get the path
            path = backtrack(candidates, height, width, input)
            sum = 0
            for num in path:
                sum+=num
            #double check that the sum of the path matches the bottom right of the cost table
            assert sum == candidates[(height-1,width-1)]
            return candidates[(height-1,width-1)], path
        else:
            #check next place to go using the unvisited set that contains all the currently reachable neighbors
            #go to tentative lowest cost
            tempCost = math.inf
            for node in unvisited:
                if(candidates[node] < tempCost and node not in visited):
                    cur = node
                    tempCost = candidates[node]
            unvisited.remove(cur)

#takes in the completed cost table, height, width, and original matrix
def backtrack(costTable, height, width, input):
    path = []
    row = height - 1
    col = width - 1
    #set current position to the bottom right
    cur = (row,col)
    while(cur[0] > 0 or cur[1] > 0):
        path.append(input[cur[0]][cur[1]])
        botVal = None
        topVal = None
        rightVal = None
        leftVal = None
        #set each of the neighbor values based on the cost table
        if(cur[0] < row):
            botVal = costTable[(cur[0]+1,cur[1])]
        if(cur[0] > 0):
            topVal = costTable[(cur[0]-1,cur[1])]
        if(cur[1] < col):
            rightVal = costTable[(cur[0],cur[1]+1)]
        if(cur[1] > 0):
            leftVal = costTable[(cur[0],cur[1]-1)]
        l = [botVal, topVal, rightVal, leftVal]
        #take the minimum of all the neighbor cost values
        minVal = min(i for i in l if i is not None)
        index = l.index(minVal)

        #based on the index in the list, you know which direction to go next
        if(index == 0):
            newCur = (cur[0]+1, cur[1])
            cur = newCur
            
        if(index == 1):
            newCur = (cur[0]-1, cur[1])
            cur = newCur
            
        if(index == 2):
            newCur = (cur[0], cur[1]+1)
            cur = newCur
            
        if(index == 3):
            newCur = (cur[0], cur[1]-1)
            cur = newCur
    #add the top left value as the last thing in the path
    path.append(input[0][0])
    return path

def main():
    # Check that there are the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3.7 pathsumfourways <input file>")
        return
    # Try to open the text file
    try:
        f = open(sys.argv[1], 'r')
    except:
        print("Error: File '%s' not found." %sys.argv[1])
        return
    # Create a 2D array from the input file
    matrix = [list(map(int, line.strip().split(","))) for line in f]
    f.close()
    # Get the answer, which returns a tuple of (minSum, path)
    ans = minPath(matrix, len(matrix), len(matrix[0]))
    minSum = ans[0]
    # Need to reverse the path to start from the top left and end at the bottom right
    path = "[" + ', '.join(map(str,reversed(ans[1]))) + "]"
    print("Min sum: " + str(minSum))
    print("Values:  " + path)
main()
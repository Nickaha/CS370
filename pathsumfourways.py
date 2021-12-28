import math
def PathFourWays():
    with open('matrix.txt','r') as infile:
        data = infile.readlines()
    values = []
    # read txt file and convert the matrix to a 2d table
    for line in data:
        values.append(list(map(int,line.strip().split(','))))
    costtable = []
    m = len(values)
    n = len(values[0])
    #create dynamic table
    for i in range(m):
        costtable.append([])
        for j in range(n):
            costtable[i].append(math.inf)
    costtable[0][0]=values[0][0]
    current = (0,0)
    visited = set()
    unvisited = set()
    #dp
    while(True):
        #check bottom
        if(current[0]<m-1):
            if((current[0]+1,current[1])not in visited):
                unvisited.add((current[0]+1,current[1]))
                costtable[current[0]+1][current[1]] = min(costtable[current[0]+1][current[1]], values[current[0]+1][current[1]] + costtable[current[0]][current[1]])
        #check top
        if(current[0]>0):
            if((current[0]-1,current[1]) not in visited):
                unvisited.add((current[0]-1,current[1]))
                costtable[current[0]-1][current[1]] = min(costtable[current[0]-1][current[1]], values[current[0]-1][current[1]] + costtable[current[0]][current[1]])
        #check right
        if(current[1] < n-1):
            if((current[0],current[1]+1) not in visited):
                unvisited.add((current[0],current[1]+1))
                costtable[current[0]][current[1]+1] = min(costtable[current[0]][current[1]+1], values[current[0]][current[1]+1] + costtable[current[0]][current[1]])
        #check left
        if(current[1] > 0):
            if((current[0],current[1]-1) not in visited):
                unvisited.add((current[0],current[1]-1))
                costtable[current[0]][current[1]-1] = min(costtable[current[0]][current[1]-1], values[current[0]][current[1]-1] + costtable[current[0]][current[1]])

        
        visited.add(current)
        #check if the table is completed
        if(current[0] == m-1 and current[1]==n-1):
            print("The min value is: ",costtable[m-1][n-1])
            print("The path is: ", getPath(costtable,values))
            return
        else:
            temp=math.inf
            for num in unvisited:
                if(costtable[num[0]][num[1]]<temp and num not in visited):
                    current=num
                    temp=costtable[num[0]][num[1]]
            unvisited.remove(current)
def getPath(costtable,values):
    m = len(values)
    n = len(values[0])
    row = m-1
    col = n-1
    result=[]
    #by finding the min value of the adjacent index and move to the min index
    while(row>0 or col>0):
        result.append(values[row][col])
        bot = math.inf
        top = math.inf
        left = math.inf
        right = math.inf
        if(row<m-1):
            bot = costtable[row+1][col]
        if(row>0):
            top = costtable[row-1][col]
        if(col<n-1):
            right=costtable[row][col+1]
        if(col>0):
            left=costtable[row][col-1]
        adj = [top,bot,left,right]
        nextc = adj.index(min(adj))
        if(nextc == 0):
            row-=1
        if(nextc==1):
            row+=1
        if(nextc==2):
            col-=1
        if(nextc==3):
            col+=1
    result.append(values[row][col])
    return result[::-1]


PathFourWays()
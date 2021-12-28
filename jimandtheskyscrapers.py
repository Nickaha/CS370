############################################
# Names: Dave Taveras, Marjan Chowdhury, Nick Guo
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Assignment: Project: Hackerrank Jim and The Skyscrapers
# Date: May 4th, 2021
# Course: CS370: Creative Problem Solving
############################################
import os
import sys

# Complete the solve function below.
def solve(arr):
    #use a list to imitate a stack to store list pairs of the heights and number of routes for that height
    stack = []
    count = 0
   
    for x in range(len(arr)):
    	#iterate through the original list
        while len(stack) != 0:
            #while stack is not empty
            if arr[x] > stack[-1][0]:
                #if the current number is higher than most recent element in stack pop since a valid route cannot be made
                stack.pop();
            else:
                #if current number is less than most recent element in stack break out of loop since a valid route can be made
                break;
        if(len(stack) != 0):
            #if the stack is not empty
            if(arr[x] == stack[-1][0]):
                #if the current height matches the height of the most recent element in the stack a valid route exists
                #increment the count by the value of most recent element in the stack * 2 since backwards also counts as a valid route
                count = count + (stack[-1][1]*2)
                #increment the number of routes for that height by 1
                stack[-1][1] = stack[-1][1] + 1
            else:
                #if current does not equal most recent element in the stack then add that element to the stack with a value of 1 
                stack.append([arr[x], 1])
        else:
            #if the stack is empty then add current element to stack with value of 1
            stack.append([arr[x], 1])
    #return count
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    ''' 
    # For large input (optional - was made to read large input easier from a .txt file)
    arr= []
    for _ in range(arr_count):
        a_item = int(input())
        arr.append(a_item)
    '''

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

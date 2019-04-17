#! /usr/bin/python

import sys

#Objective: Find the shortest path between -3 and -2

#Note: This is python3 

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,3,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1],
    [1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
    [1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1],
    [1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

class Block:
    def __init__(self, value):
        self.value=value
        self.visited=False

region=[]  #an array of blocks

for i in range(len(maze)):
    reglist=[]
    for j in range(len(maze)):
        reglist.append(Block(maze[i][j]))
    region.append(reglist)



def printRegion():
    for i in range(len(region)):
        for j in range(len(region)):
            if(region[i][j].value==1):
                print("x", end=" ", flush=True)
            elif (region[i][j].value == 0):
                print(" ", end=" ", flush=True)
            elif(region[i][j].value == 2 or region[i][j].value == 3):
                print("O", end=" ", flush=True)
            else:
                print(region[i][j].value,end=" ", flush=True)     
        print("...")

def drawPath(endValue, x,y):

    if(x<0 or x>19 or y<0 or y>19): return False

    if(region[x][y].visited or region[x][y].value==1): return False

    if(region[x][y].value == endValue): return True

    region[x][y].visited = True
    
    region[x][y].value = '.'

    if drawPath(endValue,x+1,y): return True

    if drawPath(endValue,x-1,y): return True

    if drawPath(endValue,x,y+1): return True

    if drawPath(endValue,x,y-1): return True

    region[x][y].value=0
    region[x][y].visited = False
    return False



printRegion()
drawPath(3,1,1)
print("")
printRegion()







 
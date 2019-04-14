#! /usr/bin/python

import sys

#Objective: Find the shortest path between -3 and -2

region = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-3,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
    [-1,0,0,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,0,-1,-1,0,-1,0,0,0,-1,0,0,0,0,0,-1,0,0,0,-1],
    [-1,0,-1,0,0,-1,0,0,0,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,0,-1,0,-1,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,-1],
    [-1,0,-1,-2,-1,0,0,0,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,0,-1,-1,-1,0,0,0,-1,0,0,-1,0,0,0,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,-1,-1,-1,-1,0,0,0,-1,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,-1,-1,0,0,-1,-1,0,0,0,-1],
    [-1,0,-1,-1,-1,-1,-1,0,0,0,-1,-1,0,0,-1,0,0,-1,0,-1],
    [-1,0,-1,0,0,0,-1,0,0,0,-1,-1,0,0,0,0,0,0,0,-1],
    [-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,0,0,-1,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1],
    [-1,0,-1,-1,0,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,-1],
    [-1,0,-1,-1,0,-1,-1,0,0,0,0,-1,-1,-1,-1,0,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ]

path=[]


def printRegion(region):
    for i in range(len(region)):
        for j in range(len(region)):
            if(region[i][j]==-1):
                print("x", end=" ", flush=True)
            elif (region[i][j]== 0):
                print(" ", end=" ", flush=True)
            elif(region[i][j]== -3 or region[i][j] == -2):
                print("O", end=" ", flush=True)
            else:
                print(region[i][j],end=" ", flush=True)     
        print("...")

def printPath(path):
    for element in path:
        print('path:', element)


# Mark the posible paths between -3 and -2 and mark them

def markPath(start,finish,x,y,number):

    #check if index is valid
    if (not posibleCoord(x,y)): return 
    
    #exit condition: it reached the object.
    if(region[x][y] == finish): return 

    #trigger recursivity
    if(region[x][y]==0 or region[x][y]== start): 

        #change number of the current position
        if(region[x][y]==0):
            region[x][y]=number
            number+=1     

        markPath(start, finish,x+1,y,number)
        markPath(start, finish,x-1,y,number)
        markPath(start, finish,x,y+1,number)
        markPath(start, finish,x,y-1,number)


#check if coordinate is posible
def posibleCoord(x,y):
    if(x < 0 or  x>19 or y>19 or y<0): return False
    return True

#return coordinate of the min value
def selectMin(x,y):

    minCoord={'x':0,'y':0,'val':sys.maxsize}
    coords = [{'x':x+1,'y':y}, {'x':x-1,'y':y},{'x':x,'y':y+1},{'x':x,'y':y-1}]

    for coord in coords:
        
        if(posibleCoord(coord['x'],coord['y']) and region[coord['x']][coord['y']]<minCoord['val'] and region[coord['x']][coord['y']]!=-1): 
            minCoord['x']= coord['x']
            minCoord['y'] = coord['y']
            minCoord['val'] = region[coord['x']][coord['y']]
            print('minCoord',minCoord)

    return minCoord
    
#store min coordinate in path list
def storeMinPath(start,endx,endy):
    
    if(region[endx][endy]==start): return
    
    minCoord=selectMin(endx,endy)

    path.append(minCoord)

    print('minCoord Final',minCoord)

    #storeMinPath(start,minCoord['x'],minCoord['y'])





    

#Function calls
printRegion(region)
markPath(-3,-2,1,1,1)
storeMinPath(-3,6,3)
printRegion(region)
printPath(path)


 
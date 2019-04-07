#! /usr/bin/python

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
    [-1,0,-1,-1,0,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,1],
    [-1,0,-1,-1,0,-1,-1,0,0,0,0,-1,-1,-1,-1,0,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ]

#print region


def printRegion(region):
    for i in range(len(region)):
        for j in range(len(region)):
            if(region[i][j]==-1):
                print("x", end="", flush=True)
            elif (region[i][j]== 0):
                print(" ", end="", flush=True)
            elif(region[i][j]== -3 or region[i][j] == -2):
                print("O", end="", flush=True)
            else:
                print(region[i][j], flush=True)     
        print("...")


#find shortest path between -3 and -2

def markPath(start,finish,x,y,number):

    #check if index is valid
    if (x < 0 or  x>19 or y>19 or y<0): return 
    
    #exit condition: it reached the object.
    
    if(region[x][y] == finish): return 

    #Mark boxes near
   
    if(region[x][y] != start):
        region[x][y]=number
    
    number+=1
    
    #markPath(start, finish,x+1,y,number)
    #markPath(start, finish,x-1,y,number)
    #markPath(start, finish,x,y+1,number)
    #markPath(start, finish,x,y-1,number)


#Function calls
printRegion(region)
markPath(-3,-2,1,1,1)
printRegion(region)


 
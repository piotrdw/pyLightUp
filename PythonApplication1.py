from enum import Enum
import random
from copy import deepcopy

class Tile(Enum):
    Block = "b-"
    Block0 = "b0"
    Block1 = "b1"
    Block2 = "b2"
    Block3 = "b3"
    Block4 = "b4"
    EmptyUnlit = "e-"
    EmptyLit = "e+"
    EmptyLamp = "e*"

class GameMap(object):

    iSize = 1
    Map = []

    def __init__(self,iSizeIn):
        self.iSize = iSizeIn
        for i in range(0,self.iSize):
            x = []
            for j in range(0,self.iSize):
                x.append(Tile.EmptyUnlit)
            self.Map.append(x)
        self.LoadMap()

    def PrintMap(self):
        for i in range(0,self.iSize):
            for j in range(0,self.iSize):
                print(self.Map[i][j].value,end="")
                print(" ",end="")
            print("")
    
    def LoadMap(self,): #Later change to read from file
        print("Loading Map...")
        #e- b- e- e- e- e- e-  3,3
        #e- e- e- e- b0 e- b0  2,4
        #e- b2 e- e- e- e- e-  0,2
        #e- e- e- e- e- e- e-
        #e- e- e- e- e- b- e-
        #b- e- b4 e- e- e- e-
        #e- e- e- e- e- b1 e-
        self.Map[0][0] = Tile.EmptyUnlit
        self.Map[0][1] = Tile.Block
        self.Map[0][2] = Tile.EmptyUnlit
        self.Map[0][3] = Tile.EmptyUnlit
        self.Map[0][4] = Tile.EmptyUnlit
        self.Map[0][5] = Tile.EmptyUnlit
        self.Map[0][6] = Tile.EmptyUnlit

        self.Map[1][0] = Tile.EmptyUnlit
        self.Map[1][1] = Tile.EmptyUnlit
        self.Map[1][2] = Tile.EmptyUnlit
        self.Map[1][3] = Tile.EmptyUnlit
        self.Map[1][4] = Tile.Block0
        self.Map[1][5] = Tile.EmptyUnlit
        self.Map[1][6] = Tile.Block0

        self.Map[2][0] = Tile.EmptyUnlit
        self.Map[2][1] = Tile.Block2
        self.Map[2][2] = Tile.EmptyUnlit
        self.Map[2][3] = Tile.EmptyUnlit
        self.Map[2][4] = Tile.EmptyUnlit
        self.Map[2][5] = Tile.EmptyUnlit
        self.Map[2][6] = Tile.EmptyUnlit

        self.Map[3][0] = Tile.EmptyUnlit
        self.Map[3][1] = Tile.EmptyUnlit
        self.Map[3][2] = Tile.EmptyUnlit
        self.Map[3][3] = Tile.EmptyUnlit
        self.Map[3][4] = Tile.EmptyUnlit
        self.Map[3][5] = Tile.EmptyUnlit
        self.Map[3][6] = Tile.EmptyUnlit

        self.Map[4][0] = Tile.EmptyUnlit
        self.Map[4][1] = Tile.EmptyUnlit
        self.Map[4][2] = Tile.EmptyUnlit
        self.Map[4][3] = Tile.EmptyUnlit
        self.Map[4][4] = Tile.EmptyUnlit
        self.Map[4][5] = Tile.Block
        self.Map[4][6] = Tile.EmptyUnlit

        self.Map[5][0] = Tile.Block
        self.Map[5][1] = Tile.EmptyUnlit
        self.Map[5][2] = Tile.Block4
        self.Map[5][3] = Tile.EmptyUnlit
        self.Map[5][4] = Tile.EmptyUnlit
        self.Map[5][5] = Tile.EmptyUnlit
        self.Map[5][6] = Tile.EmptyUnlit

        self.Map[6][0] = Tile.EmptyUnlit
        self.Map[6][1] = Tile.EmptyUnlit
        self.Map[6][2] = Tile.EmptyUnlit
        self.Map[6][3] = Tile.EmptyUnlit
        self.Map[6][4] = Tile.EmptyUnlit
        self.Map[6][5] = Tile.Block1
        self.Map[6][6] = Tile.EmptyUnlit

    def PlaceLamp(self,PosRow,PosCollumn):
        if(self.Map[PosRow][PosCollumn] != Tile.EmptyUnlit):
            #print("cannot place lamp...")
            return False

        print("Placing lamp at " + str(PosRow) +","+ str(PosCollumn) + " ...")
        self.Map[PosRow][PosCollumn] = Tile.EmptyLamp
        #update lighting
        self.UpdateLighting(PosRow,PosCollumn)
        return True

    def UpdateLighting(self,PosRow,PosCollumn):
        #up
        for i in range(1,PosRow+1):
            #if(self.Map[PosRow-i][PosCollumn] == Tile.Block or self.Map[PosRow-i][PosCollumn] == Tile.Block0 or self.Map[PosRow-i][PosCollumn] == Tile.Block1 or self.Map[PosRow-i][PosCollumn] == Tile.Block2 or self.Map[PosRow-i][PosCollumn] == Tile.Block3 or self.Map[PosRow-i][PosCollumn] == Tile.Block4):
            if(self.IsBlock(PosRow-i,PosCollumn)):
                break
            else:
                self.Map[PosRow-i][PosCollumn] = Tile.EmptyLit
        #down
        for j in range(1,self.iSize-PosRow): 
            #i = j - self.iSize
            #if(self.Map[PosRow+j][PosCollumn] == Tile.Block or self.Map[PosRow+j][PosCollumn] == Tile.Block0 or self.Map[PosRow+j][PosCollumn] == Tile.Block1 or self.Map[PosRow+j][PosCollumn] == Tile.Block2 or self.Map[PosRow+j][PosCollumn] == Tile.Block3 or self.Map[PosRow+j][PosCollumn] == Tile.Block4):
            if(self.IsBlock(PosRow+j,PosCollumn)):
                break
            else:
                self.Map[PosRow+j][PosCollumn] = Tile.EmptyLit
            #self.PrintMap()
            #print("")
        #left
        for i in range(1,PosCollumn+1):
            #if(self.Map[PosRow][PosCollumn-i] == Tile.Block or self.Map[PosRow][PosCollumn-i] == Tile.Block0 or self.Map[PosRow][PosCollumn-i] == Tile.Block1 or self.Map[PosRow][PosCollumn-i] == Tile.Block2 or self.Map[PosRow][PosCollumn-i] == Tile.Block3 or self.Map[PosRow][PosCollumn-i] == Tile.Block4):
            if(self.IsBlock(PosRow,PosCollumn-i)):
                break
            else:
                self.Map[PosRow][PosCollumn-i] = Tile.EmptyLit
        #right
        for j in range(1,self.iSize-PosCollumn): #Make sure it works the way its supposed to!
            #i = j - self.iSize
            #if(self.Map[PosRow][PosCollumn-i] == Tile.Block or self.Map[PosRow][PosCollumn-i] == Tile.Block0 or self.Map[PosRow][PosCollumn-i] == Tile.Block1 or self.Map[PosRow][PosCollumn-i] == Tile.Block2 or self.Map[PosRow][PosCollumn-i] == Tile.Block3 or self.Map[PosRow][PosCollumn-i] == Tile.Block4):
            if(self.IsBlock(PosRow,PosCollumn+j)):
                break
            else:
                self.Map[PosRow][PosCollumn+j] = Tile.EmptyLit

    def CheckMap(self):
        #print("Checking map...")
        for i in range(0,self.iSize):
            for j in range(0,self.iSize):

                if(self.Map[i][j]== Tile.EmptyUnlit):
                    return False
                elif(self.IsBlock(i,j)):

                    Done = False

                    if(self.Map[i][j]==Tile.Block):
                        Done = True
                    elif(self.Map[i][j]==Tile.Block0):
                        if(self.IsBlock0Done(i,j)):
                            Done = True
                    elif(self.Map[i][j] == Tile.Block1):
                        if(self.IsBlock1Done(i,j)):
                            Done = True
                    elif(self.Map[i][j] == Tile.Block2):
                        if(self.IsBlock2Done(i,j)):
                            Done = True
                    elif(self.Map[i][j] == Tile.Block3):
                        if(self.IsBlock3Done(i,j)):
                            Done = True
                    elif(self.Map[i][j] == Tile.Block4):
                        if(self.IsBlock4Done(i,j)):
                            Done = True

                    if(Done == False):
                        return False

        return True

    def IsBlock(self,PosRow,PosCollumn):
        if(self.Map[PosRow][PosCollumn] == Tile.Block or self.Map[PosRow][PosCollumn] == Tile.Block0 or self.Map[PosRow][PosCollumn] == Tile.Block1 or self.Map[PosRow][PosCollumn] == Tile.Block2 or self.Map[PosRow][PosCollumn] == Tile.Block3 or self.Map[PosRow][PosCollumn] == Tile.Block4):
            return True
        else:
            return False
    
    def IsBlock0Done(self,PosRow,PosCollumn):
        #check up
        if(PosRow>0):
            if(self.Map[PosRow-1][PosCollumn] == Tile.EmptyLamp):
                return False
        #check down
        if(PosRow<(self.iSize-1)):
            if(self.Map[PosRow+1][PosCollumn] == Tile.EmptyLamp):
                return False
        #check right
        if(PosCollumn < (self.iSize-1)):
            if(self.Map[PosRow][PosCollumn+1] == Tile.EmptyLamp):
                return False
        #check left
        if(PosCollumn > 0):
            if(self.Map[PosRow][PosCollumn-1] == Tile.EmptyLamp):
                return False

        return True

    def IsBlock1Done(self,PosRow,PosCollumn):
        iLamps = 0
        #check up
        if(PosRow>0):
            if(self.Map[PosRow-1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check down
        if(PosRow<(self.iSize-1)):
            if(self.Map[PosRow+1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check right
        if(PosCollumn < (self.iSize-1)):
            if(self.Map[PosRow][PosCollumn+1] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check left
        if(PosCollumn > 0):
            if(self.Map[PosRow][PosCollumn-1] == Tile.EmptyLamp):
                iLamps = iLamps+1

        if(iLamps == 1):
            return True
        else:
            return False

    def IsBlock2Done(self,PosRow,PosCollumn):
        iLamps = 0
        #check up
        if(PosRow>0):
            if(self.Map[PosRow-1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check down
        if(PosRow<(self.iSize-1)):
            if(self.Map[PosRow+1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check right
        if(PosCollumn < (self.iSize-1)):
            if(self.Map[PosRow][PosCollumn+1] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check left
        if(PosCollumn > 0):
            if(self.Map[PosRow][PosCollumn-1] == Tile.EmptyLamp):
                iLamps = iLamps+1

        if(iLamps == 2):
            return True
        else:
            return False
    def IsBlock3Done(self,PosRow,PosCollumn):
        iLamps = 0
        #check up
        if(PosRow>0):
            if(self.Map[PosRow-1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check down
        if(PosRow<(self.iSize-1)):
            if(self.Map[PosRow+1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check right
        if(PosCollumn < (self.iSize-1)):
            if(self.Map[PosRow][PosCollumn+1] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check left
        if(PosCollumn > 0):
            if(self.Map[PosRow][PosCollumn-1] == Tile.EmptyLamp):
                iLamps = iLamps+1

        if(iLamps == 3):
            return True
        else:
            return False

    def IsBlock4Done(self,PosRow,PosCollumn):
        iLamps = 0
        #check up
        if(PosRow>0):
            if(self.Map[PosRow-1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check down
        if(PosRow<(self.iSize-1)):
            if(self.Map[PosRow+1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check right
        if(PosCollumn < (self.iSize-1)):
            if(self.Map[PosRow][PosCollumn+1] == Tile.EmptyLamp):
                iLamps = iLamps+1
        #check left
        if(PosCollumn > 0):
            if(self.Map[PosRow][PosCollumn-1] == Tile.EmptyLamp):
                iLamps = iLamps+1

        if(iLamps == 4):
            return True
        else:
            return False

class Node():
    state = 0
    parent = 0
    nodesToVisit = []
    steps = 0
    def __init__(self,state,parent,steps):
        self.state = state
        self.parent = parent
        self.steps = steps
    
    def UpdateNodesToVisit(self):  #Push all available moves to the stack
        for y in range(0,6):
            for x in range(0,6):
                if(self.state.Map[y][x] == Tile.EmptyUnlit):  #if the move is valid
                    temp=deepcopy(self.state)                 #deep copy of current Node state
                    #temp.PrintMap()
                    temp.PlaceLamp(y,x)                       #Modify current state
                    self.nodesToVisit.append(temp)            #Add modified state to the stack

def Test():
    Map = GameMap(7)
    #Map.PrintMap()
    root = Node(Map,Map,Map)
   # root.state.PrintMap()
    root.UpdateNodesToVisit()
    n=len(root.nodesToVisit)
    print(n)

Test()
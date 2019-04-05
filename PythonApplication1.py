from enum import Enum
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

    def __init__(self, iSizeIn):
        self.Map = []
        self.iSize = iSizeIn
        for i in range(0, self.iSize):
            x = []
            for j in range(0, self.iSize):
                x.append(Tile.EmptyUnlit)
            self.Map.append(x)
        self.loadmap()

    def CopyMap(self, GMap):
        if (self.iSize != GMap.iSize):
            print("Cannot Copy maps of different sizes")
            return
        else:
            for i in range(0, self.iSize):
                for j in range(0, self.iSize):
                    if (GMap.Map[i][j] == Tile.Block):
                        self.Map[i][j] = Tile.Block
                    elif (GMap.Map[i][j] == Tile.Block0):
                        self.Map[i][j] = Tile.Block0
                    elif (GMap.Map[i][j] == Tile.Block1):
                        self.Map[i][j] = Tile.Block1
                    elif (GMap.Map[i][j] == Tile.Block2):
                        self.Map[i][j] = Tile.Block2
                    elif (GMap.Map[i][j] == Tile.Block3):
                        self.Map[i][j] = Tile.Block3
                    elif (GMap.Map[i][j] == Tile.Block4):
                        self.Map[i][j] = Tile.Block4
                    elif (GMap.Map[i][j] == Tile.EmptyLamp):
                        self.Map[i][j] = Tile.EmptyLamp
                    elif (GMap.Map[i][j] == Tile.EmptyLit):
                        self.Map[i][j] = Tile.EmptyLit
                    elif (GMap.Map[i][j] == Tile.EmptyUnlit):
                        self.Map[i][j] = Tile.EmptyUnlit
                    # print(self.Map[i][j].value,end="")
                # print("")

    def PrintMapConsole(self):
        for i in range(0, self.iSize):
            for j in range(0, self.iSize):
                print(self.Map[i][j].value, end="")
                print(" ", end="")
            print("")

    def loadmap(self, ):  # Later change to read from file
        print("Loading Map...")
        # e- b- e- e- e- e- e-  3,3
        # e- e- e- e- b0 e- b0  2,4
        # e- b2 e- e- e- e- e-  0,2
        # e- e- e- e- e- e- e-
        # e- e- e- e- e- b- e-
        # b- e- b4 e- e- e- e-
        # e- e- e- e- e- b1 e-
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

    def fLoadMap(self, sPath):
        print("Loading from file " + sPath)

        tile = None
        iter = 0

        try:
            with open(sPath) as mapfile:
                while True:
                    tile = mapfile.read(1)

                    if (tile == 'E'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.EmptyUnlit
                    elif (tile == 'B'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.Block
                    elif (tile == '0'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.Block0
                    elif (tile == '1'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.Block1
                    elif (tile == '2'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.Block2
                    elif (tile == '3'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.Block3
                    elif (tile == '4'):
                        self.Map[(int)(iter / 7)][iter % 7] = Tile.Block4

                    iter = iter + 1

                    if not tile:
                        break


        except IOError:
            print("Cannot open file...")
            return
        print("", end="")

    def PlaceLamp(self, PosRow, PosCollumn):
        if (self.Map[PosRow][PosCollumn] == Tile.EmptyLit):
            print("cannot place lamps in lit spaces...")
            return

        self.Map[PosRow][PosCollumn] = Tile.EmptyLamp
        # update lighting

        self.UpdateLighting(PosRow, PosCollumn)

    def UpdateLighting(self, PosRow, PosCollumn):
        # up
        for i in range(1, PosRow + 1):
            # if(self.Map[PosRow-i][PosCollumn] == Tile.Block or self.Map[PosRow-i][PosCollumn] == Tile.Block0 or self.Map[PosRow-i][PosCollumn] == Tile.Block1 or self.Map[PosRow-i][PosCollumn] == Tile.Block2 or self.Map[PosRow-i][PosCollumn] == Tile.Block3 or self.Map[PosRow-i][PosCollumn] == Tile.Block4):
            if (self.IsBlock(PosRow - i, PosCollumn)):
                break
            else:
                self.Map[PosRow - i][PosCollumn] = Tile.EmptyLit
        # down
        for j in range(1, self.iSize - PosRow):
            # i = j - self.iSize
            # if(self.Map[PosRow+j][PosCollumn] == Tile.Block or self.Map[PosRow+j][PosCollumn] == Tile.Block0 or self.Map[PosRow+j][PosCollumn] == Tile.Block1 or self.Map[PosRow+j][PosCollumn] == Tile.Block2 or self.Map[PosRow+j][PosCollumn] == Tile.Block3 or self.Map[PosRow+j][PosCollumn] == Tile.Block4):
            if (self.IsBlock(PosRow + j, PosCollumn)):
                break
            else:
                self.Map[PosRow + j][PosCollumn] = Tile.EmptyLit
            # self.PrintMap()
            # print("")
        # left
        for i in range(1, PosCollumn + 1):
            # if(self.Map[PosRow][PosCollumn-i] == Tile.Block or self.Map[PosRow][PosCollumn-i] == Tile.Block0 or self.Map[PosRow][PosCollumn-i] == Tile.Block1 or self.Map[PosRow][PosCollumn-i] == Tile.Block2 or self.Map[PosRow][PosCollumn-i] == Tile.Block3 or self.Map[PosRow][PosCollumn-i] == Tile.Block4):
            if (self.IsBlock(PosRow, PosCollumn - i)):
                break
            else:
                self.Map[PosRow][PosCollumn - i] = Tile.EmptyLit
        # right
        for j in range(1, self.iSize - PosCollumn):  # Make sure it works the way its supposed to!
            # i = j - self.iSize
            # if(self.Map[PosRow][PosCollumn-i] == Tile.Block or self.Map[PosRow][PosCollumn-i] == Tile.Block0 or self.Map[PosRow][PosCollumn-i] == Tile.Block1 or self.Map[PosRow][PosCollumn-i] == Tile.Block2 or self.Map[PosRow][PosCollumn-i] == Tile.Block3 or self.Map[PosRow][PosCollumn-i] == Tile.Block4):
            if (self.IsBlock(PosRow, PosCollumn + j)):
                break
            else:
                self.Map[PosRow][PosCollumn + j] = Tile.EmptyLit

    def CheckMap(self):
        # print("Checking map...")
        for i in range(0, self.iSize):
            for j in range(0, self.iSize):

                if (self.Map[i][j] == Tile.EmptyUnlit):
                    return False
                elif (self.IsBlock(i, j)):

                    Done = False

                    if (self.Map[i][j] == Tile.Block):
                        Done = True
                    elif (self.Map[i][j] == Tile.Block0):
                        if (self.IsBlock0Done(i, j)):
                            Done = True
                    elif (self.Map[i][j] == Tile.Block1):
                        if (self.IsBlock1Done(i, j)):
                            Done = True
                    elif (self.Map[i][j] == Tile.Block2):
                        if (self.IsBlock2Done(i, j)):
                            Done = True
                    elif (self.Map[i][j] == Tile.Block3):
                        if (self.IsBlock3Done(i, j)):
                            Done = True
                    elif (self.Map[i][j] == Tile.Block4):
                        if (self.IsBlock4Done(i, j)):
                            Done = True

                    if (Done == False):
                        return False

        return True

    def IsBlock(self, PosRow, PosCollumn):
        if (self.Map[PosRow][PosCollumn] == Tile.Block or self.Map[PosRow][PosCollumn] == Tile.Block0 or
                self.Map[PosRow][PosCollumn] == Tile.Block1 or self.Map[PosRow][PosCollumn] == Tile.Block2 or
                self.Map[PosRow][PosCollumn] == Tile.Block3 or self.Map[PosRow][PosCollumn] == Tile.Block4):
            return True
        else:
            return False

    def IsBlock0Done(self, PosRow, PosCollumn):
        # check up
        if (PosRow > 0):
            if (self.Map[PosRow - 1][PosCollumn] == Tile.EmptyLamp):
                return False
        # check down
        if (PosRow < (self.iSize - 1)):
            if (self.Map[PosRow + 1][PosCollumn] == Tile.EmptyLamp):
                return False
        # check right
        if (PosCollumn < (self.iSize - 1)):
            if (self.Map[PosRow][PosCollumn + 1] == Tile.EmptyLamp):
                return False
        # check left
        if (PosCollumn > 0):
            if (self.Map[PosRow][PosCollumn - 1] == Tile.EmptyLamp):
                return False

        return True

    def IsBlock1Done(self, PosRow, PosCollumn):
        iLamps = 0
        # check up
        if (PosRow > 0):
            if (self.Map[PosRow - 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check down
        if (PosRow < (self.iSize - 1)):
            if (self.Map[PosRow + 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check right
        if (PosCollumn < (self.iSize - 1)):
            if (self.Map[PosRow][PosCollumn + 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check left
        if (PosCollumn > 0):
            if (self.Map[PosRow][PosCollumn - 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1

        if (iLamps == 1):
            return True
        else:
            return False

    def IsBlock2Done(self, PosRow, PosCollumn):
        iLamps = 0
        # check up
        if (PosRow > 0):
            if (self.Map[PosRow - 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check down
        if (PosRow < (self.iSize - 1)):
            if (self.Map[PosRow + 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check right
        if (PosCollumn < (self.iSize - 1)):
            if (self.Map[PosRow][PosCollumn + 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check left
        if (PosCollumn > 0):
            if (self.Map[PosRow][PosCollumn - 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1

        if (iLamps == 2):
            return True
        else:
            return False

    def IsBlock3Done(self, PosRow, PosCollumn):
        iLamps = 0
        # check up
        if (PosRow > 0):
            if (self.Map[PosRow - 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check down
        if (PosRow < (self.iSize - 1)):
            if (self.Map[PosRow + 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check right
        if (PosCollumn < (self.iSize - 1)):
            if (self.Map[PosRow][PosCollumn + 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check left
        if (PosCollumn > 0):
            if (self.Map[PosRow][PosCollumn - 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1

        if (iLamps == 3):
            return True
        else:
            return False

    def IsBlock4Done(self, PosRow, PosCollumn):
        iLamps = 0
        # check up
        if (PosRow > 0):
            if (self.Map[PosRow - 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check down
        if (PosRow < (self.iSize - 1)):
            if (self.Map[PosRow + 1][PosCollumn] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check right
        if (PosCollumn < (self.iSize - 1)):
            if (self.Map[PosRow][PosCollumn + 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1
        # check left
        if (PosCollumn > 0):
            if (self.Map[PosRow][PosCollumn - 1] == Tile.EmptyLamp):
                iLamps = iLamps + 1

        if (iLamps == 4):
            return True
        else:
            return False


# Node

class Node():
    state = None
    parent = None
    nodesToVisit = []
    steps = None
    visited = False

    def __init__(self, state, parent, steps):
        self.state = state
        self.parent = parent
        self.steps = steps


    def UpdateNodesToVisit(self):  # Push all available moves to the stack
        self.nodesToVisit= []
        for y in range(0, 7):
            for x in range(0, 7):
                if self.state.Map[y][x] == Tile.EmptyUnlit:  # if the move is valid
                    temp = Node(self.state, self.parent, self.steps)
                    temp.state = deepcopy(self.state)
                    temp.parent = deepcopy(self.parent)
                    temp.steps = deepcopy(self.steps)
                    temp.state.PlaceLamp(y, x)  # Modify current state
                    self.nodesToVisit.append(temp)


def depthfirstsearch(node):
    # initial
    root = Node(node.state, node.parent, node.steps)
    root.UpdateNodesToVisit()
    visited = []
    a = root.nodesToVisit
    # main loop
    while a:
        x = a.pop()
        x.UpdateNodesToVisit()
        if x.state.CheckMap():
            return x
        # check for visited states
        flag = 0
        for r in visited:
            for p in x.nodesToVisit:
                if p.state == r.state:
                    flag = 1
                    print("flag")
        # if states were not visited append to stack
        if flag == 0:
            visited.append(x)
            for n in x.nodesToVisit:
                a.append(n)












def test():
    map = GameMap(7)
    # Map.PrintMap()
    root = Node(map,map,map)
    d = depthfirstsearch(root)
    d.state.PrintMapConsole()

test()
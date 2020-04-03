from array import *
import random
class Board:
    # data = ""
    def getPos(self,x,y): #returns what is in the selected spot
        #x is column, y is row
        a = self.data[y]
        return a[x]

    def setPos(self, x, y, num):
        print("setting {0},{1} to {2}".format(x,y,num))
        a = self.data[y]
        a[x] = num

    def __init__(self): #currently just 9x9 board
        self.data = [None] * 9
        for c in range(0,9):
            self.data[c] = [None] * 9


    def printBoard(self): #this method tests the 2d array
        for x in self.data:
            print(x)

    def getBoard(self):
        return self.data

    def checkRow(self, yPos):
        valid = True
        print("checking row ", yPos)
        currentRow = self.data[yPos]
        for i in range(1, 10):
            if currentRow.count(i) > 1:
                valid = False
                print("error")
        if(valid):
            print("row okay")

    def checkColumn(self, xPos):
        currentColumn = []
        for i in range(0, 9):
            currentColumn.append(self.getPos(xPos, i))
        print("column: ",currentColumn)
        for i in range(1, 10):
            if currentColumn.count(i) > 1:
                valid = False

                print("error at ",i)
        if(valid):
            print("Column okay")

    def checkSquare(self, xPos, yPos):
        xSquare = self.getSquareCoord(xPos)
        ySquare = self.getSquareCoord(yPos)
        # print("square at {}, {}".format(xSquare, ySquare))
        SquareList = []
        # print("checking square")
        for i in range(xSquare - 1, xSquare + 2):
            for j in range(ySquare - 1, ySquare + 2):
                # print("adding ",self.getPos(j, i)," from ",i,",",j)
                SquareList.append(self.getPos(j, i))
        print("\n",SquareList)
        for i in range(1, 10):
            if SquareList.count(i) > 1:
                valid = False
                print("error at ",i)
        if(valid):
            print("Square okay")

    def getSquareCoord(self,i):
        if i <= 3:
            return 1
        elif i <= 7:
            return 4
        else:
            return 7
    def setBoard(self, newBoard):
        self.data = newBoard

    def createBoardFromFile(self):
        file = open("SampleBoards.txt")
        fileData = file.read()
        f2 = fileData.rstrip('\n')
        input = f2.split(',')
        for x in range(0, 9):
            a = [int(d) for d in str(input[x])]
            input[x] = a
        self.setBoard(input)


# #
# b = Board()
# b.createBoardFromFile()
# b.setPos(8,8,999)
# b.printBoard()

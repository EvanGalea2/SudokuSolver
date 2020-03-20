from array import *
import random
class Board:
    # data = ""
    def getPos(self,x,y): #returns what is in the selected spot
        #x is column, y is row
        a = self.data[y]
        return a[x]

    def __init__(self): #currently just 9x9 board
        self.data = [None] * 9
        for c in range(0,9):
            self.data[c] = [None] * 9

    def fillBoard(self):
        for x in range(0, 9):
            a = self.data[x]
            for y in range(0, 9):
                a[y] = random.randint(1,9)

    def testBoard(self): #this method tests the 2d array
        for x in self.data:
            print(x)

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
    #     print "checking column"
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



b = Board()
b.fillBoard()
b.testBoard()
# b.checkRow(3)
# b.checkColumn(5)
# b.checkSquare(0,0)
# print("position at 3, 2 is ", b.getPos(3,2))
print("test end")

file = open("SampleBoards.txt")

# print(f.read())
fileData = file.read()
# [line.rstrip('\n') for line in file]
f2 = fileData.rstrip('\n')
print(f2)
input = f2.split(',')
print(input)
for b in input:

    b = [int(d) for d in str(b)]
    print(b)
print(input)

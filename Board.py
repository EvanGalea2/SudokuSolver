from array import *

class Board:
    # data = ""

    def __init__(self): #currently just 9x9 board
        self.data = [9]
        for x in self.data:
            x = [9]

    def testBoard(self): #this method tests the 2d array
        for x in range(0, 8):
            for y in range(0, 8):
                a = self.data[x]
                a[y] = y
    def checkRow(self, yPos):
        print "checking row"
    def checkColumn(self, xPos):
        print "checking column"
    def checkSquare(self, xPos):
        print "checking square"

    # def checkAll():
    #     checkRow()
    #     checkColumn()
    #     checkSquare()

    def printBoard(self):
        for x in range(0, 8):
            for y in range(0, 8):
                print(x + " " + y)
b = Board()
b.testBoard()
print("test")
b.printBoard()

from tkinter import *
from functools import partial
import Board
import UserInput

class GUI:
    def __init__(self):
        self.Application = Tk()
        self.frame = Frame(self.Application)
        self.frame.grid()
        self.buttonList = []
        self.strList = []
        self.data = Board.Board()
        self.initialiseBoard(self.frame)
        testButton = Button(self.frame, text='load board', command=self.updateBoard)
        testButton.grid(row = 0, column = 10)
        print("end")
        # self.updateGUI()
        # self.test()
        self.Application.mainloop()

    def pressButton(self, x, y):
        print("You have pressed ",x,", ",y)
        row = self.buttonList[y]
        button = row[x]
        button['bg'] = '#8c8c8c'
        UI = UserInput.UserInput(self, x, y)

    def setPosition(self, x, y, num):
        print("num is ",num)
        self.data.setPos(x,y,num)
        self.updateBoard()

    def updateBoard(self):
        self.data.createBoardFromFile()
        self.data.printBoard()
        for y in range(0, 9):
            e = self.strList[y]
            data = self.data.getBoard()[y]
            for x in range(0, 9):
                e[x].set(data[x])

    def initialiseBoard(self, frame):
        for y in range(0, 9):
            buttonRow = []
            strRow = []
            self.buttonList.append(buttonRow)
            self.strList.append(strRow)
            for x in range(0, 9):
                currentStr = StringVar()
                currentStr.set((x,",",y))
                # button = Button(board, text=(x,",",y), command=partial(self.pressButton, x, y))
                button = Button(frame, textvariable=currentStr, command=partial(self.pressButton, x, y))
                button.grid(row = y, column = x)
                buttonRow.append(button)
                strRow.append(currentStr)
    # for r in buttonList:
    #     print(r)
g = GUI()
g.setPosition(3,3,80)
# b = Board()
# updateGUI()

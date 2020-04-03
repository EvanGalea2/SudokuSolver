from tkinter import *

class UserInput:
    def __init__(self, mainGUI, x, y):
        self.mainApplication = mainGUI
        self.x = x
        self.y = y
        self.Application = Tk()
        self.frame = Frame(self.Application)
        self.frame.grid()
        self.v = IntVar()
        self.textBox = Entry(self.frame, textvariable = self.v)
        self.textBox.grid()
        self.enterButton = Button(self.frame, text = 'enter', command = self.pressButton)
        self.enterButton.grid()
        self.Application.mainloop()

    def pressButton(self):

        self.mainApplication.setPosition(self.x,self.y,self.v.get())
        self.Application.destroy()
        print(self.textBox.get())

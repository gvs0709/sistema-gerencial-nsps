from tkinter import *
from tkinter import ttk

class moduleWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Module Template")
        self.geometry('400x600')
        self.protocol("WM_DELETE_WINDOW", self.onFinish)

        self.parent = parent
        """self.myLable = Label(self, text ="Hello world!", font = ("sans bold", 20))
        self.myLable.grid(row = "0", column = "0")
        self.moduleBtn = Button(self, text="Finish Module", command = self.onFinish)
        self.moduleBtn.grid(row = "0", column = "1")"""

    def onFinish(self):
        self.parent.onClose(__name__)
        self.destroy()

    #def smth(self):
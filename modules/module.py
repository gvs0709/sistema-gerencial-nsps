import tkinter as tk
from tkinter import ttk

class moduleWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Module 1")
        self.geometry('400x600')
        self.protocol("WM_DELETE_WINDOW", self.onFinish)

        self.parent = parent
        self.myLable = tk.Label(self, text ="Hello world!", font = ("sans bold", 20))
        self.myLable.grid(row = "0", column = "0")
        self.closeBtn = tk.Button(self, text="Encerrar", command = self.onFinish)
        self.closeBtn.grid(row = "0", column = "1")

    def onFinish(self):
        self.parent.onClose(__name__)
        self.destroy()

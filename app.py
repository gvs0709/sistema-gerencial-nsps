import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import modules
import os
import importlib as imp
import shutil
from pathlib import Path

"""myLable = Label(window, text ="Hello world!", font = ("sans bold", 20))
myLable2 = Label(window, text ="Luke, I am your father")
txt = Entry(window, width = 30, state = 'disabled')

def clicked():
    res = txt.get()
    myLable.configure(text = res)

btn = Button(window, text="Click Me", command = clicked)

myLable.grid(row = 0, column = 0)
myLable2.grid(row = 1, column = 1)
btn.grid(column=1, row=0)
txt.grid(row = 3, column = 0)
txt.focus()"""

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.files = os.listdir("modules") #Search for modules in the 'modules' directory
        self.files.remove("__init__.py")
        l = len(self.files)
        i = 0

        while(True):
            if i < l:
                if self.files[i][len(self.files[i])-3:] != ".py": #Checks if the current file is a '.py' (python) file
                    self.files.remove(self.files[i]) #If its not remove it
                    l = len(self.files) #And update the list lenght
            
                else: #If its a python file
                    self.files[i] = self.files[i][:-3] #Remove '.py' from the end of module file name
                    i += 1 #Update index
            
            else:
                break
        
        self.title("Gerenciador de Módulos")
        self.geometry('400x300')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.modulesLable = tk.Label(self, text ="Serviços Paroquiais", font = ("Times bold", 20))
        self.selectedModule = tk.StringVar()
        self.modulesCombobox = ttk.Combobox(self, textvariable = self.selectedModule)
        self.modulesCombobox['values'] = self.files #Available modules
        self.modulesCombobox['state'] = 'readonly'
        self.selectBtn = tk.Button(self, text = "Selecionar", command = self.onSelect)
        self.unistallBtn = tk.Button(self, text = "Desinstalar", command = self.unistall)
        self.installBtn = tk.Button(self, text = "Instalar Módulo", command = self.install)
        self.running = []

    def onSelect(self):
        module = self.selectedModule.get()

        if module != "":
            while(True):
                try:
                    if module in self.running:
                        #exec("modules." + module + ".focus_set()")
                        #print("Módulo em execução!")
                        messagebox.showinfo("Informação", f"O módulo {module} já está em execução")
                        break
                    
                    else:
                        exec("modules." + module + ".moduleWindow(self)")
                        self.running.append(module)
                        #window = module.moduleWindow(self)
                        #window.grab_set()
                        break
                
                except AttributeError: #If a new module is not imported, adds it in modules/__init__.py and automaticly executes it
                    self.install(module + ".py")
    
    def unistall(self):
        module = self.selectedModule.get()

        if module != "":
            if module in self.running:
                messagebox.showwarning("Aviso", "Feche o módulo antes de desintalá-lo")
            
            elif messagebox.askokcancel("Atenção", f"Deseja mesmo desinstalar o módulo {module}?", icon = "question"):
                path = "modules/"

                with open(path + "__init__.py", "r") as old:
                    with open(path + "new.py", "w") as new:
                        for line in old:
                            if line.strip("\n") != "from . import " + module and line != "\n":
                                new.write(line)

                os.remove(path + "__init__.py")
                os.replace(path + "new.py", path + "__init__.py")
                os.remove(path + module + ".py")
                imp.reload(modules)

                self.selectedModule.set("")
                self.files.remove(module)
                self.modulesCombobox['values'] = self.files
    
    def install(self, fileName = None):
        if fileName == None: #Method was invoked by the user trough the 'install' button
            module = filedialog.askopenfilename(initialdir = os.path.expanduser('~'), title = "Escolha um arquivo", filetypes = [("Python Files", "*.py")])

            if module != () and os.path.isfile(module): #If the user clicks 'Cancel' 'module' is empty, if 'module' has something then proceed
                module = Path(module)
                #if module.suffix == ".py":
                shutil.copy(module, "modules")
                
                """else:
                    messagebox.showwarning("Aviso", f"{module.name} não é um arquivo Python!")
                    module = ()"""
        
        else: #Method was invoked by another method
            module = Path(fileName)

        if module != () and os.path.isfile(module): #If the user clicks 'Cancel' 'module' is empty, if 'module' has something then proceed
            with open("modules/__init__.py", "a+") as f:
                f.seek(0)

                if "from . import " + module.stem + "\n" in f.read():
                    messagebox.showinfo("Atenção", f"O módulo {module.stem} já foi instalado anteriormente")
                
                else:
                    f.write("from . import " + module.stem + "\n")
                    
            imp.reload(modules)

            if module.stem not in self.files:
                self.files.append(module.stem)
                self.modulesCombobox['values'] = self.files

    def onClose(self, data = None): #Recieves the name of the module being closed in 'data' as 'modules.<module_name>'
        if data != None: #Method was invoked by a child window (module)
            self.running.remove(data[8:]) #Ignores the 'modules.' part from 'data' to get the <module_name>
        
        else: #Method was invoked by the main window
            if len(self.running) > 0: #Checks if there are modules still running
                if messagebox.askokcancel("Atenção", "Fechar todos os módulos em execução e sair?", icon = "question"):
                    self.running = []
                    self.destroy()

            else: #If the user clicks in the 'Cancel' button above the window wont close thanks to this 'else'
                self.destroy()

    def run(self):
        self.modulesLable.pack(padx = 10, pady = 5, side = tk.TOP)
        self.modulesCombobox.pack(pady = 5, side = tk.TOP)
        #self.modulesCombobox.bind('<<ComboboxSelected>>', self.onSelect)
        self.selectBtn.place(relx = 0.38, rely = 0.26)
        self.unistallBtn.place(relx = 0.375, rely = 0.37)
        self.installBtn.place(relx = 0.34, rely = 0.48)

        self.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()

import tkinter as tk
from tkinter import ttk
from tkinter import font
import datetime

class moduleWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Formulário Dízimo")
        self.geometry('800x600')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.onFinish)

        #-----Cabeçalho-----#
        self.parent = parent
        self.paroco = "Michel" #Mudar forma de obter/armazenar o nome do pároco!
        self.pastoral = tk.Label(self, text = "Pastoral do Dízimo", font = ("Times bold", 20))
        self.pastoral.pack(side = tk.TOP)

        self.subTitle = tk.Label(self, text = f"Valores retidos para entrega ao Padre {self.paroco}", font = ("Times", 16))
        self.subTitle.pack(side = tk.TOP)

        self.xPosLeft = 0.1
        self.xPosRight = 0.5
        self.data = tk.Label(self, text = datetime.datetime.now().strftime("Dia: %d / %m / %Y"), font = ("Times", 14))
        self.data.place(relx = self.xPosLeft+0.05, rely = 0.13)

        self.turno = tk.Label(self, text = "Missas:", font = ("Times", 16))
        self.turno.place(relx = self.xPosRight+0.05, rely = 0.128)

        self.selected = tk.StringVar()
        self.turnoCombobox = ttk.Combobox(self, textvariable = self.selected)
        self.turnoCombobox['values'] = ["manhã", "tarde", "noite"]
        self.turnoCombobox['state'] = 'readonly'
        self.turnoCombobox.place(relx = self.xPosRight+0.15, rely = 0.128)

        #-----Tabela na esquerda-----#
        self.contrib = tk.Label(self, text = "Contribuições", font = ("Times bold", 14))
        self.contrib.place(relx = self.xPosLeft, rely = 0.2)

        self.valores = tk.Label(self, text = "Valores", font = ("Times bold", 14))
        self.valores.place(relx = self.xPosLeft+0.2, rely = 0.2)

        self.dizimo = tk.Label(self, text = "Dízimo", font = ("Times", 14))
        self.dizimo.place(relx = self.xPosLeft, rely = 0.25)

        self.valorDizimo = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorDizimo.place(relx = self.xPosRight-0.2, rely = 0.25)

        self.obras = tk.Label(self, text = "Obras", font = ("Times", 14))
        self.obras.place(relx = self.xPosLeft, rely = 0.3)

        self.valorObras = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorObras.place(relx = self.xPosRight-0.2, rely = 0.3)

        self.ovs = tk.Label(self, text = "O.V.S", font = ("Times", 14))
        self.ovs.place(relx = self.xPosLeft, rely = 0.35)

        self.valorOVS = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorOVS.place(relx = self.xPosRight-0.2, rely = 0.35)

        self.radioCatedral = tk.Label(self, text = "Rádio Catedral", font = ("Times", 14))
        self.radioCatedral.place(relx = self.xPosLeft, rely = 0.4)

        self.valorRadioCat = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorRadioCat.place(relx = self.xPosRight-0.2, rely = 0.4)

        self.morada = tk.Label(self, text = "Morada", font = ("Times", 14))
        self.morada.place(relx = self.xPosLeft, rely = 0.45)

        self.valorMorada = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorMorada.place(relx = self.xPosRight-0.2, rely = 0.45)

        self.outras = tk.Label(self, text = "Outras", font = ("Times", 14))
        self.outras.place(relx = self.xPosLeft, rely = 0.5)

        self.valorOutras = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorOutras.place(relx = self.xPosRight-0.2, rely = 0.5)

        self.total = tk.Label(self, text = "TOTAL", font = ("Times", 14))
        self.total.place(relx = self.xPosLeft, rely = 0.55)

        self.valorTotal = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorTotal.place(relx = self.xPosRight-0.2, rely = 0.55)

        #-----Tabela na direita-----#
        self.resumo = tk.Label(self, text = "Resumo", font = ("Times bold", 14))
        self.resumo.place(relx = self.xPosRight+0.15, rely = 0.2)

        self.pgto = tk.Label(self, text = "Pgto. em", font = ("Times bold", 14))
        self.pgto.place(relx = self.xPosRight+0.05, rely = 0.25)

        self.valor = tk.Label(self, text = "Valor", font = ("Times bold", 14))
        self.valor.place(relx = self.xPosRight+0.25, rely = 0.25)

        self.dinheiro = tk.Label(self, text = "Dinheiro", font = ("Times bold", 14))
        self.dinheiro.place(relx = self.xPosRight+0.05, rely = 0.35)

        self.valorDinheiro = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorDinheiro.place(relx = self.xPosRight+0.25, rely = 0.35)

        self.cheque = tk.Label(self, text = "Cheque", font = ("Times bold", 14))
        self.cheque.place(relx = self.xPosRight+0.05, rely = 0.45)

        self.valorCheque = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorCheque.place(relx = self.xPosRight+0.25, rely = 0.45)

        self.resumoTotal = tk.Label(self, text = "TOTAL", font = ("Times bold", 14))
        self.resumoTotal.place(relx = self.xPosRight+0.05, rely = 0.55)

        self.valorResumo = tk.Text(self, height = 1, width = 7, font = ("Times", 14))
        self.valorResumo.place(relx = self.xPosRight+0.25, rely = 0.55)

        #-----Rodapé-----#
        self.funcionario = tk.Label(self, text = "Funcionário de Plantão:", font = ("Times bold", 14))
        self.funcionario.place(relx = self.xPosLeft, rely = 0.7)

        self.valorFuncionario = tk.Text(self, height = 1, width = 42, font = ("Times", 14))
        self.valorFuncionario.place(relx = self.xPosRight-0.1, rely = 0.7)

        self.obs = tk.Label(self, text = "Obs:", font = ("Times bold", 14))
        self.obs.place(relx = self.xPosLeft, rely = 0.75)

        self.valorObs = tk.Text(self, height = 1, width = 60, font = ("Times", 14))
        self.valorObs.place(relx = self.xPosRight-0.3, rely = 0.75)

        self.plantonista = tk.Label(self, text = "Plantonista(s):", font = ("Times bold", 14))
        self.plantonista.place(relx = self.xPosLeft, rely = 0.8)

        self.valorPlantonista = tk.Text(self, height = 1, width = 51, font = ("Times", 14))
        self.valorPlantonista.place(relx = self.xPosRight-0.2, rely = 0.8)
        
        #self.closeBtn = tk.Button(self, text="Encerrar", command = self.onFinish)
        #self.closeBtn.grid(row = "1", column = "1")

    def onFinish(self):
        self.parent.onClose(__name__)
        self.destroy()
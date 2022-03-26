import tkinter as tk
from PIL import Image, ImageTk

class Lamp():
    def __init__(self):
        self.on = False
    
    def press(self):
        self.on = not self.on

root = tk.Tk()

lamp = Lamp()

desligado = ImageTk.PhotoImage(Image.open('lampoff.png'))
ligado = ImageTk.PhotoImage(Image.open('lampon.png'))
tela = tk.Canvas(root, width=200)
tela.grid(rowspan=2, columnspan=1)
ini = tk.Label(root, image=desligado)
ini.grid(row=0, column=0)


def on_off():

    lamp.press()

    # A variavel luz é um operador ternário em Python que altera a imagem ligado desligado
    luz = tk.Label(root, image=ligado) if lamp.on else tk.Label(root, image=desligado)
    luz.grid(row=0, column=0)

texto = tk.StringVar()
bt = tk.Button(root, textvariable=texto, command=lambda: on_off())
texto.set('ON OFF')
bt.grid(row=1)

root.mainloop()

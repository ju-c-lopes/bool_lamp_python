import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
ligar = False
desligado = ImageTk.PhotoImage(Image.open('lampoff.png'))
ligado = ImageTk.PhotoImage(Image.open('lampon.png'))
tela = tk.Canvas(root, width=200)
tela.grid(rowspan=2, columnspan=1)
ini = tk.Label(root, image=desligado)
ini.grid(row=0, column=0)

def on_off():
    global ligar
    ligar = not ligar

    # A variavel luz é um operador ternário em Python que altera a imagem ligado desligado
    luz = tk.Label(root, image=ligado) if ligar else tk.Label(root, image=desligado)
    luz.grid(row=0, column=0)

texto = tk.StringVar()
bt = tk.Button(root, textvariable=texto, command=lambda: on_off())
texto.set('ON OFF')
bt.grid(row=1)

root.mainloop()

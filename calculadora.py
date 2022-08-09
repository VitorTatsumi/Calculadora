from tkinter import *

janela = Tk()
janela.title('Calculadora Tatsumi')
janela.resizable(width=False, height=False)

valor1 = Label(janela, text='Valor 1:')
valor1.grid(row=0, column=0)
entrada1 = Entry(janela, width=10)
entrada1.grid(row=0, column = 1)

valor2 = Label(janela, text='Valor 2:')
valor2.grid(row=1, column=0)
entrada2 = Entry(janela, width=10)
entrada2.grid(row=1, column = 1)

#Soma
def soma():
    v1 = entrada1.get()
    v2 = entrada2.get()
    resultado["text"] = int(v1) + int(v2)

bsoma = Button(janela, text=' + ', bg='gray', command = soma, width=10)
bsoma.grid(row=2, column=0)

#Subtração
def sub():
    v1 = entrada1.get()
    v2 = entrada2.get()
    resultado["text"] = int(v1) - int(v2)

bsub = Button(janela, text=' - ', bg='gray', command = sub, width=10)
bsub.grid(row=2, column=1)

#Multiplicação
def mult():
    v1 = entrada1.get()
    v2 = entrada2.get()
    resultado["text"] = int(v1) * int(v2)

bmult = Button(janela, text=' X ', bg='gray', command = mult, width=10)
bmult.grid(row=2, column=2)

#Divisão
def div():
    v1 = entrada1.get()
    v2 = entrada2.get()
    resultado["text"] = int(v1) / int(v2)

bdiv = Button(janela, text=' / ', bg='gray', command = div, width=10)
bdiv.grid(row=3, column=0)

#Porcentagem
def bpc():
    v1 = entrada1.get()
    v2 = entrada2.get()
    resultado["text"] = (int(v1)/100) * int(v2)

bpc = Button(janela, text=' % ', bg='gray', command = bpc, width=10)
bpc.grid(row=3, column=2)

#Clear
def clear():
    entrada1.delete('0', 'end')
    entrada2.delete('0', 'end')

bclear = Button(janela, text='CLEAR', bg='gray', command = clear, width=10)
bclear.grid(row=3, column=1)

#Resultado
resultado = Label(janela, text='')
resultado.grid(row=5, column=1)

janela.mainloop()

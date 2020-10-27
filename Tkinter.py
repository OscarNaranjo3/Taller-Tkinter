import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculadora(n1,n2,operador,redondear):
    if operador=='+': R=n1+n2
    elif operador=='-': R=n1-n2
    elif operador == '*': R=n1*n2
    elif operador == '/': R = n1/n2
    else: R=n1**n2
    if redondear==True:
        R = round(R,2)
    return R
def click_calcular(n1,n2,operador,redondear):
    try:
        if n1=='' or n2=='':
            messagebox.askretrycancel('Campos vacios', 'Por favor llene los campos')
        else:
            v1 = float(n1)
            v2 = float(n2)
            res = calculadora(v1, v2, operador, redondear)
            messagebox.showinfo('Resultado', res)
    except ValueError:
        messagebox.askretrycancel('Entrada invalida', 'Por favor ingrese una entrada valida')

def init_window():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x200')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    label_entrada1 = tk.Label(window, text='Ingrese primer numero', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero', font=('Arial bold', 10))
    label_entrada2.grid(column=0,row=2)

    entrada1 = tk.Entry(window, width=10)
    entrada1.grid(column=1, row=1)

    entrada2 = tk.Entry(window, width=10)
    entrada2.grid(column=1, row=2)

    label_operador = tk.Label(window, text='Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column=0, row=3)

    combo_operadores= ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    redondear = tk.BooleanVar()
    redondear.set(False)
    chk_redondear = tk.Checkbutton(window, text='Redondear 2 decimales', var=redondear)
    chk_redondear.grid(column=1, row=4)

    boton = tk.Button(window,
                    command = lambda: click_calcular(
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get(),redondear.get()),
                      text='Calcular',
                      bg="Blue",
                      fg="white")
    boton.grid(column=8,row=1)

    window.mainloop()

def main():
    init_window()
main()

#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
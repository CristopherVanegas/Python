from tkinter import *

ventana = Tk()
ventana.title("Caulculadora de ------")

i = 0
entradaTexto = Entry(ventana, font=("Calibri 15"))
entradaTexto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Funciones


def clickBoton(valor):
    global i
    entradaTexto.insert(i, valor)
    i += 1


def borrar():
    entradaTexto.delete(0, END)
    i = 0


def operacion():
    ecuacion = entradaTexto.get()
    resultado = eval(ecuacion)
    entradaTexto.delete(0, END)
    entradaTexto.insert(0, resultado)
    i = 0
# botones


# Botones de números
boton1 = Button(ventana, text="1", width=5, height=2,
                command=lambda: clickBoton(1))
boton2 = Button(ventana, text="2", width=5, height=2,
                command=lambda: clickBoton(2))
boton3 = Button(ventana, text="3", width=5, height=2,
                command=lambda: clickBoton(3))
boton4 = Button(ventana, text="4", width=5, height=2,
                command=lambda: clickBoton(4))
boton5 = Button(ventana, text="5", width=5, height=2,
                command=lambda: clickBoton(5))
boton6 = Button(ventana, text="6", width=5, height=2,
                command=lambda: clickBoton(6))
boton7 = Button(ventana, text="7", width=5, height=2,
                command=lambda: clickBoton(7))
boton8 = Button(ventana, text="8", width=5, height=2,
                command=lambda: clickBoton(8))
boton9 = Button(ventana, text="9", width=5, height=2,
                command=lambda: clickBoton(9))
boton0 = Button(ventana, text="0", width=13, height=2,
                command=lambda: clickBoton(0))

# Botones de opciones
botonBorrar = Button(ventana, text="xD", width=5,
                     height=2, command=lambda: borrar())
botonParentesis = Button(ventana, text="(", width=5,
                         height=2, command=lambda: clickBoton("("))
botonParentesis2 = Button(ventana, text=")", width=5,
                          height=2, command=lambda: clickBoton(")"))
botonPunto = Button(ventana, text=".", width=5, height=2,
                    command=lambda: clickBoton("."))

# Botones de operaciones matematicas
botonSuma = Button(ventana, text="+", width=5, height=2,
                   command=lambda: clickBoton("+"))
botonResta = Button(ventana, text="-", width=5, height=2,
                    command=lambda: clickBoton("-"))
botonDivisión = Button(ventana, text="/", width=5,
                       height=2, command=lambda: clickBoton("/"))
botonMultiplicación = Button(
    ventana, text="x", width=5, height=2, command=lambda: clickBoton("*"))
botonIgual = Button(ventana, text="=", width=5, height=2,
                    command=lambda: operacion())

# Interfaz de los botones en la pantalla
botonBorrar.grid(row=1, column=0, padx=5, pady=5)
botonParentesis.grid(row=1, column=1, padx=5, pady=5)
botonParentesis2.grid(row=1, column=2, padx=5, pady=5)
botonDivisión.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
botonMultiplicación.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
botonResta.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
botonSuma.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
botonPunto.grid(row=5, column=2, padx=5, pady=5)
botonIgual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()

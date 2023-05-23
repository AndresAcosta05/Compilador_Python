import tkinter as tk
from tkinter import messagebox
from compilador import Compilador

class Ventana(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Ventada Compilador')
        # configuracion del tamaño de columnas
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        # creando el espacio de texto
        self.input_text = tk.Text(self, wrap=tk.WORD)
        self.crear_componentes()
    
    def crear_componentes(self):
        # creacion del espacio
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        # creacion de los botones
        boton_compilar = tk.Button(frame_botones, text='Compilar', command=self.compilar)
        boton_limpiar = tk.Button(frame_botones, text='Limipar', command=self.limpiar)
        # estilo y ubicacion a los botones
        boton_compilar.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_limpiar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        # agregando el frame de los botones
        frame_botones.grid(row=0, column=0, sticky='ns')
        self.input_text.grid(row=0, column=1, sticky='nswe')
    
    def compilar(self):
        contenido = self.input_text.get(1.0, tk.END)
        # devuelve un arreglo con las lineas y su contenido
        lexico = Compilador.fase_lexica(contenido)        
        if lexico:
            Compilador.fase_sintactica(lexico)

    def limpiar(self):
        self.input_text.delete("1.0", "end")

if __name__ == '__main__':
    ventana = Ventana()
    ventana.mainloop()
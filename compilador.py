import re
from tkinter import messagebox

class Compilador:

    _comandos = {
        'Captura.Texto()' : 'Capturador de Texto',
        'Captura.Entero()': 'Capturador de Entero',
        'Captura.Real()' : 'Capturador de Real',
        'Mensaje.Texto()': 'Capturador de Mensaje' 
    }
    _tipos_dato = {
        'Entero' : 'Identificador de Entero',
        'Real' : 'Identificador de Real',
        'Texto' : 'Identificador de Texto'
    }
    _simbolos_admitidos = {
        ',' : 'Coma',
        '.' : 'Punto',
        ';' : 'Punto y Coma',
        '(' : 'Parentesis Izquierdo',
        ')' : 'Parentesis derecho',
        '=' : 'Asignacion',
        '+' : 'Adicion',
        '-' : 'Resta',
        '*' : 'Multiplicacion',
        '/' : 'Division',
        '"' : 'Comilla doble',
        '\'' : 'Comilla Sencilla',
        '”' : 'Comilla doble derecha',
        '“' : 'Comilla doble izquierda'

    }
    # creamos las variables que se usaran en el compilador
    valores_tipo_datos = _tipos_dato.keys()
    valores_simbolos_admitidos = _simbolos_admitidos.keys()
    valores_comandos = _comandos.keys()

    @classmethod
    def fase_lexica(self, contenido_archivo):
        """
        Dentro de esta funcion se recibe todo el contenido del archivo a leer y se aplicara las respectivas divisiones
        para saber cada uno de sus componentes
        """
        count = 0
        lines = contenido_archivo.split('\n')
        contenido = []
        for line in lines:
            count += 1
            if not line:
                continue
            # imprimimos la linea actual
            print(f'Linea {count}')
            # separamos cada uno de los tokens
            tokens = re.split(r'([\W+,;])', line)
            for token in tokens:
                if token != '' and token != ' ':
                    if token in self.valores_tipo_datos:
                        print(f'Token: {token}, Funcion: {self._tipos_dato[token]}')

                    elif token in self.valores_simbolos_admitidos:
                        print(f'Token: {token}, Funcion: {self._simbolos_admitidos[token]}')
                    
                    elif token in self.valores_comandos:
                        print(f'Token: {token}, Funcion: {self._comandos[token]}')
                    
                    elif re.match(r'[a-zA-Z0-9]+', token):
                        print(f'Token: {token}, Funcion: Espacio de asignacion o valor')
                
                    else:
                        print(f'Token: {token}', 'Error: Token Desconocido')
                        messagebox.showerror('Error en fase lexica', 'Token desconocido en la linea '+ str(count))
                        contenido = None
                        return contenido
                        
            contenido.append({
                'Linea': count,
                'texto': line
            })
        return contenido

    @classmethod
    def fase_sintactica(self, contenido_archivo):
        for linea in contenido_archivo:
            # convertimos la linea a una cadena de texto para usar los metodos de la clase str
            nueva = str(linea['texto'])
            # validamos que la linea finalice en ;
            if not nueva.endswith(';'):
                messagebox.showerror('Error al compilar', 'No hay finalizacion de comando. Linea ' + str(linea['Linea']))
                return
            
            # validamos si esta intentando dar un mensaje
            elif re.match(r'Mensaje\.Texto\("[\w*\s*\w*]*"\);', nueva):
                division = nueva.split('"')
                messagebox.showinfo('Mensaje Usuario', division[1])
                continue

            # validamos si esta intentando crear una variable
            elif re.search(r'Entero|Real|Texto', nueva):
                if re.match(r'[a-zA-Z]\w* (Entero|Real|Texto);', nueva):
                    continue
                else:
                    messagebox.showerror('Error de creacion en Linea ' + str(linea['Linea']), 'Esta intentando crear una variable de la forma incorrecta. \n Pruebe: Nombre_Var Tipo;')
                    break
            
            # no se reconocio el comando
            else: 
                messagebox.showerror('Error en la Linea ' + str(linea['Linea']), 'Comando o expresion invalida')
                break
            
            

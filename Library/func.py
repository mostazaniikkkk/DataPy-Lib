import inspect, re

class Function:
    def __init__(self, name):
        self.functionList = []
        self.name = name.replace(" ", "_")

    def AddFunction(self, type, value, player = ""): 
        self.functionList.append(f"{type} {player} {value}")
        return self

def McFunction(nombre):
    def decorador(funcion):
        func = Function(nombre)
        content = inspect.getsource(funcion)

        #Agrega contenido a la lista de funciones
        def Set(values, type, player = ""): 
            for value in values: 
                # Elimina las comillas de los extremos y los espacios en blanco alrededor del valor
                value = value.strip().strip('\'"')
                func.AddFunction(type, value, player)

        def SearchFunc(sentence): return re.findall(rf"{sentence}\((.*?)\)", content)
        # Usa una expresión regular no codiciosa para capturar cada sentencia print individualmente
        Set(SearchFunc("print"),"tellraw", "@e") #Convierte los print en tellraw

        return func
    return decorador
from DataPyLib.datapackManager import DatapackManager
from DataPyLib.func import Function

pack = DatapackManager("Hello World", "icon", 9, "Hola mundo :D")

@McFunction("Hello World")
def HelloWorld(): print("Hola mundo")

pack.AddFunction(HelloWorld)

pack.Make() 
from DataPyLib.datapackManager import DatapackManager
from DataPyLib.func import Function

pack = DatapackManager("Hello World", "icon", 9, "Hola mundo :D")

helloWorld = Function("Hello World")\
    .addFunction("rawtell", "Diamantito", "@p")\
    .addFunction("give", "minecraft:diamond_sword", "@p")

pack.AddFunction(helloWorld)

pack.Make()
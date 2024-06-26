from DataPyLib.datapackManager import DatapackManager
from DataPyLib.func import Function

pack = DatapackManager("Hello World", "wavy", 9, "Hola mundo :D")

helloWorld = Function("Hello World")\
    .addFunction("rawtell", "Diamantito", "@p")\
    .addFunction("give", "minecraft:diamond_sword", "@p")

pack.func.append(helloWorld)

pack.Make()
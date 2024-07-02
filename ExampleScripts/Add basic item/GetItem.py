from DataPyLib.datapackManager import DatapackManager
from DataPyLib.items import Item

pack = DatapackManager("Dive Ball", "icon", 9, "Hola mundo :D")

item = Item("Dive Ball")\
        .SetTexture("textures/dive_ball")

pack.AddItem(item)

pack.Make()
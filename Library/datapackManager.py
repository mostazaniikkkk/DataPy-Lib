import json, io, zipfile
from . import func

class DatapackManager:
    meta = None
    name = None
    icon = None
    loadMsg = None
    rpVer = None

    items = []
    func = []
    listenedFunc = []
    recipe = []
    blocks = []

    def __init__(self, name, icon = "icon", mineVer = 10, rpVer = 15, desc = ""):
        self.meta = {
            "pack": {
                "pack_format": mineVer,
                "description": desc
            }
        }
        self.name = name
        self.icon = icon
        self.rpVer = rpVer
    
    def AddLoadMsg(self, msg = f"Datapack {name}: Loaded."):
        if isinstance(msg, str): self.loadMsg = f"tellraw as @a {msg}"
        elif isinstance(msg, func.Function): self.loadMsg = "\n".join(msg.functionList)
        else: print("Error: Tipo de dato no admitido, por favor configurar load.mcfuncion manualmente")

    def JsonDef(self, value):
        strData = {
            "values": [f"{self.name}:{value}"]
        }
        return io.StringIO(json.dumps(strData)).getvalue()

    def Make(self):
        print("Baking Datapack...")
        with zipfile.ZipFile(f'{self.name}.zip', 'w') as datapack_zip:
            #Carga basica
            pack_mcmeta = io.StringIO(json.dumps(self.meta)) # Crear el archivo pack.mcmeta en memoria
            datapack_zip.writestr('pack.mcmeta', pack_mcmeta.getvalue()) # Añadir pack.mcmeta al archivo ZIP

            try: datapack_zip.write(f'{self.icon}.png', arcname='icon.png') #Carga el icono al zip
            except: print("Icono no encontrado, recuerda cargar el icono manualmente en tu archivo ZIP")

            datapack_zip.writestr('data/minecraft/tags/functions/load.json', self.JsonDef("load"))
            datapack_zip.writestr('data/minecraft/tags/functions/tick.json', self.JsonDef("tick"))

            #Funciones
            for sentence in self.func:
                if sentence.functionList:  # Comprueba si functionList no está vacío
                    function_mcmeta = io.StringIO("\n".join(sentence.functionList))
                    datapack_zip.writestr(f"data/{self.name}/functions/{sentence.name}.mcfunction", function_mcmeta.getvalue())

        print("Datapack has been successfully compiled.")

    #Funciones constructores
    def SetIcon(self, name):
        self.icon = name
        return self
    
    def AddFunction(self, func):
        self.func.append(func)
        return self
    
    def AddListener(self, func):
        self.listenedFunc.append(func)
        return self

    def AddItem(self, item):
        self.items.append(item)
        return self
    
    def AddBlock(self, item):
        self.blocks.append(item)
        return self
    
    def AddRecipe(self, item):
        self.recipe.append(item)
        return self
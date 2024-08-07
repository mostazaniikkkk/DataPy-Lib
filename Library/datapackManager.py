import json, io, zipfile, random, os
from .rspackManager import ResourcePackManager

class DatapackManager:
    def __init__(self, name, icon = "icon", mineVer = 10, rpVer = 15, desc = ""):
        self.format = mineVer
        self.desc = desc

        self.meta = None
        self.cmdId = None

        self.loadFunc = []
        self.items = []
        self.func = []
        self.listenedFunc = []
        self.recipe = []
        self.blocks = []
        self.lootTable = []
        self.advancement = []

        self.UpdateMeta()

        self.name = name.replace(" ", "_")
        self.icon = icon
        self.rpVer = rpVer
    
    def UpdateMeta(self):
        self.meta = {
            "pack": {
                "pack_format": self.format,
                "description": self.desc
            }
        }

    def Make(self):
        print("Baking Datapack...")

        if self.cmdId is None: self.cmdId = random.randint(1, 99999)
        for i, item in enumerate(self.items, start=1):
            item.cmdId = self.cmdId + i

        os.makedirs("cache")

        #ZIP Manager
        with zipfile.ZipFile(f'{self.name}.zip', 'w') as datapack_zip:
            #SubFunciones
            def GetFile(string): return io.StringIO(string).getvalue()
            def ZipFile(stringFile, route):
                try: datapack_zip.writestr(f"data/{self.name}/{route}/", GetFile(stringFile))
                except: print(f"Error: Hubo un problema al comprimir el archivo {route}, por favor compruebe el codigo, en caso de que sea un fallo de la libreria reportelo en el repositorio oficial :()")
            def JsonDef(self, type, value):
                strData = {
                    "values": [f"{self.name}:{type}/{value}"]
                }
                return io.StringIO(json.dumps(strData)).getvalue()

            #Carga basica
            datapack_zip.writestr('pack.mcmeta', GetFile(json.dumps(self.meta))) # Añadir pack.mcmeta al archivo ZIP

            try: datapack_zip.write(f'{self.icon}.png', arcname='icon.png') #Carga el icono al zip
            except: print("Icon not found, remember to manually load the icon into your ZIP file.")

            #Items
            for item in self.items:
                #Genera un give a modo de Debug
                ZipFile(f"function/give/{item.name}.mcfunction", f"give @p {item.item}")

                #Receta T-T
                if item.recipe is not None:
                    recipe = item.recipe\
                        .SetLoot(item.item)\
                        .SetAdvancement(self.name)\
                        .CreateFuncRecipe(self.name)
                    
                    #Compresion al ZIP de la receta, funcion de carga, loot tables y avances respectivamente
                    ZipFile(f"recipes/{recipe.name}.json", json.dumps(recipe.CreateRecipe()))
                    ZipFile(f"function/craft/{item.name}.mcfunction", "\n".join(item.recipe.function.functionList))
                    ZipFile(f"loot_tables/craft/{item.name}.json", json.dumps(item.recipe.loot.GetLoot()))
                    ZipFile(f"advancement/craft/{item.name}.json", json.dumps(item.recipe.advancement.GetAdvancement()))

            #Agrega recetas, loot tables, funciones y avances declarados en la clase datapack manager
            for recipe in self.recipe: ZipFile(f"recipes/{recipe.name}.json", json.dumps(recipe.CreateRecipe()))
            for loot in self.lootTable: ZipFile(f"loot_tables/{loot.name},json", json.dumps(loot.GetLoot()))
            for sentence in self.func: ZipFile(f"functions/{sentence.name}.mcfunction", "\n".join(sentence.functionList))
            for adv in self.advancement: ZipFile(f"advancements/{adv.name}", json.dumps(adv.GetAdvancement(self)))

        #Datapack Manager
        if self.items: ResourcePackManager(self.name, self.items, self.cmdId, self.icon).Make()

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
    
    def UpdateDesc(self, desc):
        self.desc = desc
        self.UpdateMeta()
        return self
    
    def UpdateFormat(self, format):
        self.format = format
        self.UpdateMeta()
        return self
    
    def SetCustomModelData(self, cmdId):
        self.cmdId = cmdId
        return self
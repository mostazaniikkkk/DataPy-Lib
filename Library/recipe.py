from .func import Function
from .Loot import lootTable, lootFunction, entrie

class Recipe:
    def __init__(self, name, result, count = 1):
        self.name = name
        self.keys = {}
        self.pattern = []
        self.count = count

        self.result = result if "minecraft:" in result else "minecraft:knowledge_book"

    def CreateRecipe(self):
        recipe = {
            "type":  "minecraft:crafting_shaped",
            "pattern": self.pattern,
            "key": self.keys,
            "result": {
                "item": self.result,
                "count": self.count
                }
            } 
        return recipe

    #Importante: Estas 2 funciones esta diseñada para el Datapack Manager
    #Solo se ejecuta en caso de custom item, por favor no llamar :)
    def CreateLoot(self, itemTag):
        entry = entrie.Entry(self.name)\
            .SetLootFunction(lootFunction.SetNbt(itemTag).value)

        loot = lootTable.LootTable(f"{self.name}_loot", 1)\
            .SetEntries(entry)
        return loot
    
    def CreateFuncRecipe(self, datapackName):
        func = Function(f"{self.name}_recipe")
        func.addFunction("clear", f"knowledge_book 1", "@s")
        func.addFunction("loot give", f"{datapackName}:")

    # Constructores
    def SetKeys(self, keys):
        for letter, item in keys.items():
            self.keys[letter] = {"item": item}
        return self

    def SetPatternRow(self, key_pattern):
        self.pattern.append(key_pattern)
        return self
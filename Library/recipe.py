from .func import Function
from .Loot import lootTable, lootFunction, entrie
from Advancement.Criteria import criteria, unlockRecipe
from Advancement import reward, advancement

class Recipe:
    def __init__(self, name, result = "", count = 1):
        self.name = name
        self.keys = {}
        self.pattern = []
        self.count = count

        #Custom Loot
        self.loot = None
        self.advancement = None
        self.function = None

        self.result = f"minecraft:{result}" if result != "" else "minecraft:knowledge_book"

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


    #Solo llamar en caso de que el resultado sea un item custom, idealmente no llamar manualmente :D
    def SetLoot(self, itemTag):
        entry = entrie.Entry(self.name)\
            .SetLootFunction(lootFunction.SetNbt(itemTag).value)

        loot = lootTable.LootTable(f"{self.name}_loot", 1)\
            .SetEntries(entry)
        
        self.loot = loot
        return self
    
    def SetAdvancement(self, datapackName):
        rew = reward.Reward()\
            .SetFunction(f"{datapackName}:{self.name}")
        
        unlock = unlockRecipe.UnlockRecipe(self.name)\
            .SetRecipe(datapackName, self.name)

        crit = criteria.Criteria()\
            .SetRequeriment(unlock.SetRecipe())
        
        advance = advancement.Advancement()\
            .SetReward(rew)\
            .SetCriteria(crit)\
            .SetName(self.name)
        
        self.advancement = advance
        return self
      
    def CreateFuncRecipe(self, datapackName):
        func = Function(f"{self.name}_recipe")
        
        func.AddFunction("clear", f"knowledge_book 1", "@s")
        func.AddFunction("loot give", f"loot {datapackName}:crafts/{self.loot.name}_loot", "@s")
        func.AddFunction("advancement revoke", f"{datapackName}:crafts/{self.advancement.name}", "@s")
        func.AddFunction("recipe take", f"{datapackName}:{self.name}", "@s")
        
        self.function = func
        return self

    # Constructores
    def SetKeys(self, keys):
        for letter, item in keys.items():
            self.keys[letter] = {"item": item}
        return self

    def SetPatternRow(self, key_pattern):
        self.pattern.append(key_pattern)
        return self
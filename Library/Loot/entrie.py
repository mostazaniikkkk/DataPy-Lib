class Entry:
    def __init__(self, name, type, loot = ""):
        self.name = name
        self.type = type
        self.loot = loot
        self.functions = []
            
    def GetEnty(self):
        match type:
            case "empty": entry = {"type": "minecraft:empty"}
            case "loot":
                entry = {
                    "type": "minecraft:loot_table",
                    "name": f"minecraft:{self.loot.name}"
                }
            case "item":
                entry = {
                    "type": "minecraft:item",
                    "name": f"minecraft:{self.loot}"
                }

        if entry != {"type": "minecraft:empty"} and function is not None:
            entry["function"] = self.functions
        
        return entry

    def SetLootFunction(self, function):
        self.functions.append(function.value)
        return self
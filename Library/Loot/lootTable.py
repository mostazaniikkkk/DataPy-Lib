import json

class LootTable:
    def __init__(self, name, rolls):
        self.name = name
        self.rolls = rolls
        self.entries = []

    def GetLoot(self):
        loot = {
            "pools": [
                {
                    "rolls": self.rolls,
                    "entries": [",".join(self.entries)]
                }
            ]
        }

        return loot
    
    def SetEntries(self, entry):
        self.entries.append(json.dumps(entry.GetEntry()))
        return self
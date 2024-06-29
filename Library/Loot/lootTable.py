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
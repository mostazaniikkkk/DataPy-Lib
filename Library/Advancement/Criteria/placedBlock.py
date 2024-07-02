class PlacedBlock():
    def __init__(self, block, name = "requirement"):
        self.name = name
        self.block = block
        self.properties = {}

    def GetRequeriment(self):
        requeriment = {
            "trigger": "minecraft:placed_block",
            "conditions": {
                "location": [
                {
                    "condition": "minecraft:block_state_property",
                    "block": f"minecraft:{self.block}",
                    "properties": self.properties
                }
                ]
            }
        }

        return requeriment
    
    def SetPropertie(self, propertie, value):
        self.properties[propertie] = value
        return self
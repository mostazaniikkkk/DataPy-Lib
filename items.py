import json

class Item:
    item = None
    itemDisplay = None
    cmdId = None
    itemBase = None
    texture = None

    enchantment = []

    def __init__(self, name, cmdId, itemBase = "stick", italic = False, color = "white", texture = None, model = None):
        self.itemDisplay = {
            "text": name.replace(" ", "_"),
            "italic": italic,
            "color": color
        }

        self.cmdId = cmdId
        self.itemBase = itemBase
        self.texture = texture

        self.UpdateItem()
    
    def UpdateItem(self):
        self.item = f"{self.itemBase}{{display: Name '{json.dumps(self.itemDisplay)}',
            {f'Enchantments: {", ".join(self.enchantment)}' if self.enchantment else ''},
            CustomModelData: {self.cmdId}}}"
        
    def SetEnchantment(self, enchantment):
        self.enchantment.append(enchantment)
        self.UpdateItem()
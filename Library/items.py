import json

class Item:
    item = None
    itemDisplay = None
    cmdId = None
    itemBase = None
    texture = None

    enchantment = []
    leftClick = None
    rightClick = None

    def __init__(self, name, itemBase = "stick", texture = None, italic = False, color = "white"):
        self.itemDisplay = {
            "text": name.replace(" ", "_"),
            "italic": italic,
            "color": color
        }

        self.itemBase = itemBase
        self.texture = texture

        self.UpdateItem()

    #Funciones constructores
    def UpdateItem(self):
        self.item = f"{self.itemBase}{{display: Name '{json.dumps(self.itemDisplay)}',
            {f'Enchantments: {", ".join(self.enchantment)}' if self.enchantment else ''},
            CustomModelData: {self.cmdId}}}"
        return self
    
    def SetItemBase(self, name):
        self.itemBase = name
        return self
    
    def SetTexture(self, texture):
        self.texture = texture
        return self
    
    def SetEnchantment(self, enchantment):
        self.enchantment.append(enchantment)
        self.UpdateItem()
        return self
    
    def SeRightAction(self, function):
        self.rightClick = function
        return self
    
    def SetLeftAction(self, function):
        self.leftClick = function
        return self
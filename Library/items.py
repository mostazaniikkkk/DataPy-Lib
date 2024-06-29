import json

class Item:
    item = None
    itemDisplay = None
    cmdId = None
    itemBase = None
    texture = None

    name = None
    italic = None
    color = None

    enchantment = []
    leftClick = None
    rightClick = None
    lootItem = None

    def __init__(self, name, itemBase = "stick", texture = None, italic = False, color = "white"):
        self.name = name
        self.italic = italic
        self.color = color
        self.UpdateDisplay()

        self.itemBase = itemBase
        self.texture = texture

        self.UpdateItem()
    
    #Funciones constructores
    def UpdateItem(self):
        self.item = f"{self.itemBase}{{{{display: Name '{json.dumps(self.itemDisplay)}',\
                    {f'Enchantments: {', '.join(self.enchantment)}' if self.enchantment else ''},\
                    CustomModelData: {self.cmdId}}}}}"
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
    
    def UpdateDisplay(self):
        self.itemDisplay = {
            "text": self.name.replace(" ", "_"),
            "italic": self.italic,
            "color": self.color
        }
        return self
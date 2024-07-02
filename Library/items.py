import json

class Item:
    def __init__(self, name, itemBase = "stick", texture = None, italic = False, color = "white"):
        self.name = name
        self.italic = italic
        self.color = color
        self.UpdateDisplay()

        self.item = None
        self.itemDisplay = None
        self.cmdId = None

        self.enchantment = []
        self.function = None
        self.recipe = None

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
    
    def SetFunction(self, function):
        self.function = function
        return self

    def UpdateDisplay(self):
        self.itemDisplay = {
            "text": self.name.replace(" ", "_"),
            "italic": self.italic,
            "color": self.color
        }
        return self
    
    def SetRecipe(self, recipe):
        self.recipe = recipe
        return self
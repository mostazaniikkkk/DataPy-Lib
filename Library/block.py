from items import Item
from Advancement import reward
from Advancement.Criteria import criteria, placedBlock

class Block(Item):
    def __init__(self, name, texture, model = None, italic = False, color = "white"):
        super().__init__(name, "barrier", texture, italic, color)
class SetCount:
    def __init__(self, count):
        self.value = {
            "function": "minecraft:set_count",
            "count": count
        }

class RandomEnchant:
    def __init__(self): self.value = { "function": "minecraft:enchant_randomly" }

class SetNbt:
    def __init__(self, tag):
        self.value = {
            "function": "minecraft:set_nbt",
            "tag": tag
        }
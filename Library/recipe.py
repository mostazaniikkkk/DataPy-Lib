from .func import Function

class Recipe:
    def __init__(self, name, result, count = 1):
        self.name = name
        self.keys = {}
        self.pattern = []
        self.count = count

        self.result = result if "minecraft:" in result else "minecraft:knowledge_book"

    def Create_recipe(self):
        recipe = {
            "type":  "minecraft:crafting_shaped",
            "pattern": self.pattern,
            "key": self.keys,
            "result": {
                "item": self.result,
                "count": self.count
                }
        }
        return recipe

    # Constructores
    def Set_keys(self, keys):
        for letter, item in keys.items():
            self.keys[letter] = {"item": item}
        return self

    def Set_pattern_row(self, key_pattern):
        self.pattern.append(key_pattern)
        return self

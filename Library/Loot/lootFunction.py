class SetCount:
    def __init__(self, count):
        self.value = { "function": "minecraft:set_count" }

        if isinstance(count, int): self.value["count"] = count
        elif isinstance(count, list): self.value["count"] = {
            "min": count[0],
            "max": count[1],
            "type": "minecraft:uniform"
        }
        else: print(f"Error: The value {count} is not valid, so the default value 1 will be added."); self.value["count"] = 1

class RandomEnchant:
    def __init__(self): self.value = { "function": "minecraft:enchant_randomly" }

class SetNbt:
    def __init__(self, tag):
        self.value = {
            "function": "minecraft:set_nbt",
            "tag": tag
        }
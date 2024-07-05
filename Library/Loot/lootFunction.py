class SetCount:
    def __init__(self, count):
        errVal = { "CountExcep": [] }
        self.value = { "function": "minecraft:set_count" }

        if type(count) == int: self.value["count"] = count
        elif isinstance(count, list): self.value["count"] = {
            "min": count[0] if type(count[0]) == int else 1,
            "max": count[1] if type(count[1]) == int else count[0],
            "type": "minecraft:uniform"
        }
        else:
            try: raise ValueError("DataPy Lib Error: Non-numeric data cannot be entered as quantity, the default value of 1 will be entered instead.")
            except Exception as e:
                self.value["count"] = 1
                log = {
                    "name": "Non-numeric Exception",
                    "desc": f"The entered value {count} is not valid.",
                    "traceback": e
                }

                errVal["CountExcep"].append(log)

class RandomEnchant:
    def __init__(self): self.value = { "function": "minecraft:enchant_randomly" }

class SetNbt:
    def __init__(self, tag):
        self.value = {
            "function": "minecraft:set_nbt",
            "tag": tag if type(tag) == str else ""
        }
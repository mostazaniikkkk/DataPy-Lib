class UnlockRecipe:
    def __init__(self, name = "requirement"):
        self.name = name
        self.recipe = None

    def GetRequirement(self):
        requirement = {
            self.name: {
                "trigger": "minecraft:recipe_unlocked",
                "conditions": { "recipe": self.recipe }
            }
        }
        return requirement
    
    def SetRecipe(self, recipe, datapackName):
        self.recipe = f"{datapackName}:{recipe}"
        return self
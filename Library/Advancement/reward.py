class Reward:
    def __init__(self, experience = None):
        self.experience = experience
        self.loot = []
        self.function = None
    
    def GetReward(self):
        reward = {}
        if self.experience is None: reward["experience"] = self.experience
        if self.loot: reward["loot"] = [",".join(self.loot)]
        if self.function is None: reward["function"] = self.function

        return reward

    #Constructor
    def SetLoot(self, loot):
        self.loot.append(loot.GetLoot())
        return self
    
    def SetFunction(self, function):
        self.function = function
        return self
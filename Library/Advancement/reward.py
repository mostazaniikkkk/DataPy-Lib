class Reward:
    def __init__(self, experience = 0):
        self.experience = experience
        self.loot = []
    
    def GetReward(self):
        reward = {
            "experience": self.experience,
            "loot": [",".join(self.loot)]
        }

        return reward

    #Constructor
    def SetLoot(self, loot):
        self.loot.append(loot.GetLoot())
        return self
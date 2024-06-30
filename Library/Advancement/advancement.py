import json

class Advancement:
    def __init__(self):
        self.display = None
        self.criteria = None
        self.reward = None
        self.parent = None

    def GetAdvancement(self):
        advancement = {}

        if self.display is not None: advancement["display"] = self.display
        if self.parent is not None: advancement["parent"] = self.parent
        if self.criteria is not None: advancement["criteria"] = self.criteria
        if self.reward is not None: advancement["reward"] = self.reward

        return advancement
    
    #Constructores
    def SetParent(self, parent):
        self.parent = f"minecraft:{parent}"
        return self
    
    def SetDisplay(self, display):
        self.display = json.dumps(display.GetDisplay())
        return self
    
    def SetCriteria(self, criteria):
        self.criteria = json.dumps(criteria.GetCriteria())
        return self
    
    def SetReward(self, reward):
        self.reward = json.dumps(reward.GetReward())
        return self
import json

class Criteria:
    def __init__(self):
        self.requeriments = []

    def GetCriteria(self):
        criteria = {
            "criteria": {",".join(self.requeriments)}
        }
        return criteria
    
    def SetRequeriment(self, requeriment):
        self.requeriments.append(json.dumps(requeriment.GetRequeriment()))
        return self
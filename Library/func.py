class Function:
    functionList = []
    name = None

    def __init__(self, name):
        self.name = name.replace(" ", "_")

    def AddFunction(self, type, value, player = ""): 
        self.functionList.append(f"{type} {player} {value}")
        return self

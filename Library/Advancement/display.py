import json

class Display:
    def __init__(self):
        self.name = None
        self.colorName = None

        self.desc = None
        self.colorDesc = None

        self.icon = None
        self.background = None
        self.frame = None
        self.toast = False
        self.chat = False
        self.hidden = False

        self.rpName = None

    def GetDisplay(self):
        display = {
            "title": {
                "text": self.name,
                "color": self.colorName
            },
            "description": {
                "text": self.desc,
                "color": self.colorDesc
            },
            "icon": json.dumps(self.icon),
            "background": self.background,
            "frame": self.frame,
            "show_toast": self.toast,
            "announce_to_chat": self.chat,
            "hidden": self.hidden
        }
        
        return display

    #Constructores
    def SetName(self, name, color = "white"):
        self.name = name
        self.colorName = color
        return self
    
    def SetDesc(self, desc, color = "white"):
        self.desc = desc
        self.colorDesc = color
        return self
    
    def SetIcon(self, item, cmd):
        icon = { "item": item }
        if cmd: icon["nbt"] = cmd
        self.icon = icon
        return self
    
    def SetFrame(self, frame):
        self.frame = frame
        return self
    
    def SetBackground(self, texture, mc = True, path = ""):
        self.background = f"{"minecraft" if mc is True else self.rpName}:\
            {"textures/block/" if mc is True else path}\
            {texture}.png"
        return self
import zipfile, io, json
from .items import Item

class ResourcePackManager:
    name = None
    item = None
    meta = None

    def __init__(self, name, items, desc, ver = 15):
        self.name = name
        self.item = items
        self.meta = {
            "pack": {
                "pack_format": ver,
                "description": desc
            }
        }

    def Make(self):
        print("Backing Resource Pack...")
        with zipfile.ZipFile(f'{self.name}.resource.zip', 'w') as rspack_zip:
            pack_mcmeta = io.StringIO(json.dumps(self.meta))
            rspack_zip.writestr('pack.mcmeta', pack_mcmeta.getvalue())

            try: rspack_zip.write(f'{self.icon}.png', arcname='icon.png')
            except: print("Icono no encontrado, recuerda cargar el icono manualmente en tu archivo ZIP")

            for item in self.item():
                if item.texture: rspack_zip.write(f"asset/minecraft/textures/item{item.texture}.png")
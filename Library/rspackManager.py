import zipfile, io, json, os, shutil
from .items import Item

class ResourcePackManager:
    name = None
    item = None
    meta = None
    icon = None

    def __init__(self, name, items, desc, icon, ver = 15):
        self.name = name
        self.item = items
        self.icon = icon
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
            except: print("Icon not found, remember to manually load the icon into your ZIP file.")

            

            for i, item in enumerate(self.item, start=1):
                if item.texture:
                    rspack_zip.write(f"{item.texture}.png", f"assets/minecraft/textures/item/{item.texture}.png")

                    customData = {
                        "parent": "minecraft:item/generated",
                        "textures": {
                        "layer0": f"minecraft:tutorial/{item.name}"
                        }
                    }

                    # Crea eL Custom Model Data de los Items
                    new_cmd = {"predicate": {"custom_model_data": item.cmdId + i}, "model": f"{self.name}/{item.name}.json"}

                    custom_json = io.StringIO(json.dumps(customData))
                    rspack_zip.writestr(f"assets/minecraft/models/{self.name}/{item.name}.json", custom_json.getvalue())

                    if os.path.exists(f"cache/baseItems/{item.itemBase}.json"):
                        # Abre el archivo en modo de lectura
                        with open(f"cache/baseItems/{item.itemBase}.json", 'r') as file:
                            data = json.load(file)

                            data['overrides'].append(new_cmd)

                        # Abre el archivo en modo de escritura y escribe el contenido modificado
                        with open(f"cache/baseItems/{item.itemBase}.json", 'w') as file:
                            json.dump(data, file, indent=4)
                    else:
                        jsonData = {
                            "parent": "minecraft:item/generated",
                            "textures": {
                                "layer0": f"minecraft:item/{item.itemBase}"
                            },
	                        "overrides": []
                        }

                        jsonData["overrides"].append(new_cmd)
                        # Crear un archivo de texto desde cero
                        os.makedirs("cache/baseItems")
                        with open(f"cache/baseItems/{item.itemBase}.json", 'w') as file:
                            file.write(json.dumps(jsonData))
            
            # Carga los items originales al ZIP
            for file in os.listdir("cache/baseItems"):
                file_route = os.path.join("cache/baseItems", file)

                if os.path.isfile(file_route):
                    rspack_zip.write(file_route, arcname=f'assets/minecraft/models/item/{file}') # Añade el archivo al ZIP en una sección específica

            shutil.rmtree("cache")
            print("Resource pack has baked succesfully :D")
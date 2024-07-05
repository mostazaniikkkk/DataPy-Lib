import sys
from unitTest import Test
sys.path.append('D:/Programas/DPManager/DataPyLib') #Ingresa en el string la direccion de la libreria
from Library.Loot.lootFunction import SetCount, SetNbt #No se ingreso "SetEnchant porque es un dato simple"
from rich.console import Console

test = Test()
test.showResult = True

console = Console()

console.print("[cyan]LootFunction Tests:[/cyan]")
test.JsonTest(SetCount(2).value, '{"function": "minecraft:set_count","count": 2}', "count","SetCount().value Int Test")
test.JsonTest(SetCount(False).value, '{"function": "minecraft:set_count","count": 1}', "count","SetCount().value - Bool Test")
test.JsonTest(SetCount([23,"a",False]).value["count"], '{"min": 23}', "min", "SetCount().value['count'] List - Min Int Test")
test.JsonTest(SetCount([23,"a",False]).value["count"], '{"max": 23}', "max", "SetCount().value['count'] List - Max String Test")
test.JsonTest(SetCount([False,"a",1]).value["count"], '{"min": 1}', "min", "SetCount().value['count'] List - Min Bool Test")
test.JsonTest(SetNbt(1).value, '{"tag": ""}', "tag", "SetNbt().value - Random Value test")

console.print("\n[cyan]Entrie Tests:[/cyan]")


test.Exit()
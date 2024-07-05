import sys
from unitTest import Test
sys.path.append('D:/Programas/DPManager/DataPyLib')
from Library.Loot.lootFunction import SetCount, RandomEnchant, SetNbt

test = Test()
test.JsonTest(RandomEnchant().value, '{ "function": "minecraft:enchant_randomly" }', "function",  "RandomEnchant().value")
test.JsonTest(SetCount(2).value, '{"function": "minecraft:set_count","count": 2}', "count","SetCount().value Int Test")
test.JsonTest(SetCount(False).value, '{"function": "minecraft:set_count","count": 2}', "count","SetCount().value Bool Test")

test.Exit()
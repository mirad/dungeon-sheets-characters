# Add to the source file in dungeonsheets/armor.py

class PlateDwarf(HeavyArmor):
    name = "PlateDwarf"
    base_armor_class = 20 # Should be 18+2
    cost = '15,000 gp'
    dexterity_mod_max = 0
    stealth_disadvantage = True
    weight = 65

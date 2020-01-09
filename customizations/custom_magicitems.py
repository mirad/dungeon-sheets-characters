class ScutumOfTheSeventhLegion(MagicItem):
    """
    3x/Day Absorb Elements Thunder/Lighning
    """
    name = "Scutum of the Seventh Legion"
    ac_bonus = 1
    requires_attunement = True
    rarity = 'Rare'

class SwordOfSharpness(MagicItem):
    """- Object take maximum damage
    - On natural 20 -> 14 Slashing Damage, then roll again. natural20: lop of a limb
    - Command 10' bright, 10' dim light
    """
    name = "Sword of Sharpness"
    ac_bonus = 0
    requires_attunement = True
    rarity = 'Rare'
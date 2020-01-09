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

class rapir_plus_1(MagicItem):
    """Magical Damage
    """
    name = "Rapir +1"
    ac_bonus = 0
    requires_attunement = False
    rarity = 'Uncommon'

class HalfPlateOfGleaming(MagicItem):
    """
    The armor never gets dirty
    """
    name = "Half Plate of Gleaming"
    ac_bonus = 0
    requires_attunement = False
    rarity = 'Common'

class SaphireOfGleaming(MagicItem):
    """
    1 inch saqhire, attach to weapon, the weapon can then be used as a spellcasting focus. 
    Cannot be removed
    """
    name = "Saphire of Gleaming"
    ac_bonus = 0
    requires_attunement = True
    rarity = 'Common'

class EndlessSUmmer(MagicItem):
    """
    magic, indistructable
    Advantage on tragic performances
    (reminder: phil)
    """
    name = "Saphire of Gleaming"
    ac_bonus = 0
    requires_attunement = True
    rarity = 'Very Rare'
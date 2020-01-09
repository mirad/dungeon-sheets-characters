class PactWeapon(Longsword):
    name = "PactWeapon"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "d8"
    damage_type = 's'
    properties = 'Versatile (1d10)'


class MagicRapirPlusOne(Rapier):
    name = "Rapir +1"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "d8"
    damage_type = 'p'
    properties = 'Finesse'

class GlaiveOfTheMoon(Rapier):
    name = "Glaive +1"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "d10"
    damage_type = 's'
    properties = 'Heavy, Reach, Two Handed'
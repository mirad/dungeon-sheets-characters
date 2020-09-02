# Add to the source file in dungeonsheets/weapons.py
class PactWeapon(Longsword):
    name = "PactWeapon"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "d8"
    damage_type = 's'
    properties = 'Versatile (1d10)'

class BattleaxePlusOne(MartialWeapon, MeleeWeapon):
    name = "Battleaxe +1"
    cost = "300 gp"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "1d8"
    damage_type = "s"
    weight = 4
    properties = "Versatile (1d10)"
    ability = 'strength'

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
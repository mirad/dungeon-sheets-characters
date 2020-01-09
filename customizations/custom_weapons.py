class PactWeapon(Longsword):
    name = "PactWeapon"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "d8"
    damage_type = 's'
    properties = 'Versatile (1d10)'


class MagicRapir(Rapier):
    name = "Rapir+1"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "d8"
    damage_type = 'p'
    properties = 'Finesse'
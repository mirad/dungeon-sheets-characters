"""This file describes the heroic adventurer Leonie the brave.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Tyrr Ellynide Tiltrivet"
player_name = "Leonie"

# Be sure to list Primary class first
classes = ['Paladin']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [5]  # ex: [10] or [3, 2]
subclasses = ["Oath of The Ancients"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Soldier"
race = "Rock Gnome"
alignment = "Chaotic good"

xp = 0
hp_max = 46
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 16
dexterity = 9
constitution = 14
intelligence = 14
wisdom = 12
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'intimidation', 'insight', 'persuasion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('defense')

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ('martial weapons', 'simple weapons')  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ('Gaming Set Dice', 'Vehicles (Land)')  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Gnomish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 50
pp = 5

# TODO: Put your equipped weapons and armor here
weapons = ['Glaive of the Moon']  # Example: ('shortsword', 'longsword')
magic_items = ('GlaiveOfTheMoon')  # Example: ('ring of protection',)
armor = "Chain Mail"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """Explorers Pack
10 Rations
"""

attacks_and_spellcasting = """Frost Shard Amulet"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()

# Which spells have not been prepared
__spells_unprepared = (
# Level 1
'Bless', 'Command', 'Compelled Duel', 'Cure Wounds', 'Detect Evil and Good',
'Detect Magic', 'Detect Poison and Disease', 'Divine Favor', 'Heroism', 'Protection from Evil and Good',
'Purify Food and Drink', 'Searing Smite', 'Shield of Faith', 'Thunderous Smite', 'Wrathful Smite',
# Xanathas
'Ceremony',
# Level 2
'Aid', 'Branding Smite', 'Find Steed', 'Lesser Restoration', 'Locate Object', 'Magic Weapon', 
'Protection from Poison', 'Zone of Truth'
)

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """personality traits"""

ideals = """ideals"""

bonds = """bonds"""

flaws = """flaws"""

features_and_traits = """Schreib hier was tolles hin! :)"""

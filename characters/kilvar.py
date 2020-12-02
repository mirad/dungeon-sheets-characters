"""This file describes the heroic adventurer Fighter1.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Kilvar - Steelfist"
player_name = "Micha"

# Be sure to list Primary class first
classes = ['Fighter']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [9]  # ex: [10] or [3, 2]
subclasses = ["Battle Master"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Soldier"
race = "Mountain Dwarf"
alignment = "Neutral good"

xp = 0
hp_max = 93
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 20
dexterity = 10
constitution = 18
intelligence = 11
wisdom = 14
charisma = 11

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'intimidation', 'perception', 'survival')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
# features = ('commanders strike', 'disarming attack', 'distracting strike',
#            'evasive footwork', 'rally', 'parry', 'sweeping attack',
#            'lunging attack')
features = ('Riposte', 'Precision Attack', 'Distracting Strike', 'Triping Attack','Menacing Attack', 'Sentinel') #'Triping Attack' at level 

# If selecting among multiple feature options: ex Fighting Style
#Example (Fighting Style):
#feature_choices = ('Archery')
feature_choices = ('dueling',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Dwarvish"""

# Inventory
# TODO: Get yourself some money
cp = 1040
sp = 0
ep = 0
gp = 150
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('Battleaxe +1','handaxe')  # Example: ('shortsword', 'longsword')
magic_items = ('Cloak of Protection')  # Example: ('ring of protection',)
armor = "PlateDwarf"  # Eg "leather armor"
shield = "shield"  # Eg "shield"

equipment = """Squad-Leader clothes, commonm clothes, Sculp (Throphy), Backpack, Bedroll, Mess kit, Tinderbox,  10 torches, 6 days of Rations, Waterskin, 2 Blankets, 1 incense, alms box, hempen rope 50m, Bard, nice blanket  violet (80gp), tent 3 person, Trophy (Sword made out of mithril), Everfull Mug of dwarven beer """

attacks_and_spellcasting = """Disadvantage: Stealth Attack Roll: 1d20+5, 4 Superiority Dice: d8, Maneuver save DC = 8 + my proficiency + my Dex"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """I enjoy being strong and like breaking things. Read Hear and Beard. Scars in the Face."""

ideals = """Independence. When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)"""

bonds = """Someone saved my life on the battlefield. To this day, I will never leave a friend behind."""

flaws = """I have little respect for anyone who is not a proven warrior."""

features_and_traits = """Gaming set (cards), vehicle driving"""

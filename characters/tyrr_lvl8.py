"""This file describes the heroic adventurer Leonie the brave.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Tyrr Ellywick Roywinn Aithne Hallily Soraffit Tiltrivet"
player_name = "Leonie"

# Be sure to list Primary class first
classes = ['Paladin']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [8]  # ex: [10] or [3, 2]
subclasses = ["Oath of The Ancients"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Soldier"
race = "Rock Gnome"
alignment = "Chaotic good"

xp = 0
hp_max = 76
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 19
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
languages = """Common, Gnomish, Sylvan, Dwarven Script"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 11
ep = 65
gp = 12
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ['Glaive of the Moon']  # Example: ('shortsword', 'longsword')
magic_items = ('GlaiveOfTheMoon','GauntletsofOgrePower')  # Example: ('ring of protection',)
armor = "Plate Mail"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """Explorers Pack
1 Saphire
2 Greater Healing Potion
Traveler's Clothes
Stadttunika
Weinschlauch, 2 Rationen
Kristallgläser
6 Kerzen
1 Wollwalk Tarnmantel
Lederhandschuhe
Bergschuhe
Lock Crawler (18, 19, 20 Help action zum Schlösser öffnen)
Tinker's Tools
Leatherworker's Tools
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
personality_traits = """I can stare down a hell hound withouth flinching"""

ideals = """I do what I must and obey just authority"""

bonds = """Those who fight beside me are those worth dying for"""

flaws = """I have little respect for anyone who is not a proven warrior"""

features_and_traits = """Langes, weißes Haar, schwirrt immer in leichter Bewegung um meinen Kopf. Viele blassblaue Narben über den ganzen Körper verteilt. Da mir überall latent zu warm ist, trage ich oft eine Schicht Kleidung weniger als andere."""

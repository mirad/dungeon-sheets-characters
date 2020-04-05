"""This file describes the heroic adventurer Aardsøn.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Aardsøn Sumarlid"
player_name = "Fabian"

# Be sure to list Primary class first
classes = ['Bard']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = []  # ex: [10] or [3, 2]
subclasses = ["College of Valor"]
background = "Entertainer"
race = "Human"
alignment = "Chaotic neutral"

xp = 0
hp_max = 45
inspiration = 1  # integer inspiration value

# Ability Scores
strength = 11
dexterity = 16
constitution = 14
intelligence = 13
wisdom = 12
charisma = 18

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('acrobatics', 'deception', 'performance', 'sleight of hand', 'persuasion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ('persuasion', 'deception')

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
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ('martial weapons', 'simple weapons')  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ('horn', 'harp', 'piano', 'drum')  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish"""
proficiencies = """martial weapons, simple weapons"""

# Inventory
cp = 12
sp = 25
ep = 30
gp = 571
pp = 110

# TODO: Put your equipped weapons and armor here
weapons = ["MagicRapirPlusOne", "Dagger", "Heavy Crossbow"]  # Example: ('shortsword', 'longsword')
magic_items = ('SaphireOfTheWarmage', 'HalfPlateOfGleaming', 'EndlessSummer', 'rapir_plus_1', 'HornOfSummerCourt')  # Example: ('ring of protection',)
armor = "Half Plate"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """Disguise kit, Costume, Formal Cloth, 
Diplomat Pack
Grüne Feder
Duklaimer (Gittare)
Horn
Harfe
13 Hydrazähne
2 Eberdämonenfänge
2 Goldfänge
14 Hydrablut
Schriftrolle m. Ritual
Klapptisch
5 Rationen
5 Smaragde
Flasche Alkohol
Blüte von Immatensien
"""

attacks_and_spellcasting = """2 Attacken,
Saphire of the War Mage am Rapir,
Summer Court Horn,
Harp of Endless Summer,
Scimitar von Abadin (d8/d10),
Kurzschwert
Obsidiandolch"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('Minor Illusion', 'Mage Hand', 'Vicious Mockery', 'Healing Word', "Tashas Hideous Laughter",
"Thunderwave", "Heat Metal", "Enhance Ability", 'Suggestion', "Leomunds Tiny Hut", "Dispel Magic", "Send"
)

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """Loves Good Insults"""

ideals = """Creativity"""

bonds = """Loyal to Harkvaard"""

flaws = """Sucker for pretty Faces"""

features_and_traits = """Countercharm (friendly creatures in 30ft radius advantage on charmed / frightened); Disadvantage on heroic tales (performance),
Blessing,
2 Levels of Exhaustion
"""

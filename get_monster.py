import requests as req
import json

monster_url = "http://dnd5eapi.co/api/monsters/"

# Create a JSON of the full list of Monsters with their individual info URLs
monsters = req.get(monster_url).json()

# Create lists of the monster names and their urls
monster_list = [r["name"] for r in monsters["results"]]
url_list = [r["url"] for r in monsters["results"]]
# Zip those into a dictionary ({"Name":"URL"})
url_dict = dict(zip(monster_list,url_list))

# Get name of monster from user
monster_name = input("\nWhat Monster are you facing? ")

# If the name entered is not in the monster list
while monster_name not in monster_list:

    # Print out the monster list
    print ()
    for m in monster_list:
        print (m)
    # Ask for a new input
    monster_name = input("\nSorry, not found. Please enter one of the above: ")

# Create a JSON of the monster's individual information
monster = req.get(url_dict[monster_name]).json()

# Print the information in a readable way:

print ("\n#########################################")
#print "Monster Name: Size type (subtype)"
print ("{0}: {1} {2} ({3})".format(monster["name"],monster["size"],monster["type"],monster["subtype"]))
print ("#########################################")

print ("\nALIGNMENT: {0}".format(monster["alignment"]))
print ("CHALLENGE RATING: {0}".format(monster["challenge_rating"]))

print ("\nAC: {0}     HP: {1} ({2})     SPEED: {3}".format(monster["armor_class"],monster["hit_points"],monster["hit_dice"],monster["speed"]))
print ("SENSES: {0}".format(monster["senses"]))
print ("LANGUAGES: {0}".format(monster["languages"]))

print ("\nSTR:{0}    DEX:{1}    CON:{2}".format(monster["strength"],monster["dexterity"],monster["constitution"]))
print ("INT:{0}    WIS:{1}    CHA:{2}".format(monster["intelligence"],monster["wisdom"],monster["charisma"]))

print ("\nSAVING THROWS:")
# Bonuses to Saves are stored as dictionary entries i.e. {"strength_save":3}
# There is no entry if there is no inherent bonus
# Create a list of attributes (begin with caps for print formatting later)
saving_throws = ["STRENGTH",
                "DEXTERITY",
                "CONSTITUTION",
                "INTELLIGENCE",
                "WISDOM",
                "CHARISMA"
                ]
# For each attribute in the list,
for ability in saving_throws:
    # Set the format to the possible key
    ability_save = ability.lower() + "_save"
    try:
        # If there is a dictionary entry, print it
        print("{0}: +{1}".format(ability,monster[ability_save]))
    except:
        pass

# See above documentation
print ("\nSKILLS:")
skills = ["athletics",
        "acrobatics",
        "sleight_of_Hand",
        "stealth",
        "arcana",
        "history",
        "investigation",
        "nature",
        "religion",
        "animal_handling",
        "insight",
        "medicine",
        "perception",
        "survival",
        "deception",
        "intimidation",
        "performance",
        "persuasion"
        ]
for skill in skills:
    skill_name = skill.upper()
    try:
        print("{0}: +{1}".format(skill_name,monster[skill]))
    except:
        pass

print ("\nVULNERABILITIES: {0}".format(monster["damage_vulnerabilities"]))
print ("RESISTANCES: {0}".format(monster["damage_resistances"]))

print ("\nSPECIAL ABILITIES:")
try:
    for x in monster["special_abilities"]:
        print ("\n{0}:".format(x["name"]))
        if x["attack_bonus"] != 0:
            print ("ATTACK BONUS: {0}".format(x["attack_bonus"]))
        print (x["desc"])
except:
    pass

print ("\nACTIONS:")
for x in monster["actions"]:
    print ("\n{0}".format(x["name"]))
    if x["attack_bonus"] != 0:
        print ("ATT: +{0}    DMG: {1} +{2}".format(x["attack_bonus"],x["damage_dice"],x["damage_bonus"]))
    print (x["desc"])

print ("\nLEGENDARY ACTIONS:")
try:
    for x in monster["legendary_actions"]:
        print ("\n{0}".format(x["name"]))
        if x["attack_bonus"] != 0:
            print ("ATT: +{0}    DMG: {1} +{2}".format(x["attack_bonus"],x["damage_dice"],x["damage_bonus"]))
        print (x["desc"])
except:
    pass
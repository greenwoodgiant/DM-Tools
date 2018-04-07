import requests as req
import json

race_url = "http://dnd5eapi.co/api/races/"
subrace_url = "http://dnd5eapi.co/api/subraces/"
class_url = "http://dnd5eapi.co/api/classes/"
subclass_url = "http://dnd5eapi.co/api/subclasses/"
language_url = "http://dnd5eapi.co/api/languages/"
spell_url = "http://dnd5eapi.co/api/spells/"
monster_url = "http://dnd5eapi.co/api/monsters/"
feature_url = "http://dnd5eapi.co/api/features/"
equipment_url = "http://dnd5eapi.co/api/equipment/"
proficiency_url = "http://dnd5eapi.co/api/proficiencies/"
startequip_url = "http://dnd5eapi.co/api/startingequipment/"

# Create a JSON of the full list of spells with their individual info URLs
spells = req.get(spell_url).json()

# Create lists of the spell names and their urls
spell_list = [r["name"] for r in spells["results"]]
url_list = [r["url"] for r in spells["results"]]
# Zip those into a dictionary ({"Name":"URL"})
url_dict = dict(zip(spell_list,url_list))

# Get name of spell from user
spell_name = input("\nWhat Spell are you casting? ")

# If the name entered is not in the spell list
while spell_name not in spell_list:
    # Print out the spell list
    print ()
    for s in spell_list:
        print (s)
    # Ask for a new input
    spell_name = input("\nSorry, not found. Please enter one of the above: ")

# Create a JSON of the spell's individual information
spell = req.get(url_dict[spell_name]).json()

print ("\n#########################################")
print ("{0}: {1} {2} ({3})".format(spell["name"],spell["school"]["name"],spell["level"],spell["page"]))
print ("#########################################")

print ("\nCASTING TIME: {0}".format(spell["casting_time"]))
print ("DURATION: {0}".format(spell["duration"]))

print ("\nRANGE: {0}     COMPONENTS: {1}".format(spell["range"],spell["components"]))
print ("\nCONCENTRATION: {0}     RITUAL: {1}".format(spell["concentration"],spell["ritual"]))

print ("\n" + spell["desc"][0])

try:
    print ("\nAT HIGHER LEVELS: " + spell["higher_level"][0])
except:
    pass
from random import randint
# from more_itertools import unique_everseen
from time import sleep
print ()
"""
"""
#   Databases linking Attribute, Modifier, and Skill Bonus to a value 
ability_scores = {
                "STRENGTH" : 0,
                "DEXTERITY" : 0,
                "CONSTITUTION" : 0,
                "INTELLIGENCE" : 0,
                "WISDOM" : 0,
                "CHARISMA" : 0
        }
ability_modifiers = {
                "STRENGTH" : 0,
                "DEXTERITY" : 0,
                "CONSTITUTION" : 0,
                "INTELLIGENCE" : 0,
                "WISDOM" : 0,
                "CHARISMA" : 0
        }

skill_modifiers = {
                "ATHLETICS" : 0,
                "ACROBATICS" : 0,
                "SLEIGHT OF HAND" : 0,
                "STEALTH" : 0,
                "ARCANA" : 0,
                "HISTORY" : 0,
                "INVESTIGATION" : 0,
                "NATURE" : 0,
                "RELIGION" : 0,
                "ANIMAL HANDLING" : 0,
                "INSIGHT" : 0,
                "MEDICINE" : 0,
                "PERCEPTION" : 0,
                "SURVIVAL" : 0,
                "DECEPTION" : 0,
                "INTIMIDATION" : 0,
                "PERFORMANCE" : 0,
                "PERSUASION" : 0
        }
skill_to_ability = {
                "ATHLETICS" : "STRENGTH",
                "ACROBATICS" : "DEXTERITY",
                "SLEIGHT OF HAND" : "DEXTERITY",
                "STEALTH" : "DEXTERITY",
                "ARCANA" : "INTELLIGENCE",
                "HISTORY" : "INTELLIGENCE",
                "INVESTIGATION" : "INTELLIGENCE",
                "NATURE" : "INTELLIGENCE",
                "RELIGION" : "INTELLIGENCE",
                "ANIMAL HANDLING" : "WISDOM",
                "INSIGHT" : "WISDOM",
                "MEDICINE" : "WISDOM",
                "PERCEPTION" : "WISDOM",
                "SURVIVAL" : "WISDOM",
                "DECEPTION" : "CHARISMA",
                "INTIMIDATION" : "CHARISMA",
                "PERFORMANCE" : "CHARISMA",
                "PERSUASION" : "CHARISMA"
        }

#   List of attributes, skill and feats available to the character.
#   (Functions will remove items from list to prevent doubling)
avail_attributes = [
                "STRENGTH",
                "DEXTERITY",
                "CONSTITUTION",
                "INTELLIGENCE",
                "WISDOM",
                "CHARISMA"
            ]
avail_skills = [
                "ATHLETICS",
                "ACROBATICS",
                "SLEIGHT OF HAND",
                "STEALTH",
                "ARCANA",
                "HISTORY",
                "INVESTIGATION",
                "NATURE",
                "RELIGION",
                "ANIMAL HANDLING",
                "INSIGHT",
                "MEDICINE",
                "PERCEPTION",
                "SURVIVAL",
                "DECEPTION",
                "INTIMIDATION",
                "PERFORMANCE",
                "PERSUASION"
        ]
avail_feats = [
                "ALERT",
                "ATHLETE",
                "ACTOR",
                "CHARGER",
                "CROSSBOW EXPERT",
                "DEFENSIVE DUELIST",
                "DUAL WIELDER",
                "DUNGEON DELVER",
                "DURABLE",
                "ELEMENTAL ADEPT",
                "GRAPPLER",
                "GREAT WEAPON MASTER",
                "HEALER",
                "HEAVILY ARMORED",
                "HEAVY ARMOR MASTER",
                "INSPIRING LEADER",
                "KEEN MIND",
                "LIGHTLY ARMORED",
                "LINGUIST",
                "LUCKY",
                "MAGE SLAYER",
                "MAGIC INITIATE",
                "MARTIAL ADEPT",
                "MEDIUM ARMOR MASTER",
                "MOBILE",
                "MODERATELY ARMORED",
                "MOUNTED COMBATANT",
                "OBSERVANT",
                "POLEARM MASTER",
                "RESILIENT",
                "RITUAL CASTER",
                "SAVAGE ATTACKER",
                "SENTINEL",
                "SHARPSHOOTER",
                "SHIELD MASTER",
                "SKILLED",
                "SKULKER",
                "SPELL SNIPER",
                "TAVERN BRAWLER",
                "TOUGH",
                "WAR CASTER",
                "WEAPON MASTER"
            ]

#   List available things to gain proficiency with
tools = [
                "ALCHEMIST'S SUPPLIES",
                "BREWER'S SUPPLIES",
                "CALLIGRAPHER'S SUPPLIES",
                "CARPENTER'S TOOLS",
                "CARTOGRAPHER'S TOOLS",
                "COBBLER'S TOOLS",
                "COOK'S UTENSILS",
                "GLASSBLOWER'S TOOLS",
                "JEWELER'S TOOLS",
                "LEATHERWORKER'S TOOLS",
                "MASON'S TOOLS",
                "PAINTER'S SUPPLIES",
                "POTTER'S TOOLS",
                "SMITH'S TOOLS",
                "TINKER'S TOOLS",
                "WEAVER'S TOOLS",
                "WOODCARVER'S TOOLS"
        ]
instruments = [
                "BAGPIPES",
                "DRUM",
                "DULCIMER",
                "FLUTE",
                "LUTE",
                "LYRE",
                "HORN",
                "PAN FLUTE",
                "SHAWM",
                "VIOL"
        ]
gaming_sets = [
                "DICE",
                "DRAGONCHESS",
                "PLAYING CARDS",
                "THREE-DRAGON ANTE"
        ]
languages = [
                "DWARVEN",
                "ELVEN",
                "GIANT",
                "GITH",
                "GNOMISH",
                "GOBLIN",
                "HALFLING",
                "ORC",
                "ABYSSAL",
                "CELESTIAL",
                "DRACONIC",
                "DEEP SPEECH",
                "INFERNAL",
                "PRIMORDIAL",
                "SYLVAN",
                "UNDERCOMMON"
            ]

simple_wpns = [
                "CLUB",
                "DAGGER",
                "GREATCLUB",
                "HANDAXE",
                "JAVELIN",
                "LIGHT HAMMER",
                "MACE",
                "QUARTERSTAFF",
                "SICKLE",
                "SPEAR",
                "LIGHT CROSSBOW",
                "DART",
                "SHORTBOW",
                "SLING"
            ]
martial_wpns = [
                "BATTLEAXE",
                "FLAIL",
                "GLAIVE",
                "GREATAXE",
                "GREATSWORD",
                "HALBERD",
                "LANCE",
                "LONGSWORD",
                "MAUL",
                "MORNINGSTAR",
                "PIKE",
                "RAPIER",
                "SCIMITAR",
                "SHORT SWORD",
                "TRIDENT",
                "WAR PICK",
                "WARHAMMER",
                "WHIP"
                ]
armor = [
        "LIGHT",
        "MEDIUM",
        "HEAVY",
        "SHIELDS"
        ]   
saves = [
                "STRENGTH",
                "DEXTERITY",
                "CONSTITUTION",
                "INTELLIGENCE",
                "WISDOM",
                "CHARISMA"
                ]   
avail_profs = [
                tools, 
                instruments, 
                gaming_sets, 
                languages, 
                simple_wpns, 
                martial_wpns,
                saves
                ]

#   Empty lists to add Profs, Race/Class/Background features and Inventory items to.
proficiencies = ["Languages (COMMON)"]
race_features = []
class_features = []
bg_features = []
inventory = []

#   Lists of available spells by Class/Level to build Spellbook from
bard_spell_0 = [
                "BLADE WARD",
                "DANCING LIGHTS",
                "FRIENDS",
                "LIGHT",
                "MAGE HAND",
                "MENDING",
                "MESSAGE",
                "MINOR ILLUSION",
                "PRESTIDIGITATION",
                "TRUE STRIKE",
                "VICIOUS MOCKERY",
                "THUNDERCLAP (XAN)"
                ]
cleric_spell_0 = [
                "GUIDANCE",
                "LIGHT",
                "MENDIING",
                "RESISTANCE",
                "SACRED FLAME",
                "SPARE THE DYING",
                "THAUMATURGY",
                "TOLL THE DEAD (XAN)",
                "WORD OF RADIANCE (XAN)"
                ]
druid_spell_0 = [
                "DRUIDCRAFT",
                "GUIDANCE",
                "MENDING",
                "POISON SPRAY",
                "PRODUCE FLAME",
                "RESISTANCE",
                "SHILLELAGH",
                "THORN WHIP",
                "CREATE BONFIRE (XAN)",
                "CONTROL FLAMES (XAN)",
                "FROSTBITE (XAN)",
                "GUST (XAN)",
                "MAGIC STONE (XAN)",
                "MOLD EARTH (XAN)",
                "PRIMAL SAVAGERY (XAN)",
                "SHAPE WATER (XAN)",
                "THUNDERCLAP (XAN)"
                ]
sorc_spell_0 = [
                "ACID SPLASH",
                "BLADE WARD",
                "CHILL TOUCH",
                "DANCING LIGHTS",
                "FIRE BOLT",
                "FRIENDS",
                "LIGHT",
                "MAGE HAND",
                "MENDING",
                "MESSAGE",
                "MINOR ILLUSION",
                "POISON SPRAY",
                "PRESTIDIGITATION",
                "RAY OF FROST",
                "SHOCKING GRASP",
                "TRUE STRIKE",
                "CREATE BONFIRE (XAN)",
                "CONTROL FLAMES (XAN)",
                "FROSTBITE (XAN)",
                "GUST (XAN)",
                "MOLD EARTH (XAN)",
                "SHAPE WATER (XAN)",
                "THUNDERCLAP (XAN)",
                "INFESTATION (XAN)"
                ]
warlock_spell_0 = [
                "BLADE WARD",
                "CHILL TOUCH",
                "ELDRITCH BLAST",
                "FRIENDS",
                "MAGE HAND",
                "MINOR ILLUSION",
                "POISON SPRAY",
                "PRESTIDIGITATION",
                "TRUE STRIKE",
                "CREATE BONFIRE (XAN)",
                "FROSTBITE (XAN)",
                "INFESTATION (XAN)",
                "MAGIC STONE (XAN)",
                "THUNDERCLAP (XAN)",
                "TOLL THE DEAD (XAN)"
                ]
wiz_spell_0 = [
                "ACID SPLASH",
                "BLADE WARD",
                "CHILL TOUCH",
                "DANCING LIGHTS",
                "FIRE BOLT",
                "FRIENDS",
                "LIGHT",
                "MAGE HAND",
                "MENDING",
                "MESSAGE",
                "MINOR ILLUSION",
                "POISON SPRAY",
                "PRESTIDIGITATION",
                "RAY OF FROST",
                "SHOCKING GRASP",
                "TRUE STRIKE",
                "CREATE BONFIRE (XAN)",
                "CONTROL FLAMES (XAN)",
                "FROSTBITE (XAN)",
                "GUST (XAN)",
                "INFESTATION (XAN)",
                "MOLD EARTH (XAN)",
                "SHAPE WATER (XAN)",
                "THUNDERCLAP (XAN)",
                "TOLL THE DEAD (XAN)"
                ]

bard_spell_1 = [
                "ANIMAL FRIENDSHIP",
                "BANE",
                "CHARM PERSON",
                "COMPREHEND LANGUAGES",
                "CURE WOUNDS",
                "DETECT MAGIC",
                "DISGUISE SELF",
                "DISSONANT WHISPERS",
                "FAERIE FIRE",
                "FEATHER FALL",
                "HEALING WORD",
                "HEROISM",
                "IDENTIFY",
                "ILLUSORY SCRIPT",
                "LONGSTRIDER",
                "SILENT IMAGE",
                "SLEEP",
                "SPEAK WITH ANIMALS",
                "TASHA'S HIDEOUS LAUGHTER",
                "THUNDERWAVE",
                "UNSEEN SERVANT",
                "EARTH TREMOR (XAN)"
                ]
cleric_spell_1 = [
                "BANE",
                "BLESS",
                "COMMAND",
                "CREATE OR DESTROY WATER",
                "CURE WOUNDS",
                "DETECT EVIL AND GOOD",
                "DETECT MAGIC",
                "DETECT POISON AND DISEASE",
                "GUIDING BOLT",
                "HEALING WORD",
                "INFLICT WOUNDS",
                "PROTECTION FROM EVIL AND GOOD",
                "PURIFY FOOD AND DRINK",
                "SANCTUARY",
                "SHIELD OF FAITH",
                "CEREMONY (XAN)"
                ]
druid_spell_1 = [
                "ANIMAL FRIENDSHIP",
                "CHARM PERSON",
                "CREATE OR DESTROY WATER",
                "CURE WOUNDS",
                "DETECT MAGIC",
                "DETECT POISON AND DISEASE",
                "ENTANGLE",
                "FAERIE FIRE",
                "FOG CLOUD",
                "GOODBERRY",
                "HEALING WORD",
                "JUMP",
                "LONGSTRIDER",
                "PURIFY FOOD AND DRINK",
                "SPEAK WITH ANIMALS",
                "THUNDERWAVE",
                "ABSORB ELEMENTS (XAN)",
                "BEAST BOND (XAN)",
                "ICE KNIFE (XAN)",
                "SNARE (XAN)"
                ]
sorc_spell_1 = [
                "BURNING HANDS",
                "CHARM PERSON",
                "CHROMATIC ORB",
                "COLOR SPRAY",
                "COMPREHEND LANGUAGES",
                "DETECT MAGIC",
                "DISGUISE SELF",
                "EXPEDITIOUS RETREAT",
                "FALSE LIFE",
                "FEATHER FALL",
                "FOG CLOUD",
                "JUMP",
                "MAGE ARMOR",
                "MAGIC MISSILE",
                "RAY OF SICKNESS",
                "SHIELD",
                "SILENT IMAGE",
                "SLEEP",
                "THUNDERWAVE",
                "WITCH BOLT",
                "ABSORB ELEMENTS (XAN)",
                "CHAOS BOLT (XAN)",
                "CATAPULT (XAN)",
                "ICE KNIFE (XAN)",
                "EARTH TREMOR (XAN)"
                ]
warlock_spell_1 = [
                "ARMOR OF AGATHYS",
                "ARMS OF HADAR",
                "CHARM PERSON",
                "COMPREHEND LANGUAGES",
                "EXPEDITIOUS RETREAT",
                "HELLISH REBUKE",
                "HEX",
                "ILLUSORY SCRIPT",
                "PROTECTION FROM EVIL AND GOOD",
                "UNSEEN SERVANT",
                "WITCH BOLT",
                "CAUSE FEAR (XAN)"
                ]
wiz_spell_1 = [
                "ALARM",
                "BURNING HANDS",
                "CHARM PERSON",
                "CHROMATIC ORB",
                "COLOR SPRAY",
                "COMPREHEND LANGUAGES",
                "DETECT MAGIC",
                "DISGUISE SELF",
                "EXPEDITIOUS RETREAT",
                "FALSE LIFE",
                "FEATHER FALL",
                "FIND FAMILIAR",
                "FOG CLOUD",
                "GREASE",
                "IDENTIFY",
                "ILLUSORY SCRIPT",
                "JUMP",
                "LONGSTRIDER",
                "MAGE ARMOR",
                "MAGIC MISSILE",
                "PROTECTION FROM EVIL AND GOOD",
                "RAY OF SICKNESS",
                "SHIELD",
                "SILENT IMAGE",
                "SLEEP",
                "TASHA'S HIDEOUS LAUGHTER",
                "TENSER'S FLOATING DISC",
                "THUNDERWAVE",
                "UNSEEN SERVANT",
                "WITCH BOLT"
                "ABSORB ELEMENTS (XAN)",
                "CATAPULT (XAN)",
                "CAUSE FEAR (XAN)",
                "SNARE (XAN)",
                "ICE KNIFE (XAN)",
                "EARTH TREMOR (XAN)"
                ]

#   Empty lists for Spellbooks (by Spell level)
spellbook_0 = ["CANTRIPS:"]
spellbook_1 = ["LEVEL 1 SPELLS:"]
spellbook = [spellbook_0, spellbook_1]

#   Return a random item from a group/list
def get_item(group):
   item = (randint(1, (len(group))) - 1)
   return group[item]

#   Gain proficiency in a random skill from a certain skill set
def get_skill(skill_set):
    
    # Return a random item from the skill set
    chosen_skill = get_item(skill_set)

    # If the character already has proficiency,
    if skill_modifiers[(chosen_skill)] > 0:
        # Find/Remove this skill in the list of available skills
        for item in avail_skills:
            if item == chosen_skill:
                avail_skills.remove(item)
        # Then start over with the list of available skills
        get_skill(avail_skills)

    else:
        # Otherwise, add proficiency bonus to that skill's modifier
        skill_modifiers[(chosen_skill)] += 2

    # Find/Remove this skill in the list of available skills
    for item in avail_skills:
        if item == chosen_skill:
            avail_skills.remove(item)
    
    # Find/Remove this skill in the original skill set list
    for item in skill_set:
        if item == chosen_skill:
            skill_set.remove(item)

#   Gain expertise in a random skill from a certain skill set
#   (Same as get_skill except will double proficiency if already proficient)
def get_expertise(skill_set):
    
    # Return a random skill from skill set
    chosen_skill = get_item(skill_set)

    # For Thieves' Tools, update Proficiency list to reflect Expertise
    if chosen_skill == "THIEVES' TOOLS":
        proficiencies.remove("Tools (THIEVES' TOOLS)")
        proficiencies.append("Tools (THIEVES' TOOLS) *EXPERTISE*")
    else:
        # Otherwise, add proficiency bonus to skill modifier
        skill_modifiers[(chosen_skill)] += 2

        # Find/Remove skill in list of available skills
        for item in avail_skills:
            if item == chosen_skill:
                avail_skills.remove(item)

        # Find/Remove skill in original skill set
        for item in skill_set:
            if item == chosen_skill:
                skill_set.remove(item)

#   Gain proficiency in a specific item from a group
def get_proficiency(chosen_item, group=avail_profs):
    
    # Return a random item if asked to "GET"
    if chosen_item == "GET":
        chosen_item = get_item(group)
                
    if chosen_item in group:
        group.remove(chosen_item)
    
    if group == tools:
        inventory.append(chosen_item)
        chosen_item = "Tools ({0})".format(chosen_item)
    if group == instruments:
        inventory.append(chosen_item)
        chosen_item = "Instruments ({0})".format(chosen_item)
    if group == gaming_sets:
        inventory.append(chosen_item)
        chosen_item = "Games ({0})".format(chosen_item)
    if group == languages:
        chosen_item = "Languages ({0})".format(chosen_item)
    if group == simple_wpns or group == martial_wpns:
        chosen_item = "Weapons ({0})".format(chosen_item)
    if group == saves:
        chosen_item = "Saving Throws ({0})".format(chosen_item)
    if group == armor:
        chosen_item = "Armor ({0})".format(chosen_item)

    proficiencies.append(chosen_item)
   
    return (chosen_item)

def get_feat():

    def stat_required(feat, attribute, score):
    
        if ability_scores[(attribute)] < score:

            avail_feats.remove(feat)
            get_feat()

    def stat_bump(stat_1, stat_2):
        stat_options = []
        stat_options.append(stat_1)
        stat_options.append(stat_2)

        chosen_stat = get_item(stat_options)

        if ability_scores[chosen_stat] < 20:
            ability_scores[chosen_stat] += 1
        
        elif stat_1 < 20 or stat_2 < 20:
            stat_bump(stat_1, stat_2)
        
        return chosen_stat
    
    chosen_feat = get_item(avail_feats)

    if chosen_feat == "ALERT":

        race_features.append("ALERT: +5 bonus to Initiative")
        race_features.append("     : Cannot be surprised while conscious.")
        race_features.append("     : Creatures don't gain advantage for being hidden from you.")
        
        avail_feats.remove("ALERT")
        return "ALERT" 
    if chosen_feat == "ATHLETE":

        stat_bump("STRENGTH", "DEXTERITY")

        race_features.append("ATHLETE: Standing from prone only uses 5ft of movement.")
        race_features.append("       : Climbing doesn't halve your speed.")
        race_features.append("       : Only require 5ft for a running high/long jump instead of 10.")

        avail_feats.remove("ATHLETE")
        return "ATHLETE"
    if chosen_feat == "ACTOR":

        ability_scores[("CHARISMA")] += 1

        race_features.append("ACTOR: ADV: Deception / Performance when passing yourself off as someone else.")
        race_features.append("     : You can mimic the speech or sounds of a creature if you have heard it for at least 1 minute.")
        race_features.append("     : Creature makes WIS check vs. your Deception check to determine the effect is faked.")

        avail_feats.remove("ACTOR")
        return "ACTOR"   
    if chosen_feat == "CHARGER":

        race_features.append("CHARGER: On [Dash], Use [Bonus] to make one melee attack or to shove a creature")
        race_features.append("       : If you move at least 10ft in straight line before the attack/shove,")
        race_features.append("       : Add +5 to the damage roll or shove 10ft instead of 5ft")

        avail_feats.remove("CHARGER")
        return "CHARGER"
    if chosen_feat == "CROSSBOW EXPERT":

        race_features.append("CROSSBOW EXPERT: Ignore 'loading' quality of xbows you are proficient in")
        race_features.append("      : No DISADV: Ranged Attack rolls within 5ft of hostile creature")
        race_features.append("      : On [Attack], use [Bonus] to fire a loaded hand xbow you are holding")

        avail_feats.remove("CROSSBOW EXPERT")
        return "CROSSBOW EXPERT"
    if chosen_feat == "DEFENSIVE DUELIST":

        stat_required("DEFENSIVE DUELIST", "DEXTERITY", 13)

        race_features.append("DEFENSIVE DUELIST: When wielding finesse melee weapon and hit by melee attack,")
        race_features.append("        : Use [Reaction] to add Proficiency to AC for that attack")
        avail_feats.remove("DEFENSIVE DUELIST")
        return "DEFENSIVE DUELIST"
    if chosen_feat == "DUAL WIELDER":

        race_features.append("DUAL WIELDER: Gain +1 to AC while dual-wielding")
        race_features.append("      : Dual-wield weapons that aren't 'light'")
        race_features.append("      : Draw or stow two melee weapons at the same time")

        avail_feats.remove("DUAL WIELDER")
        return "DUAL WIELDER"
    if chosen_feat == "DUNGEON DELVER":

        race_features.append("DUNGEON DELVER: ADV: Perception / Investigation v. Secret Doors")
        race_features.append("      : ADV: Saves v. Traps, RES: Damage from Traps")
        race_features.append("      : Search for traps at normal pace instead of slow")

        avail_feats.remove("DUNGEON DELVER")
        return "DUNGEON DELVER"
    if chosen_feat == "DURABLE":

        ability_scores[("CONSTITUTION")] += 1

        race_features.append("DURABLE: When rolling HD during SR, gain at least 2x CON Mod")

        avail_feats.remove("DURABLE")
        return "DURABLE"
    if chosen_feat == "ELEMENTAL ADEPT":

        elements = [
                    "ACID",
                    "COLD",
                    "FIRE",
                    "LIGHTNING",
                    "THUNDER"
                    ]
        elem_adept = get_item(elements)
        
        race_features.append("{0} ADEPT: Spells which deal {1} damage ignore DR.".format(elem_adept, elem_adept))
        race_features.append("      : When you roll for {0} damage, count 1's as 2's".format(elem_adept))
        race_features.append("")

        elements.remove(elem_adept)
        return "ELEMENTAL ADEPT"
    if chosen_feat == "GRAPPLER":

        stat_required("GRAPPLER", "STRENGTH", 13)

        race_features.append("GRAPPLER: ADV: Attacks v. Creature you are grappling")
        race_features.append("    : Use [Action] to pin a grappled creature with another grapple check;")
        race_features.append("    : On success, You and creature are both restrained until grapple ends")
        race_features.append("    : Creatures 1 size larger than you don't auto-escape your grapple")

        avail_feats.remove("GRAPPLER")
        return "GRAPPLER"
    if chosen_feat == "GREAT WEAPON MASTER":

        race_features.append("GREAT WEAPON MASTER: On Critical Hit with melee or dropping")
        race_features.append("       : creature to 0HP, use [Bonus] for 1 melee attack")
        race_features.append("       : Before you attack with heavy melee weapon, you can")
        race_features.append("       : take -5 on attack roll for +10 to damage roll")

        avail_feats.remove("GREAT WEAPON MASTER")
        return "GREAT WEAPON MASTER"
    if chosen_feat == "HEALER":

        race_features.append("HEALER: When you use Healing Kit to stabilize, creature gains 1 HP as well")
        race_features.append("      : [Action]: Use Healing Kit to restore 1d6 + 4 + target's HD in HP")
        race_features.append("                : (Once per target per Short Rest)")

        avail_feats.remove("HEALER")
        return "HEALER"
    if chosen_feat == "HEAVILY ARMORED":

        #*!* You will need to be proficient with Medium Armor through Race, Class, or Background to use this feat*!*")

        ability_scores[("STRENGTH")] += 1
        if ability_scores[("STRENGTH")] > 20:
            ability_scores[("STRENGTH")] = 20

        get_proficiency("HEAVY", armor)

        avail_feats.remove("HEAVILY ARMORED")
        return "HEAVILY ARMORED"
    if chosen_feat == "HEAVY ARMOR MASTER":

        #"*!*You will need to be proficient with Heavy Armor through Race, Class, or Background to use this feat*!*")
        
        ability_scores[("STRENGTH")] += 1
        if ability_scores[("STRENGTH")] > 20:
            ability_scores[("STRENGTH")] = 20

        race_features.append("HEAVY ARMOR MASTER: While Heavily Armored, Gain DR 3")
        race_features.append("      : (Non-magical Bludgeoning/Piercing/Slashing)")

        avail_feats.remove("HEAVY ARMOR MASTER")
        return "HEAVILY ARMORED"
    if chosen_feat == "INSPIRING LEADER":

        stat_required("INSPIRING LEADER", "CHARISMA", 13)

        race_features.append("INSPIRING LEADER: Spend 10 min inspiring companions,")
        race_features.append("     : choose <6 friendly creatures (including yourself) who see/hear and understand you")
        race_features.append("     : Gain temp HP = your Level + your Charisma Modifier (1/creature/SR)")

        avail_feats.remove("INSPIRING LEADER")
        return "INSPIRING LEADER"
    if chosen_feat == "KEEN MIND":

        ability_scores[("INTELLIGENCE")] += 1
        if ability_scores[("INTELLIGENCE")] > 20:
            ability_scores[("INTELLIGENCE")] = 20

        race_features.append("KEEN MIND: Always know which way is North / time of day")
        race_features.append("         : Accurately recall anything seen or heard in past month")

        avail_feats.remove("KEEN MIND")
        return "KEEN MIND"
    if chosen_feat == "LIGHTLY ARMORED":

        stat_bump("STRENGTH", "DEXTERITY")

        get_proficiency("LIGHT", armor)

        race_features.append("LIGHTLY ARMORED: Gain Proficiency in Light Armor")

        avail_feats.remove("LIGHTLY ARMORED")
        return "LIGHTLY ARMORED"
    if chosen_feat == "LINGUIST":

        ability_scores[("INTELLIGENCE")] += 1
        if ability_scores[("INTELLIGENCE")] > 20:
            ability_scores[("INTELLIGENCE")] = 20

        get_proficiency("GET", languages)
        get_proficiency("GET", languages)
        get_proficiency("GET", languages)

        race_features.append("LINGUIST: Create written codes; INT check DC(8 + Prof + INT Mod) to decipher")

        avail_feats.remove("LINGUIST")
        return "LINGUIST"
    if chosen_feat == "LUCKY":

        race_features.append("LUCKY: (3/LR) : On attack/ability_scores/saving throw,")
        race_features.append("     : before outcome is determined, roll an")
        race_features.append("     : additional d20 and take either roll.")
        race_features.append("     : Can also use for attack made against you.")

        avail_feats.remove("LUCKY")
        return "LUCKY"
    if chosen_feat == "MAGE SLAYER":

        race_features.append("MAGE SLAYER: [Reaction]: When spell cast w/in 5ft of you,")
        race_features.append("     : Make melee weapon attack against that creature.")
        race_features.append("     : Creatures you hit have DISADV: maintain Concentration")
        race_features.append("     : ADV: Save v. spells cast w/in 5ft of you")

        avail_feats.remove("MAGE SLAYER")
        return "MAGE SLAYER"
    if chosen_feat == "MAGIC INITIATE":

        initiate_classes = ["BARD", "CLERIC", "DRUID", "SORCERER", "WARLOCK", "WIZARD"]
        chosen_class = get_item(initiate_classes)

        if chosen_class == "BARD":
            get_spell("GET", bard_spell_0, spellbook_0)
            get_spell("GET", bard_spell_0, spellbook_0)
            initiate_spell = get_item(bard_spell_1)
        if chosen_class == "CLERIC":
            get_spell("GET", cleric_spell_0, spellbook_0)
            get_spell("GET", cleric_spell_0, spellbook_0)
            initiate_spell = get_item(cleric_spell_1)
        if chosen_class == "DRUID":
            get_spell("GET", druid_spell_0, spellbook_0)
            get_spell("GET", druid_spell_0, spellbook_0)
            initiate_spell = get_item(druid_spell_1)
        if chosen_class == "SORCERER":
            get_spell("GET", sorc_spell_0, spellbook_0)
            get_spell("GET", sorc_spell_0, spellbook_0)
            initiate_spell = get_item(sorc_spell_1)
        if chosen_class == "WARLOCK":
            get_spell("GET", warlock_spell_0, spellbook_0)
            get_spell("GET", warlock_spell_0, spellbook_0)
            initiate_spell = get_item(warlock_spell_1)
        if chosen_class == "WIZARD":
            get_spell("GET", wiz_spell_0, spellbook_0)
            get_spell("GET", wiz_spell_0, spellbook_0)
            initiate_spell = get_item(warlock_spell_1)

        race_features.append("{0} INITIATE: Cast {1} 1/LR at lowest level (CHA Spell Ability)".format(chosen_class, initiate_spell))

        initiate_classes.remove(chosen_class)
        return "MAGIC INITIATE"
    if chosen_feat == "MARTIAL ADEPT":

        race_features.append("MARTIAL ADEPT: Learn Two Maneuvers, Save DC: 8 + Prof + (STR or DEX)")
        race_features.append("     : +1 Superiority Die (d6) to fuel Maneuvers, replenish after [SR]")

        battle_maneuvers = [
                    "COMMANDER'S STRIKE",
                    "DISARMING ATTACK",
                    "DISTRACTING STRIKE",
                    "EVASIVE FOOTWORK",
                    "FEINTING ATTACK",
                    "GOADING ATTACK",
                    "LUNGING ATTACK",
                    "MANEUVERING ATTACK",
                    "MENACING ATTACK",
                    "PARRY",
                    "PRECISION ATTACK",
                    "PUSHING ATTACK",
                    "RALLY",
                    "RIPOSTE",
                    "SWEEPING ATTACK",
                    "TRIP ATTACK"
                    ]
        maneuver_text = [
                    "COMMANDER'S STRIKE: On [Att]: Forgo an attack to direct ally that can\n     : see/hear you to attack, adding 1d6 to damage roll",
                    "DISARMING ATTACK: On Hit w/ Wpn: Add 1d6 to damage, target must make\n     : STR Saving Throw or drops held object of your choice to feet",
                    "DISTRACTING STRIKE: On Hit w/ Wpn: Add 1d6 to damage, and next attack\n     : on same target by ally before next turn has ADV",
                    "EVASIVE FOOTWORK: When moving, add 1d6 to your AC until you stop moving",
                    "FEINTING ATTACK: [Bonus]: Gain ADV on one target w/in 5ft of you for your\n     : next attack; add 1d6 to damage if successfull",
                    "GOADING ATTACK: On Hit w/ Wpn: Add 1d6 to damage, and target makes WIS\n     : Saving Throw or has DISADV: Attack against any creature\n     : besides you until the end of your next turn",
                    "LUNGING ATTACK: On [Att] w/ Melee Wpn: Extend reach by 5ft, and if hit\n     : add 1d6 to damage roll",
                    "MANEUVERING ATTACK: On Hit w/ Wpn: Add 1d6 to damage roll, and choose\n     : ally that can see hear/you; they can use [Reaction] to move\n     : up to 1/2 speed w/o provoking AoO from target",
                    "MENACING ATTACK: On Hit w/ Wpn: Add 1d6 to damage roll, and target must\n     : make WIS Save or be frightened of you until end of next turn",
                    "PARRY: On taking damage from Wpn: [Rxn]: Reduce damage by 1d6 + DEX ability_modifiers",
                    "PRECISION ATTACK: On [Att] w/ Wpn: Add 1d6 to attack roll\n     : (You may use this after the roll but before effect of attack are applied)",
                    "PUSHING ATTACK: On Hit w/ Wpn: Add 1d6 to damage roll, and target\n     : must make STR Save or be pushed up to 15ft away from you",
                    "RALLY: [Bonus]: Ally that can see/hear you gains temp hp = 1d6 + CHA ability_modifiers",
                    "RIPOSTE: When a creature misses you with a melee attack: [Reaction]: \n     : Make melee weapon attack, adding 1d6 to damage if hit",
                    "SWEEPING ATTACK: On Hit w/ Melee Wpn: Choose additional target w/in 5ft\n     : of original/within your reach, and if attack would also hit:\n     : that creature takes 1d6 damage",
                    "TRIP ATTACK: On Hit w/ Wpn: Add 1d6 to damage roll, and if target is\n     : Large or smaller, it makes STR Save or falls prone"
                    ]

        chosen_mnvr_1 = get_item(battle_maneuvers)
        chosen_mnvr_2 = get_item(battle_maneuvers)
        
        char_text1 = maneuver_text[battle_maneuvers.index(chosen_mnvr_1)]
        char_text2 = maneuver_text[battle_maneuvers.index(chosen_mnvr_2)]

        race_features.append(char_text1)
        race_features.append(char_text2)

        return "MARTIAL ADEPT"
    if chosen_feat == "MEDIUM ARMOR MASTER":

        race_features.append("MEDIUM ARMOR MASTER: No DISADV on Stealth in Med. Armor")
        race_features.append("     : You can add your DEX bonus up to +3 in Med. Armor")

        avail_feats.remove("MEDIUM ARMOR MASTER")
        return "MEDIUM ARMOR MASTER"
    if chosen_feat == "MOBILE":

        race_features.append("MOBILE: Speed increases by 10ft")
        race_features.append("      : On [Dash]: Difficult terrain doesn't cost extra movement")
        race_features.append("      : After [Attack], you don't take AoO from your target that turn")

        avail_feats.remove("MOBILE")
        return "MOBILE"
    if chosen_feat == "MODERATELY ARMORED":

        stat_bump("STRENGTH", "DEXTERITY")

        race_features.append("MODERATELY ARMORED: Gain prof: Medium Armor/Shields")
        race_features.append("*!* Must also be proficient with Light Armor to use this feat*!*")

        get_proficiency("MEDIUM", armor)
        get_proficiency("SHIELDS", armor)

        return "MODERATELY ARMORED"
    if chosen_feat == "MOUNTED COMBATANT":

        race_features.append("MOUNTED COMBATANT: While mounted and not incapacitated:")
        race_features.append("     : ADV: Melee Attack v. unmounted creature smaller than your mount")
        race_features.append("     : You can force an attack on your mount to target yourself instead")
        race_features.append("     : Your mount takes no damage when succeeds a DEX save that would")
        race_features.append("     : deal 1/2 damage, and only takes 1/2 if it fails the save")

        avail_feats.remove("MOUNTED COMBATANT")
        return "MOUNTED COMBATANT"
    if chosen_feat == "OBSERVANT":

        stat_bump("INTELLIGENCE", "WISDOM")

        skill_modifiers[("PERCEPTION")] += 5
        skill_modifiers[("INVESTIGATION")] += 5

        race_features.append("OBSERVANT: You can understand creatures by reading lips")
        race_features.append("         : +5 to Perception and Investigation checks")

        avail_feats.remove("OBSERVANT")
        return "OBSERVANT"
    if chosen_feat == "POLEARM MASTER":

        race_features.append("POLEARM MASTER: On [Attack] w/ Glaive, Halberd, or Quarterstaff:")
        race_features.append("     : [Bonus]: Melee Attack with opposite end for 1d4 Bludgeoning")
        race_features.append("     : While wielding Glaive / Halberd / Pike / Quarterstaff:")
        race_features.append("     : Creatures provoke AoO from you when they enter your reach")

        avail_feats.remove("POLEARM MASTER")
        return "POLEARM MASTER"
    if chosen_feat == "RESILIENT":

        chosen_stat = get_item(avail_attributes)

        ability_scores[(chosen_stat)] += 1
        
        get_proficiency("{0}".format(chosen_stat), saves)
        
        race_features.append("RESILIENT: Increase {0} by 1 and gain Prof: Saving Throws")

        avail_feats.remove("RESILIENT")
        return "RESILIENT"
    if chosen_feat == "RITUAL CASTER":

        while ability_scores[("INTELLIGENCE")] < 13 and ability_scores[("WISDOM")] < 13:
            avail_feats.remove("RITUAL CASTER")
            get_item(avail_feats)

        ritual_classes = [
                        "BARD",
                        "CLERIC",
                        "DRUID",
                        "SORCERER",
                        "WARLOCK",
                        "WIZARD"]
        bard_ritual = [
                        "COMPREHEND LANGUAGES",
                        "DETECT MAGIC",
                        "IDENTIFY",
                        "ILLUSORY SCRIPT",
                        "UNSEEN SERVANT",
                        ]
        cleric_ritual = [
                        "DETECT MAGIC",
                        "DETECT POISON AND DISEASE",
                        "PURIFY FOOD AND DRINK",
                        ]
        druid_ritual = [
                        "DETECT MAGIC",
                        "DETECT POISON AND DISEASE",
                        "PURIFY FOOD AND DRINK",
                        "SPEAK WITH ANIMALS",
                        ]
        sorc_ritual = [
                        "COMPREHEND LANGUAGES",
                        "DETECT MAGIC",
                        ]
        warlock_ritual = [
                        "COMPREHEND LANGUAGES",
                        "ILLUSORY SCRIPT",
                        "UNSEEN SERVANT",
                        ]
        wiz_ritual = [
                        "COMPREHEND LANGUAGES",
                        "DETECT MAGIC",
                        "FIND FAMILIAR",
                        "IDENTIFY",
                        "ILLUSORY SCRIPT",
                        "UNSEEN SERVANT",
                        ]

        if ability_scores["INTELLIGENCE"] < 13:
            ritual_classes.remove("WIZARD")
        if ability_scores["WISDOM"] < 13:
            ritual_classes.remove("CLERIC")
            ritual_classes.remove("DRUID")
        if ability_scores["CHARISMA"] < 13:
            ritual_classes.remove("BARD")
            ritual_classes.remove("SORCERER")
            ritual_classes.remove("WARLOCK")
        
        chosen_class = get_item(ritual_classes)

        if chosen_class == "BARD":
            get_spell("GET", bard_ritual, spellbook_1)
            get_spell("GET", bard_ritual, spellbook_1)
            spell_ability = "CHARISMA"
        
        if chosen_class == "CLERIC":
            get_spell("GET", cleric_ritual, spellbook_1)
            get_spell("GET", cleric_ritual, spellbook_1)
            spell_ability = "WISDOM"
        
        if chosen_class == "DRUID":
            get_spell("GET", druid_ritual, spellbook_1)
            get_spell("GET", druid_ritual, spellbook_1)
            spell_ability = "WISDOM"
        
        if chosen_class == "SORCERER":
            get_spell("GET", sorc_ritual, spellbook_1)
            get_spell("GET", sorc_ritual, spellbook_1)
            spell_ability = "CHARISMA"
        
        if chosen_class == "WARLOCK":
            get_spell("GET", warlock_ritual, spellbook_1)
            get_spell("GET", warlock_ritual, spellbook_1)
            spell_ability = "CHARISMA"
        
        if chosen_class == "WIZARD":
            get_spell("GET", wiz_ritual, spellbook_1)
            get_spell("GET", wiz_ritual, spellbook_1)
            spell_ability = "INTELLIGENCE"
        
        ritual_classes.remove(chosen_class)

        race_features.append("RITUAL CASTER: Gain a Ritual Book with two Level 1 Ritual spells")
        race_features.append("     : Class: {0} ; Spellcasting Ability: {1}".format(chosen_class, spell_ability))
        race_features.append("     : You can add ritual spells found in written form if they are")
        race_features.append("     : on your class' spell list and the level is <= 1/2 your level (rounded douwn)")
        race_features.append("     : Adding the spell takes 2hrs / spell level and costs 50g / spell level")

        return "RITUAL CASTER"
    if chosen_feat == "SAVAGE ATTACKER":

        race_features.append("SAVAGE ATTACKER: 1/turn when you roll damage for melee weapon:")
        race_features.append("     : Re-roll the weapon's damage dice and take use either total")

        avail_feats.remove("SAVAGE ATTACKER")
        return("SAVAGE ATTACKER")
    if chosen_feat == "SENTINEL":

        race_features.append("SENTINEL: When you hit on an AoO, your target's speed drops to 0 that turn.")
        race_features.append("        : You can ignore a creature's [Disengage] when it leaves your reach")
        race_features.append("        : When a creature w/in reach attacks something other than you:")
        race_features.append("        : [Reaction]: Melee weapon attack against that creature")

        avail_feats.remove("SENTINEL")
        return "SENTINEL"
    if chosen_feat == "SHARPSHOOTER":

        race_features.append("SHARPSHOOTER: Attacking at Long Range doesn't impose DISADV")
        race_features.append("     : Ranged Weapons ignore half- and three-quarters cover")
        race_features.append("     : Take -5 on Ranged Attack roll for +10 to damage roll")

        avail_feats.remove("SHARPSHOOTER")
        return "SHARPSHOOTER"
    if chosen_feat == "SHIELD MASTER":

        race_features.append("SHIELD MASTER: On [Att]: [Bonus]: Shove creature w/in 5ft")
        race_features.append("     : Add Shield's AC Bonus to DEX Saves while not incapicitated")
        race_features.append("     : against attacks targeting only you")
        race_features.append("     : [Reaction]: Turn DEX Save for 1/2 damage into No damage")

        avail_feats.remove("SHIELD MASTER")
        return "SHIELD MASTER"
    if chosen_feat == "SKILLED":

        def get_skilled():

            skill_or_tool = randint(1,2)

            if skill_or_tool == 1:
                get_skill(avail_skills)
            else:
                get_proficiency("GET", tools)
        
        get_skilled()
        get_skilled()
        get_skilled()

        return "SKILLED"
    if chosen_feat == "SKULKER":

        stat_required("SKULKER", "DEXTERITY", 13)

        race_features.append("SKULKER: [Hide] when lightly obscured from creature")
        race_features.append("       : Missed [Attack] from hiding doesn't reveal location")
        race_features.append("       : Dim light doesn't impose DISADV: Perception checks")

        avail_feats.remove("SKULKER")
        return "SKULKER"
    if chosen_feat == "SPELL SNIPER":

        #*!*You will need to be able to cast a spell (other than this cantrip) to use this feat*!*")
        
        race_features.append("SPELL SNIPER: Double the range of Spells with Attack rolls")
        race_features.append("     : Ranged Spell Attacks ignore half- and three-quarters cover")
        race_features.append("     : Gain Cantrip: Use Ability appropriate to Spellcasting Class")

        sniper_spells = [
                        "CHILL TOUCH",
                        "ELDRITCH BLAST",
                        "FIRE BOLT",
                        "PRODUCE FLAME",
                        "RAY OF FROST",
                        "SHOCKING GRASP",
                        "THORN WHIP"
                        ]
        get_spell("GET", sniper_spells, spellbook_0)

        avail_feats.remove("SPELL SNIPER")

        return "SPELL SNIPER"
    if chosen_feat == "TAVERN BRAWLER":

        stat_bump("STRENGTH", "CONSTITUTION")

        race_features.append("TAVERN BRAWLER: Prof: Unarmed Strikes / Improvised Wpns")
        race_features.append("     : Unarmed Strike = 1d4 damage")
        race_features.append("     : On Hit with U.S. / I.W.: [Bonus] attempt to Grapple")

        avail_feats.remove("TAVERN BRAWLER")
        return "TAVERN BRAWLER"
    if chosen_feat == "TOUGH":
        tough = True

        race_features.append("TOUGH: Hit Point Max increased by 2x Lvl, and wih every")
        race_features.append("     : level gained, it increased by an additional 2")

        avail_feats.remove("TOUGH")
        return "TOUGH"
    if chosen_feat == "WAR CASTER":

        #*!*You will need to be able to cast a spell to use this feat*!*")
        
        race_features.append("WAR CASTER: ADV: CON Saves to maintain Concentration through damage")
        race_features.append("     : Perform Somatic spell components whith Wpn/Shield equipped")
        race_features.append("     : Cast spell with Attack roll as AoO when creature leaves your reach")
        race_features.append("     : (Spell must have Casting Time: 1 action / target only that creature)")

        avail_feats.remove("WAR CASTER")
        return "WAR CASTER"
    if chosen_feat == "WEAPON MASTER":

        stat_bump("STRENGTH", "DEXTERITY")

        race_features.append("WEAPON MASTER: Gain Prof: 4 additional weapons")

        def master_weapon():

            weapon_types = ["SIMPLE", "MARTIAL"]
            chosen_type = get_item(weapon_types)

            if chosen_type == "SIMPLE":
                get_proficiency("GET", simple_wpns)
            if chosen_type == "MARTIAL":
                get_proficiency("GET", martial_wpns)

        master_weapon()
        master_weapon()
        master_weapon()
        master_weapon()

        avail_feats.remove("WEAPON MASTER")
        return "WEAPON MASTER"
 
def get_spell(name, from_list, to_spellbook):
    
        if name == "GET":
            name = get_item(from_list)
        
        to_spellbook.append(name)
        from_list.remove(name)

        return name

def roll_attribute():

    roll = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    roll = sorted(roll)                         

    score = roll[1] + roll[2] + roll[3]
    return score

def update_mods():
    #   If the modifer has a half, take off the half
    for key in ability_modifiers:
        ability_modifiers[key] = (ability_scores[key] - 10) / 2

        mod = str(abs(ability_modifiers[key]))    
        if mod[2] == ("5"):         
            ability_modifiers[key] += -0.5        

        ability_modifiers[key] = int(ability_modifiers[key])

#   Roll 4d6 and drop the lowest for each ability score
for score in ability_scores:
    ability_scores[score] = roll_attribute()

#   These variables will affect hit point totals if set to True
#   tough will be set to True if the feat "Tough" is chosen
#   hill_dwarf will be set to True if that Dwarven Subrace is chosen
tough = False
hill_dwarf = False

race = [
        "HUMAN",
        "ELF",
        "DWARF",
        "HALFLING",
        "HALF-ELF",
        "HALF-ORC",
        "TIEFLING",
        "DRAGONBORN",
        "GNOME",
        "AARAKOCRA",
        "GENASI",
        "GOLIATH",
        "AASIMAR",
        "FIRBOLG",
        "KENKU",
        "LIZARDFOLK",
        "TABAXI",
        "TRITON",
        "BUGBEAR",
        "GOBLIN",
        "HOBGOBLIN",
        "KOBOLD",
        "ORC",
        "YUAN-TI PUREBLOOD",
        "GITH"
        ]
def get_race():

    def get_age(low, young, old, high):
        
        
        char_age = randint(low, high)

        if char_age <= young:               
            how_old = "Young Adult"         
        elif char_age <= old:               
            how_old = "Adult"               
        else:
            how_old = "Middle-aged"

        race_features.append("AGE: {0} ({1})".format(char_age, how_old))
        race_features.append("")

    def get_size(height_mod, base_height, weight_mod, base_weight):
        
        roll_height = randint(2,height_mod)                  
        roll_weight = randint(2,weight_mod)                  
                                                    
        char_height = (roll_height + base_height)
        char_weight = ((roll_height * roll_weight) + base_weight)

        height_feet = char_height // 12
        height_inches = char_height % 12

        race_features.append("HEIGHT: {0}' {1}\"".format(height_feet, height_inches))
        race_features.append("WEIGHT: {0} lbs".format(char_weight))
        race_features.append("")
    
    def get_random_alignment():

        roll_alignment = randint(1,100)
        if roll_alignment < 6:
            char_align = "CHAOTIC EVIL"
        elif roll_alignment < 12:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 20:
            char_align = "LAWFUL EVIL"
        elif roll_alignment < 30:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 45:
            char_align = "TRUE NEUTRAL"
        elif roll_alignment < 60:
            char_align = "LAWFUL NEUTRAL"
        elif roll_alignment < 75:
            char_align = "CHAOTIC GOOD"
        elif roll_alignment < 90:
            char_align = "NEUTRAL GOOD"
        else:
            char_align = "LAWFUL GOOD"
        
        race_features.append(char_align)
        race_features.append("")

    def get_underdark_alignment():

        roll_alignment = randint(1,100)
        if roll_alignment < 40:
            char_align = "CHAOTIC EVIL"
        if roll_alignment < 60:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 80:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 90:
            char_align = "LAWFUL EVIL"
        else:
            char_align = "TRUE NEUTRAL"
        race_features.append(char_align)
        race_features.append("")

    def get_speed(feet):

        feet_per_round = "SPEED: {0}ft".format(feet)
        race_features.append(feet_per_round)
        race_features.append("")

        return feet

    def get_darkvision(feet):

        feet = "DARKVISION: {0}ft".format(feet)
        race_features.append(feet)
        race_features.append("")

        return feet

    def raise_stat_by(amount):
                                    
        chosen_attribute = get_item(avail_attributes)
        
        ability_scores[(chosen_attribute)] += amount
        avail_attributes.remove(chosen_attribute)
        
        return chosen_attribute

    def get_monstrous_origin():

        monstrous_origins = [
            "You are a spy sent to undermine from within.",
            "You are the victim of a curse/polymorph spell",
            "You were raised by Humans/Elves/Dwarves and adopted their culture.",
            "You adopted a human religion and serve it fervently.",
            "You received divine insight that led you from your home.",
            "You lost your home to a great monster/evil force.",
            "You seek to prevent your home from great tragedy.",
            "You have only brief flashes of memory of your past."
            ]
        char_mon_origin = get_item(monstrous_origins)
        char_mon_origin = "MONSTROUS ORIGIN: {0}".format(char_mon_origin)
        race_features.append(char_mon_origin)
        race_features.append("")

        return char_mon_origin

    chosen_race = get_item(race)
    
    if chosen_race == "HUMAN":

        race_features.append(chosen_race)
        race_features.append("")
        
        get_age(15, 25, 45, 60)
        get_size(20, 56, 8, 110)

        get_random_alignment()
        
        get_proficiency("GET", languages)

        get_speed(30)
        
        variant = randint(1,2)
        if variant == 1:
            for key in ability_scores:
                ability_scores[key] += 1
        if variant == 2:
            chosen_stat_1 = raise_stat_by(1)
            chosen_stat_2 = raise_stat_by(1)
            # Function removes chosen stats from list, so:
            avail_attributes.append(chosen_stat_1)
            avail_attributes.append(chosen_stat_2)
            
            get_skill(avail_skills)
            
            get_feat()

    if chosen_race == "DWARF":

        dw_subrace = ["HILL DWARF", "MOUNTAIN DWARF", "DUERGAR"]
        chosen_race = get_item(dw_subrace)
        
        race_features.append(chosen_race)
        race_features.append("")
        
        get_age(35, 50, 150, 200)
        get_size(8, 46, 12, 125)

        ability_scores["CONSTITUTION"] += 2

        dwarf_tools = ["SMITH'S TOOLS", "BREWER'S SUPPLIES", "MASON'S TOOLS"]
        get_proficiency("GET", dwarf_tools)
        get_proficiency("DWARVEN", languages)
        
        if chosen_race == "HILL DWARF":

            ability_scores["WISDOM"] += 1

            get_random_alignment()
            
            get_darkvision(60)
            
            race_features.append("HILL-BRED: +1 Hit Point per level")
            hill_dwarf = True

        if chosen_race == "MOUNTAIN DWARF":

            ability_scores["STRENGTH"] += 1

            get_random_alignment()

            get_darkvision(60)

            get_proficiency("MEDIUM", armor)
            get_proficiency("BATTLEAXE", martial_wpns)
            get_proficiency("WARHAMMER", martial_wpns)
            get_proficiency("HANDAXE", simple_wpns)
            get_proficiency("LIGHT HAMMER", simple_wpns)

        if chosen_race == "DUERGAR":

            ability_scores[("STRENGTH")] += 1

            get_underdark_alignment()
            
            get_darkvision(120)

            get_proficiency("UNDERCOMMON", languages)

            race_features.append("ADV: Saving Throws v. Illusions / Charm / Paralysis")
            race_features.append("DISADV: Attack / Perception Rolls in direct sunlight")
        
        get_speed(25)

        race_features.append("ADV: Saving Throws v. Poison")
        race_features.append("RES: Poison Damage")
        race_features.append("")
        race_features.append("2x Prof on History Checks re: Stonework")
        race_features.append("")

    if chosen_race == "ELF":

        def get_elven_weapons():
            get_proficiency("LONGSWORD", martial_wpns)
            get_proficiency("LONGBOW", martial_wpns)
            get_proficiency("SHORT SWORD", martial_wpns)
            get_proficiency("SHORT BOW", simple_wpns)

        elf_subrace = ["HIGH ELF", "WOOD ELF", "DROW"]
        chosen_race = get_item(elf_subrace)
        race_features.append(chosen_race)
        race_features.append("")

        get_age(80, 125, 325, 400)
        get_size(16, 54, 5, 90)
        
        ability_scores["DEXTERITY"] += 2
        
        skill_modifiers["PERCEPTION"] += 2

        get_proficiency("ELVEN", languages)

        get_speed(30)
        
        race_features.append("ADV : Saving Throws v. Charm")
        race_features.append("4 hrs Meditative 'Trance' = 8 hrs Sleep")
        race_features.append("IMMUNE : Magical Sleep")

        if chosen_race == "HIGH ELF":

            get_random_alignment()
        
            ability_scores["INTELLIGENCE"] += 1

            get_darkvision(60)
        
            cantrip_class = [
                            "BARD",
                            "CLERIC",
                            "DRUID",
                            "SORCERER",
                            "WARLOCK",
                            "WIZARD"
                            ]
            chosen_cantrip = get_item(cantrip_class)
            if chosen_cantrip == "BARD":
                get_spell("GET", bard_spell_0, spellbook_0)
            if chosen_cantrip == "CLERIC":
                get_spell("GET", cleric_spell_0, spellbook_0)
            if chosen_cantrip == "DRUID":
                get_spell("GET", druid_spell_0, spellbook_0)
            if chosen_cantrip == "SORCERER":
                get_spell("GET", sorc_spell_0, spellbook_0)
            if chosen_cantrip == "WARLOCK":
                get_spell("GET", warlock_spell_0, spellbook_0)
            if chosen_cantrip == "WIZARD":
                get_spell("GET", wiz_spell_0, spellbook_0)

            elven_cantrip = spellbook_0[(len(spellbook_0) -1)]
            race_features.append("ELVEN MAGIC: Gain 1 Cantrip: {0} (INT spell ability)".format(elven_cantrip))
            race_features.append("")

            get_elven_weapons()
            get_proficiency("GET", languages)

        if chosen_race == "WOOD ELF":

            get_random_alignment()

            get_elven_weapons()

            get_darkvision(60)
            
            race_features.append("MASK OF THE WILD: Can [Hide] in Lightly Obscuring Nature")
        
        if chosen_race == "DROW":

            get_underdark_alignment()
            
            ability_scores["CHARISMA"] += 1

            get_proficiency("RAPIER", martial_wpns)
            get_proficiency("HAND XBOW", martial_wpns)
            get_proficiency("UNDERCOMMON", languages)

            get_darkvision(120)

            race_features.append("DISADV: Attack / Perception (Sight) in Direct Sunlight")
            race_features.append("Gain Cantrip: Dancing Lights")

            spellbook_0.append("DANCING LIGHTS (Drow)")

    if chosen_race == "HALFLING":

        halfling_subrace = ["LIGHTFOOT HALFLING", "STOUT HALFLING"]
        chosen_race = get_item(halfling_subrace)
        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 75, 150)
        get_size(8, 31, 8, 35)

        get_random_alignment()
        
        get_speed(25)
        
        race_features.append("LUCKY: Reroll 1's on Attack / Ability / Saves")
        race_features.append("ADV: Saving Throws v. Frightened")
        race_features.append("")
        race_features.append("NIMBLE: Move through space occupied by larger creature")
        race_features.append("")
        
        ability_scores["DEXTERITY"] += 2

        get_proficiency("HALFLING", languages)

        if chosen_race == "LIGHTFOOT HALFLING":

            ability_scores["CHARISMA"] += 1

            race_features.append("Can [Hide] when obscured by larger creature")
            race_features.append("")
            
        if chosen_race == "STOUT HALFLING":

            ability_scores["CONSTITUTION"] += 1

            race_features.append("ADV: Saving Throws v. Poison")
            race_features.append("RES: Poison Damage")
            race_features.append("")

    if chosen_race == "DRAGONBORN":

        drac_ancestry = [
                        "BLACK",
                        "BLUE",
                        "BRASS",
                        "BRONZE",
                        "COPPER",
                        "GOLD",
                        "GREEN",
                        "RED",
                        "SILVER",
                        "WHITE"
                        ]
        ancestry = get_item(drac_ancestry)
        chosen_race = "{0} DRAGONBORN".format(ancestry)
        
        race_features.append(chosen_race)
        race_features.append("")

        get_age(10, 20, 40, 50)
        get_size(16, 66, 12, 175)

        get_random_alignment()
        
        get_proficiency("DRACONIC", languages)

        ability_scores["STRENGTH"] += 2
        ability_scores["CHARISMA"] += 1
        update_mods()

        get_speed(30)
        
        breath_save_DC = ability_modifiers["CONSTITUTION"] + 10
        breath_save = {
                        "BLACK" : "DEX",
                        "BLUE" : "DEX",
                        "BRASS" : "DEX",
                        "BRONZE" : "DEX",
                        "COPPER" : "DEX",
                        "GOLD" : "DEX",
                        "GREEN" : "CON",
                        "RED" : "DEX",
                        "SILVER" : "CON",
                        "WHITE" : "CON"
                        }
        breath_damage = {
                        "BLACK" : "Acid",
                        "BLUE" : "Lightning",
                        "BRASS" : "Fire",
                        "BRONZE" : "Lightning",
                        "COPPER" : "Acid",
                        "GOLD" : "Fire",
                        "GREEN" : "Poison",
                        "RED" : "Fire",
                        "SILVER" : "Cold",
                        "WHITE" : "Cold"
                        }
        breath_effect = {
                        "BLACK" : "5 x 30ft line",
                        "BLUE" : "5 x 30ft line",
                        "BRASS" : "5 x 30ft line",
                        "BRONZE" : "5 x 30ft line",
                        "COPPER" : "5 x 30ft line",
                        "GOLD" : "15ft Cone",
                        "GREEN" : "15ft Cone",
                        "RED" : "15ft Cone",
                        "SILVER" : "15ft Cone",
                        "WHITE" : "15ft Cone"
                        }
        
        race_features.append("BREATH WEAPON (1/LR): 2d6 dmg; DC {0} (8+CON+Prof) for 1/2".format(breath_save_DC))
        race_features.append("BREATH WEAPON EFFECT: {0} {1} Damage ({2} Save)".format(breath_effect[ancestry], breath_damage[ancestry], breath_save[ancestry]))
        race_features.append("")
        race_features.append("RES: {0} Damage".format(breath_damage[ancestry]))
        race_features.append("")
        
    if chosen_race == "GNOME":

        gnome_subrace = ["FOREST GNOME", "ROCK GNOME", "DEEP GNOME"]
        chosen_race = get_item(gnome_subrace)
        race_features.append(chosen_race)
        race_features.append("")

        get_age(20, 40, 140, 200)
        get_size(8, 35, 8, 35)
        
        ability_scores["INTELLIGENCE"] += 2

        get_proficiency("GNOMISH", languages)

        get_speed(25)
        
        race_features.append("ADV: INT/WIS/CHA Saves v. Magic")
        race_features.append("")
        
        if chosen_race == "FOREST GNOME":

            get_random_alignment()
            
            get_darkvision(60)
            
            ability_scores["DEXTERITY"] += 1

            spellbook_0.append("MINOR ILLUSION (Gnome)")

            race_features.append("Gain 'Minor Illusion' Cantrip (INT Spellcasting Ability)")
            race_features.append("")
            race_features.append("Can communicate simple ideas with Small or smaller beasts")
            race_features.append("")
            
        if chosen_race == "ROCK GNOME":

            get_random_alignment()
            
            get_darkvision(60)
            
            ability_scores["CONSTITUTION"] += 1

            get_proficiency("TINKER'S TOOLS", tools)
            
            race_features.append("(2x PROF): INT(History) Checks v. Magical / Alchemical / Technical Objects")
            race_features.append("")
            race_features.append("TINKERER: Spend 1hr / 10gp of material to make Tiny clockwork device")
            race_features.append("TINKER TOY: Clockwork Toy: Animal/Monster/Person; moves 5ft random direction per turn")
            race_features.append("          : Firestarter: produces miniature flame")
            race_features.append("          : Music Box: single song, moderate volume")
            race_features.append("")
            
        if chosen_race == "DEEP GNOME":

            get_underdark_alignment()
            
            get_darkvision(120)
            
            ability_scores[("DEXTERITY")] += 1

            race_features.append("ADV: DEX (Stealth) Checks in Rocky Terrain")
            race_features.append("")
            
            get_proficiency("UNDERCOMMON", languages)

    if chosen_race == "HALF-ELF":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 70, 100)
        get_size(16, 57, 8, 110)

        get_random_alignment()
        
        ability_scores["CHARISMA"] += 2
        avail_attributes.remove("CHARISMA")
        
        halfelf_stat_1 = raise_stat_by(1)
        halfelf_stat_2 = raise_stat_by(1)
        
        avail_attributes.append("CHARISMA")
        avail_attributes.append(halfelf_stat_1)
        avail_attributes.append(halfelf_stat_2)

        get_proficiency("ELVEN", languages)
        get_proficiency("GET", languages)

        get_speed(30)
        get_darkvision(60)

        race_features.append("ADV: Saving Throws v. Charm")
        race_features.append("IMMUNE: Magical Sleep")
        race_features.append("")

    if chosen_race == "HALF-ORC":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(10, 15, 35, 45)
        get_size(20, 58, 12, 140)

        get_random_alignment()
        
        ability_scores["STRENGTH"] += 2
        ability_scores["CONSTITUTION"] += 1

        get_proficiency("ORC", languages)

        skill_modifiers["INTIMIDATION"] += 2

        get_speed(30)
        get_darkvision(60)

        race_features.append("When reduced to 0 HP but not killed, drop to 1 HP instead (1/LR)")
        race_features.append("")
        race_features.append("On a critical hit with a melee weapon, add 1 damage die to roll")
        race_features.append("")

    if chosen_race == "TIEFLING":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 60, 75)
        get_size(16, 57, 8, 110)

        get_random_alignment()
        
        ability_scores["CHARISMA"] += 2
        ability_scores["INTELLIGENCE"] += 1

        get_proficiency("INFERNAL", languages)

        get_speed(30)
        get_darkvision(60)

        race_features.append("RES: Fire Damage")
        race_features.append("Gain 'Thaumaturgy' Cantrip")
        race_features.append("")

        spellbook_0.append("THAUMATURGY (Tiefling)")

    if chosen_race == "AARAKOCRA":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(2, 5, 20, 25)
        get_size(12, 54, 22, 78)

        get_random_alignment()
        
        ability_scores["DEXTERITY"] += 2
        ability_scores["WISDOM"] += 1

        get_speed(25)

        race_features.append("FLY SPEED: 50ft (No Medium or Heavy Armor)")
        race_features.append("")
        race_features.append("TALONS: Unarmed Strike deals 1d4 Slashing damage")
        race_features.append("")
            
        get_proficiency("UNARMED", simple_wpns)
        get_proficiency("AARAKOCRAN", languages)
        get_proficiency("AURAN", languages)

    if chosen_race == "GENASI":

        genasi_elements = ["FIRE", "EARTH", "WATER", "AIR"]
        chosen_genasi = get_item(genasi_elements)
        chosen_race = "{0} GENASI".format(chosen_genasi)
        
        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 60, 80)
        get_size(20, 56, 8, 110)

        get_random_alignment()
        
        ability_scores[("CONSTITUTION")] += 2

        get_speed(30)
        
        get_proficiency("PRIMORDIAL", languages)

        if chosen_race == "AIR GENASI":

            ability_scores[("DEXTERITY")] += 1

            race_features.append("You can hold your breath indefinitely.")
            race_features.append("")
            race_features.append("1/LR: Cast LEVITATE (CON Spell Ability)")
            race_features.append("")
            
        if chosen_race == "EARTH GENASI":

            ability_scores["STRENGTH"] += 1

            race_features.append("You move across natural difficult terrain as normal.")
            race_features.append("")
            race_features.append("1/LR: Cast PASS WITHOUT TRACE")
            race_features.append("")
            
        if chosen_race == "FIRE GENASI":

            ability_scores[("INTELLIGENCE")] += 1

            get_darkvision(60)

            race_features.append("RES: Fire Damage")
            race_features.append("")
            race_features.append("Gain Cantrip 'Produce Flame'")
            race_features.append("")
            
            spellbook_0.append("PRODUCE FLAME (Genasi)")
        
        if chosen_race == "WATER GENASI":

            ability_scores[("WISDOM")] += 1

            race_features.append("SWIM SPEED: 30ft")
            race_features.append("")
            race_features.append("RES: Acid Damage")
            race_features.append("")
            race_features.append("AMBPHIBIOUS: Breathe air and water")
            race_features.append("")
            race_features.append("Gain Cantrip 'Shape Water'")
            race_features.append("")
            

            spellbook_0.append("SHAPE WATER (Genasi)")

    if chosen_race == "GOLIATH":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 45, 60)
        get_size(16, 82, 12, 235)

        get_random_alignment()
        
        ability_scores[("STRENGTH")] += 2
        ability_scores[("CONSTITUTION")] += 1
        update_mods()

        skill_modifiers[("ATHLETICS")] += 2

        get_speed(30)
        
        race_features.append("[R] (1/SR): When you take damage, reduce by 1d12+{0} (CON)".format(ability_modifiers["CONSTITUTION"]))
        race_features.append("")
        race_features.append("Count as one size larger when determining carry/push/drag/lift loads")
        race_features.append("")
        race_features.append("Naturally acclimated to high altitudes / cold climates")
        race_features.append("")
            
        get_proficiency("GIANT", languages)

    if chosen_race == "AASIMAR":

        aasm_subrace = ["PROTECTOR AASIMAR", "SCOURGE AASIMAR", "FALLEN AASIMAR"]
        chosen_race = get_item(aasm_subrace)
        race_features.append(chosen_race)
        race_features.append("")
        
        get_age(15, 25, 80, 160)
        get_size(20, 56, 8, 110)

        get_random_alignment()
        
        ability_scores["CHARISMA"] += 2
        
        get_proficiency("CELESTIAL", languages)

        get_speed(30)
        get_darkvision(60)
        race_features.append("RES: Necrotic / Radiant Damage")
        race_features.append("1/LR: Touch creature, gains your level in HP")
        race_features.append("Gain 'Light' Cantrip")
        race_features.append("")

        angels = ["TADRIEL", "MYLLANDRA", "SERAPHINA", "GALLADIA", "MYKIEL", "VALANDRAS"]
        ang_guide = get_item(angels)
        ang_guide = "ANGELIC GUIDE: {0}".format(ang_guide)
        
        angel_natures = [
            "BOOKISH / LECTURING", 
            "COMPASSIONATE / HOPEFUL", 
            "PRACTICAL / LIGHTHEARTED", 
            "FIERCE / VENGEFUL", 
            "STERN / JUDGEMENTAL", 
            "KIND / PARENTAL"]
        ang_nature = get_item(angel_natures)
        ang_nature = "GUIDE'S TEMPERAMENT: {0}".format(ang_nature)
        
        race_features.append(ang_guide)
        race_features.append(ang_nature)
        race_features.append("")

        spellbook_0.append("LIGHT (Aasimar)")

        if chosen_race == "PROTECTOR AASIMAR":
            ability_scores["WISDOM"] += 1
        if chosen_race == "SCOURGE AASIMAR":
            ability_scores["CONSTITUTION"] += 1
        if chosen_race == "FALLEN AASIMAR":
            ability_scores["STRENGTH"]+= 1
    
    if chosen_race == "FIRBOLG":

        firbolg_origins = [
            "OUTCAST FOR MURDER",
            "OUTCAST FOR ENDANGERING HOME",
            "CLAN SLAIN BY HUMANOIDS",
            "CLAN SLAIN BY DEMON / DRAGON",
            "SEPARATED FROM TRIBE / LOST",
            "HOME DESTROYED BY NATURAL DISASTER",
            "PERSONAL QUEST ORDAINED BY OMENS",
            "DISPATCHED ON QUEST BY TRIBAL ELDERS"
            ]
        chosen_origin = get_item(firbolg_origins)
        
        race_features.append(chosen_race)
        race_features.append("")
        race_features.append("ORIGIN: {0}".format(chosen_origin))
        race_features.append("")

        ability_scores["WISDOM"] += 2
        ability_scores["STRENGTH"] += 1

        get_age(15, 30, 250, 400)
        get_size(24, 74, 12, 175)

        roll_alignment = randint(1,100)
        if roll_alignment < 75:
            char_align = "NEUTRAL GOOD"
        elif roll_alignment < 80:
            char_align = "LAWFUL GOOD"
        elif roll_alignment < 85:
            char_align = "CHAOTIC GOOD"
        elif roll_alignment < 90:
            char_align = "LAWFUL NEUTRAL"
        elif roll_alignment < 93:
            char_align = "TRUE NEUTRAL"
        elif roll_alignment < 96:
            char_align = "CHAOTIC NEUTRAL"
        else:
            char_align = "NEUTRAL EVIL"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        race_features.append("[B]: 1/SR Cast either 'Detect Magic' or 'Disguise Self'")
        race_features.append("     'Disguise Self' allows you to seem up to 3ft shorter,")
        race_features.append("     So as to blend in with Human-sized crowds")
        race_features.append("[B]: 1/SR Turn Invisible until you attack, roll damage, or force a save")
        race_features.append("POWERFUL BUILD: Count 1 size larger for push/drag/lift thresholds")
        race_features.append("ADV: Charisma checks to influence animals and plants")
        race_features.append("")

        get_proficiency("ELVISH", languages)
        get_proficiency("GIANT", languages)

    if chosen_race == "KENKU":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(12, 18, 30, 45)
        get_size(16, 52, 6, 50)

        roll_alignment = randint(1,100)
        if roll_alignment < 75:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 85:
            char_align = "CHAOTIC GOOD"
        elif roll_alignment < 95:
            char_align = "NEUTRAL EVIL"
        else:
            char_align = "CHAOTIC EVIL"
        race_features.append(char_align)
        race_features.append("")

        ability_scores["DEXTERITY"] += 2
        ability_scores["WISDOM"] += 1

        get_speed(30)
        race_features.append("ADV: Checks to create forgeries or duplicates")
        race_features.append("MIMICRY: Recreate any sound you have heard, including voices")
        race_features.append("         Insight Check v. your Deception Check to identify imitation")
        race_features.append("         This is a kenku's only form of speech")

        kenku_skills = ["ACROBATICS", "DECEPTION", "STEALTH", "SLEIGHT OF HAND"]
        get_skill(kenku_skills)
        get_skill(kenku_skills)
        get_proficiency("AURAN", languages)

    if chosen_race == "LIZARDFOLK":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(14, 20, 30, 45)
        get_size(20, 57, 12, 120)

        lizfolk_quirks = [
            "You hate waste and scavenge every piece of every enemy.",
            "You don't sleep well if not partially submerged in water.",
            "The concept of money makes no sense whatsoever to you.",
            "There are two species of humanoid: lizardfolk, and meat.",
            "You learned to laugh, but do not understand when to do it.",
            "You don't understand metaphors, but insist on using them.",
            "You see other humanoids as soft and weak. It's cute when they try.",
            "Your favorite foods try to wriggle out of your mouth mid-meal."
            ]
        liz_quirk = get_item(lizfolk_quirks)
        race_features.append("LIZARDFOLK QUIRK: {0}".format(liz_quirk))
        race_features.append("")

        ability_scores["CONSTITUTION"] += 2
        ability_scores["WISDOM"] += 1
        update_mods()

        roll_alignment = randint(1,100)
        if roll_alignment < 80:
            char_align = "TRUE NEUTRAL"
        elif roll_alignment < 85:
            char_align = "LAWFUL NEUTRAL"
        elif roll_alignment < 90:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 95:
            char_align = "NEUTRAL GOOD"
        else:
            char_align = "NEUTRAL EVIL"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        race_features.append("BITE: Unarmed Strike: 1d6+{0} Piercing (STR)".format(ability_modifiers["STRENGTH"]))
        race_features.append("      1/SR: [B] Make Bite attack, gain {0} Temp HP (CON)".format(ability_modifiers["CONSTITUTION"]))
        race_features.append("NATURAL ARMOR: AC = {0} (13+DEX) without armor on".format(ability_modifiers["DEXTERITY"] + 13))
        race_features.append("You can hold your breath up to 15 minutes at a time.")
        race_features.append("")

        lizfolk_skills = ["ANIMAL HANDLING", "NATURE", "PERCEPTION", "STEALTH", "SURVIVAL"]
        for i in range(2):
            get_skill(lizfolk_skills)
    
        get_proficiency("DRACONIC", languages)        

    if chosen_race == "TABAXI":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 35, 45)
        get_size(20, 58, 8, 90)

        tabaxi_obsessions = [
            "A GOD / PLANAR ENTITY",
            "A MONSTER",
            "A LOST CIVILIZATION",
            "A WIZARD'S SECRETS",
            "A MUNDANE ITEM",
            "A MAGIC ITEM",
            "A LOCATION",
            "A LEGEND / TALE"
            ]
        obsession = get_item(tabaxi_obsessions)
        obsession = "TABAXI OBSESSION: {0}".format(obsession)
        
        tabaxi_quirks = [
            "You complain endlessly about how you miss your tropical homeland.",
            "You never wear the same outfit twice.",
            "You have a minor phobia of water / getting wet.",
            "Your tail always betrays your inner thoughts.",
            "You purr loudly when happy."
            "You have a small ball of yarn you constantly fidget with."
            "You constantly spend money on lavish parties and gifts for friends.",
            "You become unintelligible when you get excited about something.",
            "You are a font of random bits of trivia and lore.",
            "You can't help but pocket random items you come across."
            ]
        tab_quirk = get_item(tabaxi_quirks)
        tab_quirk = "TABAXI QUIRK: {0}".format(tab_quirk)       
        
        race_features.append(obsession)
        race_features.append(tab_quirk)
        race_features.append("")

        ability_scores["DEXTERITY"] += 2
        ability_scores["CHARISMA"] += 1
        update_mods()

        roll_alignment = randint(1,100)
        if roll_alignment < 40:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 80:
            char_align = "CHAOTIC GOOD"
        elif roll_alignment < 90:
            char_align = "NEUTRAL GOOD"
        elif roll_alignment < 95:
            char_align = "CHAOTIC EVIL"
        else:
            char_align = "NEUTRAL EVIL"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        race_features.append("DARKVISION: 60ft")
        race_features.append("Move 2x Speed: Must go 0ft in a round before re-using ability")
        race_features.append("CLIMBING SPEED: 20ft")
        race_features.append("CLAWS: Unarmed Strike: 1d4+{0} Slashing (STR)".format(ability_modifiers["STRENGTH"]))

        skill_modifiers["PERCEPTION"] += 2
        skill_modifiers["STEALTH"] += 2

        get_proficiency("GET", languages)

    if chosen_race == "TRITON":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 30, 100, 160)
        get_size(20, 54, 8, 90)

        triton_quirks = [
            "You don't make requests. You give orders.",
            "You boast often of the greatness of your people.",
            "You learned an antiquated version of Common.",
            "You take things said and done at face value.",
            "You are obsessed with cataloguing the entire surface world.",
            "You assume all surface dwellers know and fear Tritons."
            ]
        tri_quirk = get_item(triton_quirks)
        race_features.append("TRITON QUIRK: {0}".format(tri_quirk))
        race_features.append("")

        ability_scores["STRENGTH"] += 1
        ability_scores["CONSTITUTION"] += 1
        ability_scores["CHARISMA"] += 1

        roll_alignment = randint(1,100)
        if roll_alignment < 75:
            char_align = "LAWFUL GOOD"
        elif roll_alignment < 85:
            char_align = "NEUTRAL GOOD"
        elif roll_alignment < 95:
            char_align = "LAWFUL NEUTRAL"
        elif roll_alignment < 98:
            char_align = "CHAOTIC GOOD"
        else:
            char_align = "LAWFUL EVIL"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        race_features.append("SWIM SPEED: 30ft")
        race_features.append("AMPHIBIOUS: Breathe air and water")
        race_features.append("1/LR: Cast 'Fog Cloud' (CHA spellcasting)")
        race_features.append("Communicate simple ideas with water beasts")
        race_features.append("RES: Cold Damage")
        
        get_proficiency("PRIMORDIAL", languages)

        spellbook_1.append("FOG CLOUD (Genasi)")

    if chosen_race == "BUGBEAR":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(16, 23, 40, 65)
        get_size(24, 72, 12, 200)

        get_monstrous_origin()
        
        ability_scores["STRENGTH"] += 2
        ability_scores["DEXTERITY"] += 1

        roll_alignment = randint(1,100)
        if roll_alignment < 75:
            char_align = "CHAOTIC EVIL"
        elif roll_alignment < 85:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 95:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 98:
            char_align = "TRUE NEUTRAL"
        else:
            char_align = "CHAOTIC GOOD"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        get_darkvision(60)
        
        race_features.append("LONG-LIMBED: +5ft reach to Melee attack on your turn")
        race_features.append("Count as one size larger for push/pull/drag thresholds")
        race_features.append("SURPRISE ATTACK: +2d6 damage to hit made on surprised creature")
        race_features.append("               : on first turn in combat. Usable 1/Combat")
        race_features.append("")

        skill_modifiers["STEALTH"] += 2
        
        get_proficiency("GOBLIN", languages)

    if chosen_race == "GOBLIN":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(8, 15, 30, 45)
        get_size(8, 41, 2, 35)

        get_monstrous_origin()

        roll_alignment = randint(1,100)
        if roll_alignment < 85:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 90:
            char_align = "TRUE NEUTRAL"
        elif roll_alignment < 95:
            char_align = "CHAOTIC EVIL"
        elif roll_alignment < 98:
            char_align = "CHAOTIC NEUTRAL"
        else:
            char_align = "NEUTRAL GOOD"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        race_features.append("DARKVISION: 60ft")
        race_features.append("1/SR: On damaging creature larger than you,")
        race_features.append("      Deal extra damage equal to your level")
        race_features.append("[B]: Disengage / Hide")

        get_proficiency("GOBLIN", languages)

    if chosen_race == "HOBGOBLIN":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 45, 60)
        get_size(20, 56, 8, 110)

        get_monstrous_origin()

        ability_scores["CONSTITUTION"] += 2
        ability_scores["INTELLIGENCE"] += 1

        roll_alignment = randint(1,100)
        if roll_alignment < 85:
            char_align = "LAWFUL EVIL"
        elif roll_alignment < 90:
            char_align = "LAWFUL NEUTRAL"
        elif roll_alignment < 95:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 98:
            char_align = "TRUE NEUTRAL"
        else:
            char_align = "LAWFUL GOOD"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        race_features.append("DARKVISION: 60ft")
        race_features.append("1/SR: Gain bonus on failed attack/ability/save")
        race_features.append("      equal to allies seen w/in 30ft (max +5)")

    if chosen_race == "KOBOLD":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(6, 20, 60, 90)
        get_size(8, 25, 2, 25)
        
        get_monstrous_origin()

        roll_alignment = randint(1,100)
        if roll_alignment < 55:
            char_align = "LAWFUL EVIL"
        elif roll_alignment < 75:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 95:
            char_align = "LAWFUL NEUTRAL"
        elif roll_alignment < 98:
            char_align = "TRUE NEUTRAL"
        else:
            char_align = "LAWFUL GOOD"
        race_features.append(char_align)
        race_features.append("")

        ability_scores["DEXTERITY"] += 2
        ability_scores["STRENGTH"] += 1

        get_speed(30)
        race_features.append("DARKVISION: 60ft")
        race_features.append("1/SR: Cower/Grovel/Beg to distract enemies,")
        race_features.append("    giving allies ADV v. enemies w/in 10ft of you")
        race_features.append("    until the end of your next turn")
        race_features.append("ADV: Attacks v. creatures if ally w/in 5ft")
        race_features.append("DISADV: Attack / Perception when target in direct sunlight")
        race_features.append("")

        get_proficiency("DRACONIC", languages)

    if chosen_race == "ORC":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(12, 20, 30, 40)
        get_size(16, 64, 12, 175)

        get_monstrous_origin()

        roll_alignment = randint(1,100)
        if roll_alignment < 65:
            char_align = "CHAOTIC EVIL"
        elif roll_alignment < 75:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 95:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 98:
            char_align = "TRUE NEUTRAL"
        else:
            char_align = "CHAOTIC GOOD"
        race_features.append(char_align)
        race_features.append("")

        ability_scores["STRENGTH"] += 2
        ability_scores["CONSTITUTION"] += 1
        ability_scores["INTELLIGENCE"] += -2

        get_speed(30)
        race_features.append("DARKVISION: 60ft")
        race_features.append("[B]: Move up to your speed towards an enemy")
        race_features.append("     you can see or hear, ending closer than starting")
        race_features.append("Count as one size larger for carry and push/pull/lift thresholds")
        race_features.append("")

        skill_modifiers["INTIMIDATION"] += 2
        
        get_proficiency("ORC", languages)

    if chosen_race == "YUAN-TI PUREBLOOD":

        race_features.append(chosen_race)
        race_features.append("")

        get_age(15, 25, 45, 60)
        get_size(20, 56, 8, 110)

        get_monstrous_origin()

        roll_alignment = randint(1,100)
        if roll_alignment < 70:
            char_align = "NEUTRAL EVIL"
        elif roll_alignment < 90:
            char_align = "TRUE NEUTRAL"
        elif roll_alignment < 95:
            char_align = "CHAOTIC NEUTRAL"
        elif roll_alignment < 98:
            char_align = "CHAOTIC EVIL"
        else:
            char_align = "CHAOTIC GOOD"
        race_features.append(char_align)
        race_features.append("")

        get_speed(30)
        get_darkvision(60)

        race_features.append("Gain 'Poison Spray' Cantrip (CHA Spellcasting)")
        race_features.append("ADV: Save v. Spells / Magical effects")
        race_features.append("IMMUNE: Poison Damage / Poisoned Condition")

        get_proficiency("ABYSSAL", languages)
        get_proficiency("DRACONIC", languages)

        spellbook_0.append("Poison Spray (Yuan-Ti)")

    if chosen_race == "GITH":

        def get_githyanki_align():

            roll_alignment = randint(1,100)
            if roll_alignment < 40:
                char_align = "LAWFUL EVIL"
            if roll_alignment < 60:
                char_align = "LAWFUL NEUTRAL"
            elif roll_alignment < 80:
                char_align = "NEUTRAL EVIL"
            elif roll_alignment < 90:
                char_align = "CHAOTIC NEUTRAL"
            else:
                char_align = "CHAOTIC EVIL"
            race_features.append(char_align)
            race_features.append("")
        def get_githzerai_align():

            roll_alignment = randint(1,100)
            if roll_alignment < 40:
                char_align = "LAWFUL NEUTRAL"
            if roll_alignment < 60:
                char_align = "TRUE NEUTRAL"
            elif roll_alignment < 80:
                char_align = "NEUTRAL GOOD"
            elif roll_alignment < 90:
                char_align = "LAWFUL GOOD"
            else:
                char_align = "CHAOTIC GOOD"
            race_features.append(char_align)
            race_features.append("")

        gith_subrace = ["GITHYANKI", "GITHZERAI"]
        chosen_race = get_item(gith_subrace)

        race_features.append(chosen_race)
        race_features.append("")

        ability_scores["INTELLIGENCE"] += 1

        get_age(15, 25, 45, 60)
        get_speed(30)
        get_proficiency("GITH", languages)

        race_features.append("PSIONICS: You know the Mage Hand cantrip, and the")
        race_features.append("        : hand is invisible to you when you cast it.")
        
        if chosen_race == "GITHYANKI":
            
            ability_scores["STRENGTH"] += 2
            
            get_githyanki_align()
            get_size(24, 60, 8, 100)
            
            skill_or_tool = randint(1,2)
            if skill_or_tool == 1:
                get_proficiency("GET", avail_skills)
            else:
                get_proficiency("GET", tools)
            
            get_proficiency("GET", languages)
            get_proficiency("LIGHT", armor)
            get_proficiency("MEDIUM", armor)
            get_proficiency("SHORT SWORD", martial_wpns)
            get_proficiency("LONGSWORD", martial_wpns)
            get_proficiency("GREATSWORD", martial_wpns)
        
        if chosen_race == "GITHZERAI":
            
            ability_scores["WISDOM"] += 2
            
            get_githzerai_align()
            get_size(24, 59, 4, 90)
            
            race_features.append("ADV: Saves v. Charmed / Frightened condition")

    return chosen_race

print (get_race())
print ()

update_mods()

clss = [
        "BARBARIAN",
        "BARD",
        "CLERIC",
        "DRUID",
        "FIGHTER",
        "MONK",
        "PALADIN",
        "RANGER",
        "ROGUE",
        "SORCERER",
        "WARLOCK",
        "WIZARD"
        ]
def get_class():

    def get_hit_points(hit_die):

        hit_points = (ability_modifiers["CONSTITUTION"] + hit_die)
        
        if tough == True:
            hit_points += 2
        
        if hill_dwarf == True:
            hit_points += 1

        class_features.append("HIT DIE: 1d{0}".format(hit_die))
        class_features.append("HIT POINTS: {0}".format(hit_points))
        class_features.append("")

    spell_dc = 0
    def get_spellcasting(attribute, spell_slots_1):

        spell_attack = (2 + ability_modifiers[(attribute)])
        spell_dc = (spell_attack + 8)
        
        class_features.append("SPELLCASTING: Attack: +{0}, Save DC: {1}".format(spell_attack, spell_dc))
        class_features.append("            : Spell Slots : Level 1 : {0}".format(spell_slots_1))
        class_features.append("")

    def get_inventory(option_1, option_2):

        item_options = []
        items_to_add = []

        simple_melee = simple_wpns[:10]

        item_options.append(option_1)
        item_options.append(option_2)

        chosen_item = get_item(item_options)

        if chosen_item == "SIMPLE WEAPON":
            items_to_add.append(get_item(simple_wpns))

        elif chosen_item == "SIMPLE MELEE":
            items_to_add.append(get_item(simple_melee))

        elif chosen_item == "TWO SIMPLE MELEE":
            items_to_add.append(get_item(simple_melee))
            items_to_add.append(get_item(simple_melee))

        elif chosen_item == "MARTIAL WEAPON":
            items_to_add.append(get_item(martial_wpns))

        elif chosen_item == "MARTIAL/SHIELD":
            items_to_add.append(get_item(martial_wpns))
            items_to_add.append("SHIELD")
            
        elif chosen_item == "TWO MARTIAL WEAPONS":
            items_to_add.append(get_item(martial_wpns))
            items_to_add.append(get_item(martial_wpns))
            
        elif chosen_item == "SCALE/CHAIN":
            get_inventory("SCALE MAIL", "CHAIN MAIL")
            
        elif chosen_item == "LEATHER/LONGBOW":
            items_to_add.append("LEATHER ARMOR")
            items_to_add.append("LONGBOW")
        
        elif chosen_item == "RAPIER/LONGSWORD":
            get_inventory("RAPIER", "LONGSWORD")
        
        elif chosen_item == "INSTRUMENT":
            items_to_add.append(get_item(instruments))
        
        else:
            items_to_add.append(chosen_item)
        
        for item in items_to_add:
            inventory.append(item)

    if ability_scores["STRENGTH"] < 10 and ability_scores["DEXTERITY"] < 10:
        clss.remove("FIGHTER")
    if ability_scores["STRENGTH"] < 10 and ability_scores["CONSTITUTION"] < 10:
        clss.remove("BARBARIAN")
    if ability_scores["STRENGTH"] < 10 and ability_scores["CHARISMA"] < 10:
        clss.remove("PALADIN")
    if ability_scores["DEXTERITY"] < 10:
        clss.remove("MONK")
        clss.remove("ROGUE")
    if ability_scores["DEXTERITY"] < 10 and ability_scores["WISDOM"] < 10:
        clss.remove("RANGER")
    if ability_scores["INTELLIGENCE"] < 10:
        clss.remove("WIZARD")
    if ability_scores["WISDOM"] < 10:
        clss.remove("CLERIC")
        clss.remove("DRUID")
    if ability_scores["CHARISMA"] < 10:
        clss.remove("BARD")
        clss.remove("SORCERER")
        clss.remove("WARLOCK")

    chosen_class = get_item(clss)

    if chosen_class == "BARBARIAN":

        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(12)
        
        unarmored_ac = ability_modifiers["DEXTERITY"] + ability_modifiers["CONSTITUTION"] + 10
        class_features.append("RAGE: ADV: Strength Checks and Saving Throws")
        class_features.append("    : (2/day, bonus action, no Heavy Armor)")
        class_features.append("    : +2 Damage with melee weapons")
        class_features.append("    : RES: Bludgeoning / Piercing / Slashing damage")
        class_features.append("")
        class_features.append("UNARMORED DEFENSE: AC = {0} (10+DEX+CON)".format(unarmored_ac))
        class_features.append("")
        
        get_proficiency("MEDIUM", armor)
        get_proficiency("SHIELDS", armor)
        get_proficiency("MARTIAL", martial_wpns)
        get_proficiency("STRENGTH", saves)
        get_proficiency("CONSTITUTION", saves)
        
        barb_skills = [
                    "ANIMAL HANDLING",
                    "ATHLETICS",
                    "INTIMIDATION",
                    "NATURE",
                    "PERCEPTION",
                    "SURVIVAL"
                    ]
        for i in range(2):
            get_skill(barb_skills)

        get_inventory("GREATAXE", "MARTIAL WEAPON")
        get_inventory("HANDAXE (x2)", "SIMPLE WEAPON")
        inventory.append("JAVELIN (x4)")
        inventory.append("EXPLORER'S PACK")

    if chosen_class == "BARD":

        class_features.append(chosen_class)
        class_features.append("")
        
        get_hit_points(8)

        class_features.append("BARDIC INSPIRATION (Bonus Action):")
        class_features.append("         : Creature w/in 60ft that can hear you:")
        class_features.append("         : Gains 1d6 to use w/in 10 min on Attack / Ability / Save")
        class_features.append("")

        get_spellcasting("CHARISMA", "4")

        get_proficiency("LIGHT", armor)
        get_proficiency("DEXTERITY", saves)
        get_proficiency("CHARISMA", saves)
        get_proficiency("SIMPLE", simple_wpns)
        get_proficiency("LONGSWORD", martial_wpns)
        get_proficiency("SHORT SWORD", martial_wpns)
        get_proficiency("RAPIER", martial_wpns)
        get_proficiency("HAND XBOW", martial_wpns)
        
        bard_skills = [
                    "ATHLETICS",
                    "ACROBATICS",
                    "SLEIGHT OF HAND",
                    "STEALTH",
                    "ARCANA",
                    "HISTORY",
                    "INVESTIGATION",
                    "NATURE",
                    "PERFORMANCE",
                    "ANIMAL HANDLING",
                    "DECEPTION",
                    "MEDICINE",
                    "PERCEPTION",
                    "SURVIVAL",
                    "DECEPTION",
                    "INTIMIDATION",
                    "PERFORMANCE",
                    "PERSUASION"
                    ]
        for i in range(3):
            get_skill(bard_skills)

        get_inventory("RAPIER/LONGSWORD", "SIMPLE WEAPON")
        get_inventory("DIPLOMAT'S PACK", "ENTERTAINER'S PACK")
        get_inventory("LUTE", "INSTRUMENT")
        inventory.append("LEATHER ARMOR")
        inventory.append("DAGGER")
        
        for i in range(2):
            get_spell("GET", bard_spell_0, spellbook_0)
        for i in range(4):
            get_spell("GET", bard_spell_1, spellbook_1)

    if chosen_class == "CLERIC":

        def get_domain_spells(spell_1, spell_2):

            domain_spells = "DOMAIN SPELLS (always prepared): {0} / {1}".format(spell_1, spell_2)
            class_features.append(domain_spells)
            class_features.append("")

            spell_1 = "(Domain) {0}".format(spell_1)
            spell_2 = "(Domain) {0}".format(spell_2)
            
            spellbook_1.append(spell_1)
            spellbook_1.append(spell_2)

        spellbook_1.remove("LEVEL 1 SPELLS:")
        spellbook_1.append("LEVEL 1 SPELLS PREPARED:")

        cler_domain = [
                    "KNOWLEDGE",
                    "LIFE",
                    "LIGHT",
                    "NATURE",
                    "TEMPEST",
                    "TRICKERY",
                    "WAR",
                    "ARCANA"
                    ]
        chosen_domain = get_item(cler_domain)
        chosen_class = "CLERIC, {0} DOMAIN".format(chosen_domain)
        
        class_features.append(chosen_class)
        class_features.append("")
        
        get_hit_points(8)

        get_spellcasting("WISDOM", "2")
 
        spells_prepared = ability_modifiers[("WISDOM")] + 1
        if spells_prepared < 1:
            spells_prepared = 1
        
        domain_per_LR = ability_modifiers[("WISDOM")]
        if domain_per_LR < 1:
            domain_per_LR = 1
 
        class_features.append("      : After LR, Prepare up to {0} spells from Cleric list".format(spells_prepared))
        class_features.append("      : Preparing takes at least 1 min per spell in meditation")
        class_features.append("")

        get_proficiency("SIMPLE", simple_wpns)
        get_proficiency("MEDIUM", armor)
        get_proficiency("SHIELDS", armor)
        get_proficiency("WISDOM", saves)
        get_proficiency("CHARISMA", saves)

        cleric_skills = [
                        "HISTORY",
                        "DECEPTION",
                        "MEDICINE",
                        "PERSUASION",
                        "PERFORMANCE"
                        ]
        for i in range(2):
            get_skill(cleric_skills)

        get_inventory("MACE", "WARHAMMER")
        get_inventory("LEATHER ARMOR", "SCALE/CHAIN")
        get_inventory("LIGHT XBOW", "SIMPLE WEAPON")
        inventory.append("SHIELD")
        inventory.append("HOLY SYMBOL")

        for i in range(3):
            get_spell("GET", cleric_spell_0, spellbook_0)

        for i in range(spells_prepared):
            get_spell("GET", cleric_spell_1, spellbook_1)
        

        if chosen_domain == "KNOWLEDGE":

            get_domain_spells("COMMAND", "IDENTIFY")

            get_proficiency("GET", languages)
            get_proficiency("GET", languages)

            domain_skills = [
                        "HISTORY",
                        "ARCANA",
                        "NATURE",
                        "PERFORMANCE"
                        ]
            get_expertise(domain_skills)
            get_expertise(domain_skills)

        if chosen_domain == "LIFE":

            get_domain_spells("BLESS", "CURE WOUNDS")
            
            class_features.append("DISCIPLE OF LIFE: Add 2 + Spell Lvl to Lvl 1+ Heal Spells")
            class_features.append("")
            
            get_proficiency("HEAVY", armor)

        if chosen_domain == "LIGHT":

            get_domain_spells("BURNING HANDS", "FAERIE FIRE")
            spellbook_0.append("(Domain) LIGHT")

            class_features.append("WARDING FLARE (Reaction): Give DISADV: Attack to creature within 30ft")
            class_features.append("  : Uses per LR: {0}".format(domain_per_LR))
            class_features.append("")
            class_features.append("Gain Cantrip: Light")
            class_features.append("")
            
        if chosen_domain == "NATURE":

            get_spell("GET", druid_spell_0, spellbook_0)
            druid_cantrip = spellbook_0[(len(spellbook_0)-1)]

            get_domain_spells("ANIMAL FRIENDSHIP", "SPEAK WITH ANIMALS")
            class_features.append("Gain Druid cantrip: {0}".format(druid_cantrip))
            class_features.append("")
            
            get_proficiency("HEAVY", armor)

            domain_skills = [
                        "ANIMAL HANDLING",
                        "NATURE",
                        "SURVIVAL"
                        ]
            get_expertise(domain_skills)
            get_expertise(domain_skills)
        
        if chosen_domain == "TEMPEST":

            get_proficiency("MARTIAL", martial_wpns)
            get_proficiency("HEAVY", armor)

            get_domain_spells("FOG CLOUD", "THUNDERWAVE")
            
            class_features.append("WRATH OF THE STORM: (Reaction): On hit from within 5ft;")
            class_features.append("     : 2d8 Lightning or Thunder, DEX Save (DC {0}) for 1/2".format(spell_dc))
            class_features.append("     : Uses per LR: {0}".format(domain_per_LR))
            class_features.append("")
            
        if chosen_domain == "TRICKERY":

            get_domain_spells("CHARM PERSON", "DISGUISE SELF")
            
            class_features.append("TRICKSTER'S BLESSING (action): Touch a willing creature other than you;")
            class_features.append("            : give ADV: Dex(Stealth) Checks for 1 hour or until re-used")
            class_features.append("")
            
        if chosen_domain == "WAR":

            get_proficiency("MARTIAL", martial_wpns)
            get_proficiency("HEAVY", armor)

            get_domain_spells("DIVINE FAVOR", "SHIELD OF LIFE")

            class_features.append("WAR PRIEST: On 'Attack' action, make one weapon attack as Bonus action.")
            class_features.append("          : Uses per LR: {0}".format(domain_per_LR))
            class_features.append("")
            
        if chosen_domain == "ARCANA":
            
            get_domain_spells("MAGIC MISSILE", "DETECT MAGIC")
            
            get_spell("GET", wiz_spell_0, spellbook_0)
            domain_cantrip_1 = wiz_spell_0[(len(wiz_spell_0)-1)]
            
            get_spell("GET", wiz_spell_0, spellbook_0)
            domain_cantrip_2 = wiz_spell_0[(len(wiz_spell_0)-1)]

            class_features.append("Gain Prof: INT(Arcana) Checks")
            class_features.append("")
            class_features.append("Gain Two Wizard Cantrips:")
            class_features.append("     : {0}".format(domain_cantrip_1))
            class_features.append("     : {0}".format(domain_cantrip_2))
            class_features.append("")

    if chosen_class == "DRUID":

        spellbook_1.remove("LEVEL 1 SPELLS:")
        spellbook_1.append("LEVEL 1 SPELLS PREPARED:")
        
        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(8)

        get_spellcasting("WISDOM", "2")

        spells_prepared = ability_modifiers[("WISDOM")] + 1           
        if spells_prepared < 1:                         
            spells_prepared = 1                         
                                                        
        class_features.append("      : After LR, Prepare up to {0} spells from Druid list".format(spells_prepared))
        class_features.append("      : Preparing takes at least 1 min per spell in meditation")
        class_features.append("")
        class_features.append("DRUIDIC: Secret language of the Druids")
        class_features.append("")
            
        get_spell("GET", druid_spell_0, spellbook_0)    
        get_spell("GET", druid_spell_0, spellbook_0)    
                                                        
        for i in range(spells_prepared):
            get_spell("GET", druid_spell_1, spellbook_1)                    

        get_proficiency("HERBALISM KIT", tools)
        get_proficiency("DRUIDIC", languages)
        get_proficiency("CLUB", simple_wpns)
        get_proficiency("DAGGER", simple_wpns)
        get_proficiency("DART", simple_wpns)
        get_proficiency("JAVELIN", simple_wpns)
        get_proficiency("MACE", simple_wpns)
        get_proficiency("QUARTERSTAFF", simple_wpns)
        get_proficiency("SCIMITAR", simple_wpns)
        get_proficiency("SICKLE", simple_wpns)
        get_proficiency("SLING", simple_wpns)
        get_proficiency("SPEAR", simple_wpns)
        get_proficiency("Armor (MEDIUM) (non-metal)")
        get_proficiency("Armor (SHIELDS) (non-metal)")
        get_proficiency("INTELLIGENCE", saves)
        get_proficiency("WISDOM", saves)

        druid_skills = [
                    "ARCANA",
                    "DECEPTION",
                    "MEDICINE",
                    "ANIMAL HANDLING",
                    "NATURE",
                    "PERCEPTION",
                    "PERFORMANCE",
                    "SURVIVAL"
                    ]
        get_skill(druid_skills)
        get_skill(druid_skills)

        get_inventory("WOODEN SHIELD", "SIMPLE WEAPON")
        get_inventory("SCIMITAR", "SIMPLE MELEE")
        inventory.append("LEATHER ARMOR")
        inventory.append("EXPLORER'S PACK")
        inventory.append("DRUIDIC FOCUS")

    if chosen_class == "FIGHTER":

        fighting_style = [
                    "ARCHER",
                    "DEFENDER",
                    "DUELIST",
                    "GREAT WEAPONS",
                    "SHIELD MASTER",
                    "DUAL-WIELDER",
                    ]
        chosen_style = get_item(fighting_style)
        chosen_class = "FIGHTER ({0})".format(chosen_style)
        
        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(10)

        get_proficiency("Armor (ALL)")
        get_proficiency("SHIELDS", armor)
        get_proficiency("MARTIAL", martial_wpns)
        get_proficiency("STRENGTH", saves)
        get_proficiency("CONSTITUTION", saves)

        fighter_skills = [
                    "ACROBATICS",
                    "ANIMAL HANDLING",
                    "ATHLETICS",
                    "HISTORY",
                    "DECEPTION",
                    "INTIMIDATION",
                    "PERCEPTION",
                    "SURVIVAL"
                    ]
        get_skill(fighter_skills)
        get_skill(fighter_skills)

        get_inventory("CHAIN MAIL", "LEATHER/LONGBOW")
        get_inventory("MARTIAL & SHIELD", "TWO MARTIAL WEAPONS")
        get_inventory("LIGHT XBOW", "TWO HANDAXES")
        get_inventory("DUNGEONEER'S PACK", "EXPLORER'S PACK")

        class_features.append("SECOND WIND: (1/SR) Bonus Action to Heal 1d10 +Lvl HP")
        class_features.append("")
            
        if chosen_style == "ARCHER":
            class_features.append("ARCHERY: +2 to Attack Rolls with Ranged Weapons")
        if chosen_style == "DEFENDER":
            class_features.append("DEFENSE: +1 to AC while wearing Armor")
        if chosen_style == "DUELIST":
            class_features.append("DUELING: +2 Damage rolls with single Melee Weapon")
        if chosen_style == "GREAT WEAPONS":
            class_features.append("GREAT WEAPON: Re-roll 1 or 2 on damage dice when wielding with two hands")
        if chosen_style == "SHIELD MASTER":
            class_features.append("PROTECTION: Reaction (w/Shield): Give Disadv: Attack targeting adjacent ally")
        if chosen_style == "DUAL-WIELDER":
            class_features.append("TWO-WEAPON: Add Ability Modifier to Damage roll of Off-hand Attack")
        class_features.append("")
            
    if chosen_class == "MONK":

        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(8)

        unarmored_ac = ability_modifiers["DEXTERITY"] + ability_modifiers["WISDOM"] + 10
        class_features.append("UNARMORED DEFENSE: AC = {0} (10+DEX+WIS)".format(unarmored_ac))
        class_features.append("")
        class_features.append("MARTIAL ARTS: While unarmed or w/Monk weapons and unarmored")
        class_features.append("       : Use DEX instead of STR for Attack / Damage rolls")
        class_features.append("       : Can roll 1d4 in place of normal damage (^ with Lvl)")
        class_features.append("       : Make one unarmed strike as [Bonus] when using [Attack]")
        class_features.append("")
            
        tool_or_inst = randint(1,2)
        if tool_or_inst == 1:
            get_proficiency("GET", tools)
        else:
            get_proficiency("GET", instruments)

        get_proficiency("SIMPLE", simple_wpns)
        get_proficiency("SHORT SWORD", martial_wpns)
        get_proficiency("STRENGTH", saves)
        get_proficiency("DEXTERITY", saves)

        monk_skills = [
                    "ACROBATICS",
                    "ATHLETICS",
                    "HISTORY",
                    "DECEPTION",
                    "PERFORMANCE",
                    "STEALTH"
                    ]
        for i in range(2):
            get_skill(monk_skills)

        get_inventory("SHORT SWORD", "SIMPLE WEAPON")
        get_inventory("DUNGEONEER'S PACK", "EXPLORER'S PACK")
        inventory.append("DARTS (x10)")

    if chosen_class == "PALADIN":

        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(10)

        divsense_per_LR = (ability_modifiers["CHARISMA"] + 1)
        
        class_features.append("DIVINE SENSE: (Action): until next turn, w/in 60ft")
        class_features.append("    : Know location of celestial/fiend/undead")
        class_features.append("    : Know location of consecrated/desecrated grounds")
        class_features.append("    : Uses per LR: {0}".format(divsense_per_LR))
        class_features.append("")
        class_features.append("LAY ON HANDS: Pool of Healing Power = 5x Lvl")
        class_features.append("    : (Action): Restore up to max pool remaining HP")
        class_features.append("    : (Action): Cure one disease or poison (per HP in pool)")
        class_features.append("")
            
        get_proficiency("Armor (ALL)")
        get_proficiency("SHIELDS", armor)
        get_proficiency("MARTIAL", martial_wpns)
        get_proficiency("WISDOM", saves)
        get_proficiency("CHARISMA", saves)

        pal_skills = [
                    "ATHLETICS",
                    "DECEPTION",
                    "INTIMIDATION",
                    "MEDICINE",
                    "PERSUASION",
                    "PERFORMANCE",
                ]
        get_skill(pal_skills)
        get_skill(pal_skills)

        get_inventory("MARTIAL/SHIELD", "TWO MARTIAL WEAPONS")
        get_inventory("5X JAVELINS", "SIMPLE MELEE")
        get_inventory("PRIEST'S PACK", "EXPLORER'S PACK")
        inventory.append("CHAINMAIL")
        inventory.append("HOLY SYMBOL")

    if chosen_class == "RANGER":

        favored_enemies = [
                        "ABERRATION",
                        "BEAST",
                        "CELESTIAL",
                        "CONSTRUCT",
                        "DRAGON",
                        "ELEMENTAL",
                        "FEY",
                        "FIEND",
                        "GIANT",
                        "HUMANOID",
                        "MONSTROSITY",
                        "OOZE",
                        "PLANT",
                        "UNDEAD"
                        ]
        chosen_enemies = []
        chosen_enemy = get_item(favored_enemies)               
                                                               
        if chosen_enemy == "HUMANOID":                         
            humanoids = [
                            "AASIMAR",
                            "BUGBEAR",
                            "BULLYWUG",
                            "CATFOLK",
                            "DRAGONBORN",
                            "DROW",
                            "DWARF",
                            "ELF",
                            "GENASI",
                            "GITH",
                            "GNOLL",
                            "GNOME",
                            "GOBLIN",
                            "GOLIATH",
                            "HALF-ELF",
                            "HALF-ORC",
                            "HALFLING",
                            "HOBGOBLIN",
                            "HUMAN",
                            "KENKU",
                            "KOBOLD",
                            "LIZARDFOLK",
                            "MERFOLK",
                            "ORC",
                            "TIEFLING",
                            "TROGLODYTE",
                            ]
            chosen_humanoid_1 = get_item(humanoids)               
            chosen_humanoid_2 = get_item(humanoids)               

            chosen_enemies.append(chosen_humanoid_1)
            chosen_enemies.append(chosen_humanoid_2)
        else:
            chosen_enemies.append(chosen_enemy)
        
        favored_terrain = [
                        "ARCTIC",
                        "COAST",
                        "DESERT",
                        "FOREST",
                        "GRASSLAND",
                        "MOUNTAIN",
                        "SWAMP",
                        "UNDERDARK"
                        ]
        chosen_terrain = get_item(favored_terrain)

        if len(chosen_enemies) > 1:
            chosen_class = "RANGER ({0} WALKER, {1}/{2} HUNTER)".format(chosen_terrain, chosen_humanoid_1, chosen_humanoid_2)
        else:
            chosen_class = "RANGER ({0} WALKER, {1} HUNTER)".format(chosen_terrain, chosen_enemy)

        class_features.append(chosen_class)
        class_features.append("")

        for item in chosen_enemies:
            class_features.append("FAVORED ENEMY: {0}".format(item))
        class_features.append("  : ADV: WIS(Survival) Checks to track enemy")
        class_features.append("  : ADV: INT Checks to recall general information about enemy")
        class_features.append("")

        # Gain Language Proficiency    
        for item in chosen_enemies:
            if item == ("AASIMAR" or "CELESTIAL"):
                get_proficiency("CELESTIAL", languages)
            if item == ("DRAGON" or "KOBOLD" or "DRAGONBORN" or "LIZARDFOLK"):
                get_proficiency("DRACONIC", languages)
            if item == "DWARF":
                get_proficiency("DWARVEN", languages)
            if item == "ELF":
                get_proficiency("ELVEN", languages)
            if item == ("GIANT" or "GOLIATH"):
                get_proficiency("GIANT", languages)
            if item == "GITH":
                get_proficiency("GITH", languages)
            if item == "GNOLL":
                get_proficiency("GNOLL", languages)
            if item == ("GOBLIN" or "HOBGOBLIN" or "BUGBEAR"):
                get_proficiency("GOBLIN", languages)
            if item == "DROW":
                get_proficiency("UNDERCOMMON", languages)
            if item == ("GENASI" or "ELEMENTAL" or "MERFOLK"):
                get_proficiency("PRIMORDIAL", languages)
            if item == ("ORC" or "HALF-ORC"):
                get_proficiency("ORC", languages)
            if item == "TROGLODYTE":
                get_proficiency("TROGLODYTE", languages)
            if item == "FEY":
                get_proficiency("SYLVAN", languages)
            if item == ("FIEND" or "TIEFLING"):
                get_proficiency("INFERNAL", languages)

        get_hit_points(10)

        class_features.append("NATURAL EXPLORER: {0}".format(chosen_terrain))
        class_features.append("  : 2x Prof (if already Prof): INT / WIS checks re: terrain")
        class_features.append("  : During long travel: not slowed by Difficult Terrain")
        class_features.append("  : Can not get lost except by magical means")
        class_features.append("  : Remain alert to danger while foraging/tracking/other")
        class_features.append("  : Move stealthily at normal pace (solo)")
        class_features.append("  : Forage for 2x as much food")
        class_features.append("  : Learn exact number/size/timestamp of tracked creatures")
        class_features.append("")
            
        get_proficiency("MARTIAL", martial_wpns)
        get_proficiency("MEDIUM", armor)
        get_proficiency("SHIELDS", armor)
        get_proficiency("STRENGTH", saves)
        get_proficiency("DETERITY", saves)

        ranger_skills = [
                    "ANIMAL HANDLING",
                    "ATHLETICS",
                    "DECEPTION",
                    "INVESTIGATION",
                    "NATURE",
                    "PERCEPTION",
                    "STEALTH",
                    "SURVIVAL"
                    ]
        for i in range(2):
            get_skill(ranger_skills)

        get_inventory("SCALE MAIL", "LEATHER ARMOR")
        get_inventory("TWO SHORT SWORDS", "TWO SIMPLE MELEE")
        get_inventory("DUNGEONEER'S PACK", "EXPLORER'S PACK")
        get_inventory("LONGBOW", "MARTIAL WEAPON")

    if chosen_class == "ROGUE":

        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(8)

        class_features.append("SNEAK ATTACK: (1/turn): +1d6 damage if ADV: Attack roll")
        class_features.append("         : OR if target is threatened from w/in 5ft")
        class_features.append("         : AND you are *not* DISADV: Attack roll.")
        class_features.append("")
        class_features.append("THIEVES' CANT: Secret language dialect, jargon, and code")
        class_features.append("         : Hide messages in normal convo (4x longer)")
        class_features.append("         : Symbols indicate danger/territories/shelter")
        class_features.append("")
            
        get_proficiency("LIGHT", armor)
        get_proficiency("SIMPLE", simple_wpns)
        get_proficiency("HAND XBOW", martial_wpns)
        get_proficiency("LONGSWORD", martial_wpns)
        get_proficiency("RAPIER", martial_wpns)
        get_proficiency("SHORT SWORD", martial_wpns)
        get_proficiency("THIEVES' TOOLS", tools)
        get_proficiency("DEXTERITY", saves)
        get_proficiency("INTELLIGENCE", saves)

        rogue_skills = [
                    "ACROBATICS",
                    "ATHLETICS",
                    "DECEPTION",
                    "INSIGHT",
                    "INTIMIDATION",
                    "INVESTIGATION",
                    "PERFORMANCE",
                    "PERCEPTION",
                    "PERSUASION",
                    "SLEIGHT OF HAND",
                    "STEALTH"
                    ]
        expertise_skills = ["THIEVES' TOOLS"]

        for i in range(4):
            get_skill(rogue_skills)

        for skill in skill_modifiers:
            if skill_modifiers[(skill)] > 0:
                expertise_skills.append(skill)

        for i in range(2):
            get_expertise(expertise_skills)

        get_inventory("RAPIER", "SHORT SWORD")
        get_inventory("SHORTBOW", "SHORT SWORD")
        get_inventory("BURGLAR'S PACK", "DUNGEONEER'S PACK")
        inventory.append("LEATHER ARMOR")
        inventory.append("DAGGER X2")
        inventory.append("THIEVES' TOOLS")

    if chosen_class == "SORCERER":

        sorc_origin = ["DRACONIC BLOODLINE", "WILD MAGIC", "STORM SORCERY"]
        chosen_origin = get_item(sorc_origin)
        chosen_class = "SORCERER ({0})".format(chosen_origin)
        
        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(6)

        get_spellcasting("CHARISMA", "2")

        get_proficiency("DAGGER", simple_wpns)
        get_proficiency("DART", simple_wpns)
        get_proficiency("SLING", simple_wpns)
        get_proficiency("QUARTERSTAFF", simple_wpns)
        get_proficiency("CONSTITUTION", saves)
        get_proficiency("CHARISMA", saves)

        sorc_skills = [
                    "ARCANA",
                    "DECEPTION",
                    "INSIGHT",
                    "INTIMIDATION",
                    "PERSUASION",
                    "PERFORMANCE"
                    ]
        for i in range(2):
            get_skill(sorc_skills)

        get_inventory("LIGHT XBOW", "SIMPLE WEAPON")
        get_inventory("COMPONENT POUCH", "ARCANE FOCUS")
        get_inventory("DUNGEONEER'S PACK", "EXPLORER'S PACK")
        inventory.append("DAGGER x2")
        
        class_features.append("SORCEROUS ORIGIN: {0}".format(chosen_origin))
        class_features.append("")
        
        get_spell("GET", sorc_spell_0, spellbook_0)
        get_spell("GET", sorc_spell_0, spellbook_0)
        get_spell("GET", sorc_spell_0, spellbook_0)
        get_spell("GET", sorc_spell_0, spellbook_0)
        get_spell("GET", sorc_spell_1, spellbook_1)
        get_spell("GET", sorc_spell_1, spellbook_1)

        if chosen_origin == "DRACONIC BLOODLINE":

            get_proficiency("DRACONIC", languages)

            sorc_bloodline = [
                        "BLACK DRAGON",
                        "BLUE DRAGON",
                        "BRASS DRAGON",
                        "BRONZE DRAGON",
                        "COPPER DRAGON",
                        "GOLD DRAGON",
                        "GREEN DRAGON",
                        "RED DRAGON",
                        "SILVER DRAGON",
                        "WHITE DRAGON"
                        ]
            char_bloodline = get_item(sorc_bloodline)
            
            class_features.append("DRACONIC BLOODLINE: {0}".format(char_bloodline))
            class_features.append("  : 2x Prof: CHA checks v. Dragons")
            class_features.append("  : Gain +1 HP per SORCERER level")
            class_features.append("  : Scales: Unarmored AC = 13 + DEX")
            class_features.append("")

        if chosen_origin == "WILD MAGIC":

            class_features.append("WILD MAGIC: Roll 1d20 on casting spell Lvl 1+ ; 1 sets off Surge")
            class_features.append("  : Roll 1d100 on Surge table to determine effect")
            class_features.append("  : Tides of Chaos: Gain ADV on Attack / Ability / Save")
            class_features.append("  : 1/day or roll an extra 1d20 on next Surge to regain")
            class_features.append("")

        if chosen_origin == "STORM SORCERY":

            get_proficiency("PRIMORDIAL", languages)

            class_features.append("[B]: Immediately before or after you cast L1+ Spell,")
            class_features.append("   : whirling gusts of air allow you to fly 10ft")
            class_features.append("   : without provoking attacks of opportunity")
            class_features.append("")

    if chosen_class == "WARLOCK":

        def expand_spell_list(spell_1, spell_2):

            warlock_spell_1.append(spell_1)
            warlock_spell_1.append(spell_2)

            class_features.append("EXPANDED SPELL LIST: {0}, {1}".format(spell_1, spell_2))
            class_features.append("")

        patrons = [
            "THE ARCHFEY", 
            "THE FIEND", 
            "THE GREAT OLD ONE", 
            "THE UNDYING", 
            "THE CELESTIAL"
            ]
        chosen_patron = get_item(patrons)
        chosen_class = "WARLOCK OF {0}".format(chosen_patron)
        
        class_features.append(chosen_class)
        class_features.append("")
        
        get_hit_points(8)

        get_spellcasting("CHARISMA", "1")

        class_features.append("OTHERWORLDLY PATRON: {0}".format(chosen_patron))
        class_features.append("")

        for i in range(2):
            get_spell("GET", warlock_spell_0, spellbook_0)
            get_spell("GET", warlock_spell_1, spellbook_1)

        get_proficiency("SIMPLE", simple_wpns)
        get_proficiency("LIGHT", armor)
        get_proficiency("WISDOM", saves)
        get_proficiency("CHARISMA", saves)

        warlock_skills = [
                    "ARCANA",
                    "DECEPTION",
                    "HISTORY",
                    "INTIMIDATION",
                    "INVESTIGATION",
                    "NATURE",
                    "PERFORMANCE"
                    ]
        for i in range(2):
            get_skill(warlock_skills)

        get_inventory("QUARTERSTAFF", "SIMPLE WEAPON")
        get_inventory("LIGHT XBOW", "SIMPLE WEAPON")
        get_inventory("COMPONENT POUCH", "ARCANE FOCUS")
        get_inventory("DUNGEONEER'S PACK", "EXPLORER'S PACK")
        inventory.append("LEATHER ARMOR")
        inventory.append("DAGGER x2")

        if chosen_patron == "THE ARCHFEY":

            expand_spell_list("FAERIE FIRE", "SLEEP")
            
            class_features.append("Action (1/SR): 10ft cube: WIS v. Charm/Frightened")       
            class_features.append("")
            
        if chosen_patron == "THE FIEND":

            expand_spell_list("BURNING HANDS", "COMMAND")
            
            temp_hp = ability_modifiers["CHARISMA"] + 1
            class_features.append("On dropping an enemy to 0 HP, Gain {0} Temp HP (CHA + Warlock Lvl)".format(temp_hp))
            class_features.append("")
            
        if chosen_patron == "THE GREAT OLD ONE":
            
            expand_spell_list("DISSONANT WHISPERS", "TASHA'S HIDEOUS LAUGHTER")
            
            class_features.append("Communicate Telepathically within 30ft")
            class_features.append("")
            
        if chosen_patron == "THE UNDYING":

            expand_spell_list("FALSE LIFE", "RAY OF SICKNESS")

            class_features.append("ADV: Saving Throws v. Disease")
            class_features.append("")
            class_features.append("Undead must make WIS Save (DC {0}) in order to Attack you.".format(spell_dc))
            class_features.append("      : Undead are immune for 24hrs if you attack them or")
            class_features.append("      : they make a successful save")
            class_features.append("")
            
        if chosen_patron == "THE CELESTIAL":

            expand_spell_list("CURE WOUNDS", "GUIDING BOLT")
            spellbook_0.append("SACRED FLAME")
            spellbook_0.append("LIGHT")

            class_features.append("HEALING LIGHT: Pool of 1 + Warlock Lvl d6's")
            class_features.append("  [B] Heal 1 creature w/in 60ft from pool,")
            class_features.append("      CHA mod = max number of dice")
            class_features.append("      Dice replenish after Long Rest")
            class_features.append("")
            
    if chosen_class == "WIZARD":

        class_features.append(chosen_class)
        class_features.append("")

        get_hit_points(6)

        get_spellcasting("INTELLIGENCE", "2")
        class_features.append("")
        
        class_features.append("ARCANE RECOVERY (1/day): recover 1/2 Wiz Lvl in spell slots after SR")
        class_features.append("")
        
        # Gain 3 Wizard Cantrips    
        for i in range(3):
            get_spell("GET", wiz_spell_0, spellbook_0)
        # Gain 6 Lv 1 Wizard Spells
        for i in range(6):
            get_spell("GET", wiz_spell_1, spellbook_1)

        get_proficiency("DAGGER", simple_wpns)
        get_proficiency("DART", simple_wpns)
        get_proficiency("SLING", simple_wpns)
        get_proficiency("QUARTERSTAFF", simple_wpns)
        get_proficiency("LIGHT XBOW", martial_wpns)
        get_proficiency("INTELLIGENCE", saves)
        get_proficiency("WISDOM", saves)

        wiz_skills = [
                    "ARCANA",
                    "HISTORY",
                    "DECEPTION",
                    "INVESTIGATION",
                    "MEDICINE",
                    "PERFORMANCE"
                    ]
        for i in range(2):
            get_skill(wiz_skills)

        get_inventory("QUARTERSTAFF", "DAGGER")
        get_inventory("COMPONENT POUCH", "ARCANE FOCUS")
        get_inventory("SCHOLAR'S PACK", "EXPLORER'S PACK")
        inventory.append("SPELLBOOK")
    
    return chosen_class

print (get_class())
print ()

backgrounds = [
        "ACOLYTE",
        "CHARLATAN",
        "CRIMINAL",
        "ENTERTAINER",
        "FOLK HERO",
        "GUILD ARTISAN",
        "HERMIT",
        "NOBLE",
        "OUTLANDER",
        "SAGE",
        "SAILOR",
        "SOLDIER",
        "URCHIN"
        ] 
def get_bg():

    def get_quirk(qtype, qlist):

        roll_quirk = randint(1,len(qlist))
        new_quirk = qlist[(roll_quirk - 1)]
        bg_features.append("{0} : {1}".format(qtype, new_quirk))
    
    def get_quirks():
        get_quirk("TRAIT", bg_trait)
        get_quirk("IDEAL", bg_ideal)
        get_quirk(" BOND", bg_bond)
        get_quirk(" FLAW", bg_flaw)

    def background_skills(skill1, skill2):
    
        if skill_modifiers[(skill1)] == 0:
            skill_modifiers[(skill1)] += 2
        else:
            get_skill(avail_skills)

        if skill_modifiers[(skill2)] == 0:
            skill_modifiers[(skill2)] += 2
        else:
            get_skill(avail_skills)

    chosen_bg = get_item(backgrounds)

    if chosen_bg == "ACOLYTE":
        
        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("SHELTER OF THE FAITHFUL: Can perform religious ceremonies")
        bg_features.append("    : Command respect of other devotees")
        bg_features.append("    : Receive free healing / aid from shrines")
        bg_features.append("    : Receive a modest lifestyle from other devotees")
        bg_features.append("    : Residence at home temple, can request assistance")
        bg_features.append("")
        
        background_skills("DECEPTION", "PERFORMANCE")

        for i in range(2):
            get_proficiency("GET", languages)

        inventory.append("HOLY SYMBOL")
        inventory.append("PRAYER BOOK/WHEEL")
        inventory.append("STICKS OF INCENSE")
        inventory.append("VESTMENTS / COMMON CLOTHES")
        inventory.append("BELT POUCH W/ 15g")

        bg_origins = [
            "I found refuge in a temple after running away at an early age.",
            "I was left at a temple by a family unable or unwilling to care for me.",
            "I grew up in a household with strong religious convictions.",
            "An impassioned sermon struck a chord deep in my soul and moved me to service",
            "I followed friend / elder / loved one into religious service.",
            "I was inspired after a personal encounter with a celestial being."
            ]
        bg_trait = [
                    "I idolize a particular hero and constantly refer to their deeds and example.",
                    "I find common ground between the fiercest enemies and always work towards peace.",
                    "I see omens in every event and action. The gods are speaking to us, if we would listen.",
                    "Nothing can shake my optimism. My god will provide for me and mine.",
                    "I quote/misquote sacred texts and scripture at every opportunity.",
                    "I am in/tolerant of other faiths and condemn/respect the worship of other gods.",
                    "I enjoy the fine living among my faith's elite; the rough life grates on me.",
                    "I have spent so long in my temple that I have no grasp of social interaction."
                    ]
        bg_ideal = [
                    "The ancient traditions of worship must be preserved and upheld.",
                    "I always help those in need, no matter the personal cost.",
                    "We must help bring about the changes the gods are working in the world.",
                    "I aim to one day rise to the top of my faith's heirarchy.",
                    "I trust that my deity guides my actions. If I work hard, things will go well.",
                    "I seek to prove myself worthy of my god's favor through my deeds."
                    ]
        bg_bond = [
                    "I would die to recover an ancient relic of my faith lost long ago.",
                    "I will be revenged on the corrupt heirarchy that branded me a heretic.",
                    "I owe my life to the priest that took me in as an orphaned child.",
                    "Everything I do is for the common folk.",
                    "I will do anything to protect my home temple.",
                    "I must protect a sacred text my enemies seek to destroy."
                    ]
        bg_flaw = [
                    "I judge others harshly, and myself even more so.",
                    "I put too much trust in my temple's elders.",
                    "My piety leads me to blindly trust those that share my faith.",
                    "I am inflexible in my thinking.",
                    "I am suspicious of strangers and expect the worst of them.",
                    "I become obsessed with a particular goal to the detriment of other needs."
                    ]

        get_quirk("ORIGIN", bg_origins)
        get_quirks()

    if chosen_bg == "CHARLATAN":

        specialty_scheme = [
                "GAMBLING CHEAT",
                "COUNTERFEITER",
                "HONEYPOT",
                "FALSE IDENTITIES",
                "PICKPOCKET",
                "FENCER"
                ]
        chosen_specialty = get_item(specialty_scheme)
        chosen_bg = "CHARLATAN ({0})".format(chosen_specialty)

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("FALSE IDENTITY: Disguise / Docs / Established Acquaintances")
        bg_features.append("    : Can forge official document if you've seen a real one")
        bg_features.append("")
        
        background_skills("DECEPTION", "SLEIGHT OF HAND")

        get_proficiency("DIGUISE KIT", tools)
        get_proficiency("FORGERY KIT", tools)

        inventory.append("FINE CLOTHES")
        inventory.append("DISGUISE KIT")
        inventory.append("SPECIALTY TOOLS")
        inventory.append("BELT POUCH W/ 15g")

        bg_trait = [
                        "I fall in and out of love easily, and I'm always pursuing someone.",
                        "I tell my best jokes at the worst times.",
                        "I use flattery to get my way whenever possible.",
                        "I never pass up the opportunity for a game of chance.",
                        "I lie about everything, even things that don't matter at all.",
                        "Sarcasm and Insults are my weapons of choice.",
                        "I have several holy symbols and invoke whichever deity suits my need at the time.",
                        "I pocket anything I see that might have some value."
                        ]
        bg_ideal = [
                        "I am a free spirit -- No one tells me what to do.",
                        "I only target the people who have coin to spare.",
                        "I always pass some of my loot on to the needy.",
                        "I'm always trying out a new con.",
                        "I lie for a living, but I am fiercely loyal to my friends.",
                        "These cons are just a means to an end. I've got great things ahead."
                        ]
        bg_bond = [
                        "I fleeced the wrong person and now have to keep an eye out for retribution.",
                        "I owe a debt to a crime lord and need money fast.",
                        "I have an illegitimate child that I give support to.",
                        "I will reclaim my family's status as honored nobility.",
                        "A corrupt official killed someone I love, and I will be revenged.",
                        "One of my cons left an innocent person in ruins and I might never forgive myself."
                        ]
        bg_flaw = [
                        "I never say no to a pretty face.",
                        "I spend my money before I even get my hands on it.",
                        "I love to hear myself talk. Especially when I'm talking about me.",
                        "I can't pass up a game of chance.",
                        "I can't resist swindling any nobility I meet.",
                        "I will preserve my own hide and run if the going gets too tough."
                        ]

        get_quirks()

    if chosen_bg == "CRIMINAL":

        crime_specialties = [
                    "BLACKMAILER",
                    "BURGLAR",
                    "ENFORCER",
                    "FENCE",
                    "HIGHWAY ROBBER",
                    "HIRED KILLER",
                    "PICKPOCKET",
                    "SMUGGLER"
                    ]
        chosen_specialty = get_item(crime_specialties)
        chosen_bg = "CRIMINAL ({0})".format(chosen_specialty)
        
        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("CRIMINAL CONTACT: Liaison to criminal network, always accessible")
        bg_features.append("      : Can always locate the black market contacts in town")
        bg_features.append("")

        background_skills("DECEPTION", "STEALTH")

        get_proficiency("GET", gaming_sets)
        get_proficiency("THIEVES' TOOLS", tools)

        inventory.append("Dark Hooded Common Clothes")
        inventory.append("Crowbar")
        inventory.append("Belt pouch with 15g")

        bg_trait = [
                        "I always have a plan when things go wrong.",
                        "I never raise my voice or let my emotions get the best of me.",
                        "I'm always casing any room I walk into: valuables, entries, exits.",
                        "I'd rather make friends than enemies.",
                        "I am incredibly suspicious of anyone who seems good and pious.",
                        "I perform better when the odds are stacked against me.",
                        "The quickest way to get me to do something is to say I can't.",
                        "I get incredibly offended at even the slightest insult."
                        ]
        bg_ideal = [
                        "I don't steal from others in my trade.",
                        "Chains are meant to be broken along with the people that forged them.",
                        "I steal from the wealthy to benefit people in need.",
                        "I will do anything for a bit of coin.",
                        "My crew is my life. Everyone else can hang for all I care.",
                        "There's a little bit of good in everyone."
                        ]
        bg_bond = [
                        "I'm trying to pay off an old debt to a longtime benefactor.",
                        "I use my ill-gotten gains to support my family.",
                        "I must recover the family heirloom that was stolen from me.",
                        "I'm constantly looking for a bigger challenge to take on.",
                        "I committed a terrible crime, and I must atone / cover up my tracks.",
                        "A mistake cost someone I loved their life, and it haunts me."
                        ]
        bg_flaw = [
                        "I can't help but pocket any shiny thing I see.",
                        "I will choose money over friendship most of the time.",
                        "If there's a plan, I'll either forget or just ignore it altogether.",
                        "I have a strong 'tell' that lets people know when I'm lying.",
                        "I'll turn tail and run if things start to look grim.",
                        "I have no qualms watching innocent people suffer for my crimes."
                        ]

        get_quirks()

    if chosen_bg == "ENTERTAINER":

        ent_routines = [
                    "ACTOR",
                    "DANCER",
                    "FIRE-EATER",
                    "JESTER",
                    "JUGGLER",
                    "INSTRUMENTALIST",
                    "POET",
                    "SINGER",
                    "STORYTELLER",
                    "TUMBLER"
                    ]
        chosen_routine = get_item(ent_routines)
        chosen_bg = "ENTERTAINER ({0})".format(chosen_routine)
        
        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("BY POPULAR DEMAND: Can perform to receive free lodging")
        bg_features.append("    : Strangers often recognize you and treat you well")
        bg_features.append("")

        background_skills("ACROBATICS", "PERFORMANCE")

        get_proficiency("GET", instruments)
        get_proficiency("DISGUISE KIT", tools)

        inventory.append("The favor of an admirer")
        inventory.append("Costume")
        inventory.append("Belt pouch with 15g")

        bg_trait = [
                    "I know a good story for any situation.",
                    "I collect local rumors and gossip wherever I go.",
                    "I'm a hopeless romantic, looking for my special someone.",
                    "I can defuse any type of tension with a performance.",
                    "I love a good insult, even when it's directed at me.",
                    "I get bitter when I'm not the cbger of attention.",
                    "I settle for nothing less than perfection.",
                    "My mood changes faster than I change keys in a song."
                    ]
        bg_ideal = [
                    "I perform to make the world a little more beautiful.",
                    "The stories and songs of the past must never be forgotten.",
                    "What the world needs are some fresh new ideas and bold action.",
                    "I'll never back down from a challenge when there's an audience.",
                    "Putting a smile on someone's face is all the payment I need most times.",
                    "Art should reflect the true soul of the artist."
                    ]
        bg_bond = [
                    "My instrument is my most treasured possession, and I will protet it at all costs.",
                    "My instrument was stolen and I would do anything to get it back.",
                    "My noble family is ashamed of my profession, and I will prove them wrong.",
                    "I idolize an ancient hero and strive to live up to his deeds.",
                    "I will do anything to prove myself better than my rival.",
                    "I would do anything for my troupe."
                    ]
        bg_flaw = [
                    "I would do anything for fame and fortune.",
                    "I'm a sucker for a pretty face.",
                    "A recent scandal means I have to keep a low profile in certain areas.",
                    "I made fun of a noble and now they want to end my career/life.",
                    "I say what's on my mind, especially when it's inappropriate.",
                    "My word means almost nothing. I do what feels right in the moment."
                    ]

        get_quirks()

    if chosen_bg == "FOLK HERO":

        defining_events = [
                "REBEL LEADER",
                "FIRST RESPONDER",
                "MONSTER KILLER",
                "WHISTLEBLOWER",
                "WAR HERO",
                "SUPERNATURAL ORIGIN",
                ]
        chosen_event = get_item(defining_events)
        chosen_bg = "FOLK HERO ({0})".format(chosen_event)
        
        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("RUSTIC HOSPITALITY: Find a place to stay with commoners.")
        bg_features.append("                  : They will shield you from the law,")
        bg_features.append("                  : But will not risk their lives for you")
        bg_features.append("")

        background_skills("ANIMAL HANDLING", "SURVIVAL")

        get_proficiency("GET", tools)
        get_proficiency("Vehicles (LAND)")

        inventory.append("Shovel")
        inventory.append("Iron Pot")
        inventory.append("Common Clothes")
        inventory.append("Belt pouch with 15g")

        bg_trait = [
                    "I judge people by their actions, not their words.",
                    "I am always ready to help soomeone in trouble.",
                    "I always follow through on my word.",
                    "I search for the most equitable solution to any argument.",
                    "I make a conscious effort to instill confidence in those around me.",
                    "I let other people come up with the ideas. I'm the one that gets it done.",
                    "I like to show off my loquacious vocabulary.",
                    "I get antsy if I sit in one place too long."
                    ]
        bg_ideal = [
                    "Everyone deserves dignity and respect.",
                    "No one is above the law.",
                    "Tyranny should be fought at every level.",
                    "Might makes right.",
                    "No matter what, be true to yourself and to others.",
                    "I have been called by a higher power and I will heed it."
                    ]
        bg_bond = [
                    "I lost my family long ago, but I will find them again.",
                    "I grew up working the land, and I will do everything I can to protect it.",
                    "I was harassed by a proud noble growing up, and I take my revenge on any bully I see.",
                    "I carry the tools of my old profession to remind me of my roots.",
                    "No person belongs in chains, and I will break any and every shackle I see.",
                    "My hometown sweetheart is my motivation in all I do."
                    ]
        bg_flaw = [
                    "The tyrant who rules my land will stop at nothing to see me dead.",
                    "I'm blind to any risk of failure, as it is my destiny to succeed.",
                    "I have a shameful secret that keeps me from returning home.",
                    "I have a weakness for the vices of the big city, especially fine food and drink.",
                    "I seek to overthrow the current rulers only so I can usurp the throne myself.",
                    "I have little trust in my allies."
                    ]

        get_quirks()

    if chosen_bg == "GUILD ARTISAN":

        guild_biz = [
                "ALCHEMISTS & APOTHECARIES",
                "ARMORERS, LOCKSMITHS, & FINESMITHS",
                "BREWERS, DISTILLERS, & VINTNERS",
                "CALLIGRAPHERS, SCRIBES, & SCRIVENERS",
                "CARPENTERS, ROOFERS, & PLASTERERS",
                "CARTOGRAPHERS, SURVEYORS, & CHART-MAKERS",
                "COBBLERS & SHOEMAKERS",
                "COOKS & BAKERS",
                "GLASSBLOWERS & GLAZERS",
                "JEWELERS & GEMCUTTERS",
                "LEATHERWORKERS, SKINNERS, & TANNERS",
                "MASONS & STONECUTTERS",
                "PAINTERS, LIMNERS, & SIGN-MAKERS",
                "POTTERS & TILEMAKERS",
                "SHIPWRIGHTS & SAILMAKERS",
                "SMITHS AND METAL-FORGERS",
                "TINKERS, PEWTERERS, & CASTERS",
                "WAGON-MAKERS & WHEELWRIGHTS",
                "WEAVERS & DYERS",
                "WOODCARVERS, COOPERS, & BOWYERS"
                ]
        chosen_biz = get_item(guild_biz)
        chosen_bg = "GUILD ARTISAN ({0})".format(chosen_biz)

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("GUILD MEMBERSHIP: Find a place to stay / eat with guild members")
        bg_features.append("     : Centralized place in cities to meet other guild members.")
        bg_features.append("     : Must pay 5g / month to keep up dues")
        bg_features.append("     : Access to political figures, legal defense")
        bg_features.append("")
        
        background_skills("INSIGHT", "PERSUASION")

        biz_toolkits = {
            "ALCHEMISTS & APOTHECARIES" : "ALCHEMIST'S SUPPLIES",
            "ARMORERS, LOCKSMITHS, & FINESMITHS" : "SMITH'S TOOLS",
            "BREWERS, DISTILLERS, & VINTNERS" : "BREWER'S SUPPLIES",
            "CALLIGRAPHERS, SCRIBES, & SCRIVENERS" : "CALLIGRAPHER'S SUPPLIES",
            "CARPENTERS, ROOFERS, & PLASTERERS" : "CARPENTER'S TOOLS",
            "CARTOGRAPHERS, SURVEYORS, & CHART-MAKERS" : "CARTOGRAPHER'S TOOLS",
            "COBBLERS & SHOEMAKERS" : "COBBLER'S TOOLS",
            "COOKS & BAKERS" : "COOK'S UTENSILS",
            "GLASSBLOWERS & GLAZERS" : "GLASSBLOWER'S TOOLS",
            "JEWELERS & GEMCUTTERS" : "JEWELER'S TOOLS",
            "LEATHERWORKERS, SKINNERS, & TANNERS" : "LEATHERWORKER'S TOOLS",
            "MASONS & STONECUTTERS" : "MASON'S TOOLS",
            "PAINTERS, LIMNERS, & SIGN-MAKERS" : "PAINTER'S SUPPLIES",
            "POTTERS & TILEMAKERS" : "POTTER'S TOOLS",
            "SMITHS AND METAL-FORGERS" : "SMITH'S TOOLS",
            "TINKERS, PEWTERERS, & CASTERS" : "TINKER'S TOOLS",
            "WAGON-MAKERS & WHEELWRIGHTS" : "CARPENTER'S TOOLS",
            "WEAVERS & DYERS" : "WEAVER'S TOOLS",
            "WOODCARVERS, COOPERS, & BOWYERS" : "WOODCARVER'S TOOLS",
            }
        get_proficiency(biz_toolkits[chosen_biz], tools)
        
        inventory.append("Letter of Introduction from the Guild")
        inventory.append("Traveler's Clothes")
        inventory.append("Belt pouch with 15g")

        bg_trait = [
                    "Anything worth doing is worth doing right.",
                    "I look down on people who can't appreciate fine craftmanship.",
                    "I always want to know how something works / what it's made of.",
                    "I have witty aphorism and proverbs for every situation.",
                    "I can't abide a lack of work ethic or commitment to fair play.",
                    "I can and will talk about the details of my profession as long as someone will let me.",
                    "I will haggle endlessly to make sure I get the best price.",
                    "I've enjoyed some fame from my work, and I expect everyone to know who I am."
                    ]
        bg_ideal = [
                    "A civilized society requires constant work to strengthen communal bonds.",
                    "I was given this talent in order to improve the lives of people across the land.",
                    "Everyone should be free to pursue their own livelihood.",
                    "I'm just in it for the money, and quality work ain't cheap.",
                    "My friends and family are more important than any high-falutin 'ideals'.",
                    "I'm the best at what I do because I never stop working at it."
                    ]
        bg_bond = [
                    "The workshop where I learned my trade was destroyed and I wll avenge its loss.",
                    "I created a masterpiece, and am still looking for someone worthy of it.",
                    "My guild saved my life by turning me into who I am today. I owe them everything.",
                    "I pursue excellence in my craft to impress a special someone.",
                    "My hometown guild lacked confidence in me, and I will prove them wrong.",
                    "I uncovered corruption in the upper levels of my guild and I must bring it to light."
                    ]
        bg_flaw = [
                    "I'd do anything to get my hands on something rare or valuable.",
                    "I'm quick to assume someone is trying to cheat me.",
                    "I've been stealing gold from my guild's coffers for years.",
                    "I'm never satisfied with what I have. I'm always looking for more.",
                    "I would do anything for a title of nobility. Anything.",
                    "I'm horribly bitter towards anyone that exhibits a strong skill in my profession."
                    ]

        get_quirks()

    if chosen_bg == "HERMIT":

        life_of_seclusion = [
                    "SPIRITUAL ENLIGHTENMENT",
                    "COMMUNAL LIVING",
                    "EXILE",
                    "PERSONAL TRAGEDY",
                    "ARTISTIC FREEDOM",
                    "COMMUNION WITH NATURE",
                    "RELIC PROTECTOR",
                    "SITE EXPLORER"
                    ]
        chosen_life = get_item(life_of_seclusion)
        chosen_bg = "HERMIT ({0})".format(chosen_life)

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("DISCOVERY: Gain access to a unique and powerful discovery.")
        bg_features.append("         : It could be a great truth about the cosmos,")
        bg_features.append("         : a site no one has ever seen, or a fact long forgotten.")
        bg_features.append("         : DM will help determine something relevant to campaign.")
        bg_features.append("")
        
        background_skills("MEDICINE", "PERSUASION")

        get_proficiency("GET", languages)
        get_proficiency("HERBALISM KIT", tools)

        inventory.append("Herbalism Kit")
        inventory.append("Common Clothes")
        inventory.append("Winter Blanket")
        inventory.append("Scroll Case of notes from Studies")
        inventory.append("Purse with 25g")

        bg_trait = [
                    "I rarely speak, preferring occasional grunts or growls.",
                    "I am utterly serene, even in the face of disaster.",
                    "I am eager to share the wisdom of my spiritual leader/idol.",
                    "I feel tremendous empathy for all who suffer.",
                    "I am oblivious to social expectations and etiquette.",
                    "I connect every minor event to a grand cosmic plan.",
                    "I often get lost in my own thoughts, oblivious to my surroundings.",
                    "I am working on a grand philosophical theory and love sharing it."
                    ]
        bg_ideal = [
                    "I work for the greater good and not my own benefit.",
                    "Emotions should not cloud our logical judgement.",
                    "Curiosity is the pillar of progress.",
                    "I chose my life in order to attain great knowledge, and with it, power.",
                    "Meddling in the affairs of others only brings trouble.",
                    "To truly know oneself is the greatest challenge of all."
                    ]
        bg_bond = [
                    "Nothing is more important than the other members of my order.",
                    "I must confront those who.",
                    "I was harassed by a proud noble growing up, and I take my revenge on any bully I see.",
                    "I carry the tools of my old profession to remind me of my roots.",
                    "No person belongs in chains, and I will break any and every shackle I see.",
                    "My hometown sweetheart is my motivation in all I do."
                    ]
        bg_flaw = [
                    "The tyrant who rules my land will stop at nothing to see me dead.",
                    "I'm blind to any risk of failure, as it is my destiny to succeed.",
                    "I have a shameful secret that keeps me from returning home.",
                    "I have a weakness for the vices of the big city, especially fine food and drink.",
                    "I seek to overthrow the current rulers only so I can usurp the throne myself.",
                    "I have little trust in my allies."
                    ]

        get_quirks()

    if chosen_bg == "NOBLE":

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("POSITION OF PRIVELEGE: You are welcome in High Society.")
        bg_features.append("       : People assume you have the right to be wherever you are.")
        bg_features.append("       : Common folk make every accomodation possible for you.")
        bg_features.append("       : You can secure audience with another local noble.")
        bg_features.append("")
        
        background_skills("HISTORY", "PERSUASION")

        get_proficiency("GET", gaming_sets)
        get_proficiency("GET", languages)

        inventory.append("Fine Clothes")
        inventory.append("Signet Ring")
        inventory.append("Scroll of pedigree")
        inventory.append("Purse with 25g")

        bg_trait = [
                    "I make my status known by being overly-flattering towards everyone.",
                    "I am beloved by the common folk for my generosity.",
                    "No amount of pressure breaks my cool, calm composure.",
                    "I don't just follow the current fashions, I create them.",
                    "I am horrified by anything less than luxury.",
                    "I know that our class does not determine our worth. We all bleed the same.",
                    "I may forgive, but I never forget.",
                    "If anyone gets in my way, I will wipe their entire family from existence."
                    ]
        bg_ideal = [
                    "All people deserve respect regardless of station.",
                    "I deserve respect from the commoners just as I respect my betters.",
                    "My family is more than just my name-- they're my whole world.",
                    "It is my duty as nobility to protect and defend the common man.",
                    "Meddling in the affairs of others only brings trouble.",
                    "To truly know oneself is the greatest challenge of all."
                    ]
        bg_bond = [
                    "I must prove that I can survive without my coddling parents.",
                    "I seek to create/preserve an alliance between my family and a great power.",
                    "I am in love with a member of a rival family.",
                    "My loyalty to my sovereign is unwavering.",
                    "I must earn the respect that is given to me by become a hero of the people.",
                    "My family is secretly on the verge of ruin; their fate is in my hands."
                    ]
        bg_flaw = [
                    "I believe that I am innately superior to those around me.",
                    "I was at the center of a major scandal that shamed my family.",
                    "I'm quick to anger when insulted, and I'm quick to take offense as well.",
                    "I don't ever think of anyone else's needs. It just dosn't occur to me.",
                    "I have an insatiable desire for carnal vices.",
                    "I am insanely racist about one particular common race."
                    ]

        get_quirks()

    if chosen_bg == "OUTLANDER":

        outlander_origin = [
                    "FORESTER",
                    "TRAPPER",
                    "HOMESTEADER",
                    "GUIDE",
                    "EXILE/OUTCAST",
                    "BOUNTY HUNTER",
                    "PILGRIM",
                    "TRIBAL NOMAD",
                    "HUNTER-GATHERER",
                    "TRIBAL MARAUDER"
                    ]
        char_origin = get_item(outlander_origin)
        chosen_bg = "OUTLANDER ({0})".format(char_origin)

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("WANDERER: Excellent memory for geography and maps,")
        bg_features.append("    : Recall the general layout of terrain / settlements")
        bg_features.append("    : Find food / fresh water for 5 people /day")
        bg_features.append("")
        
        background_skills("ATHLETICS", "SURVIVAL")

        get_proficiency("GET", instruments)
        get_proficiency("GET", languages)

        inventory.append("STAFF")
        inventory.append("HUNTING TRAP")
        inventory.append("ANIMAL TROPHY")
        inventory.append("TRAVELER'S CLOTHES")
        inventory.append("BELT POUCH W/ 10g")

        bg_trait = [
                "A strong sense of wanderlust is what sent me from home.",
                "I watch over my allies like they were newborn pups.",
                "When I get in the zone, nothing breaks my concentration.",
                "I have a lesson drawn from nature for every situation.",
                "I place no stock in wealth or manners. They won't save you from a bear.",
                "I'm always fiddling with things, and then breaking them.",
                "I am far more comfortable with animals than people.",
                "I have a totem animal that I take very seriously."
                ]
        bg_ideal = [
                "Life is like the seasons, constantly changing, and we must change with it.",
                "It is our responsibility to make our world better for everything in it.",
                "Honor the laws of nature, and everything else will fall in place.",
                "In nature, only the strong survives.",
                "The natural world must be protected, even at the expense of civilization.",
                "I seek fame and glory for my clan."
                ]
        bg_bond = [
                "My clan is counting on me to return with something of great value.",
                "I seek to avenge the destruction of nature by civilization.",
                "My homeland was ravaged by evildoers and I will destroy them.",
                "I am the last of my tribe, and it is up to me to ensure they are remembered.",
                "I have seen terrible visions of a coming disaster and I must stop it.",
                "I have my eye on a particularly challenging bounty, and I will collect."
                ]
        bg_flaw = [
                "I am very keen on wine, ale, or any intoxicant.",
                "There's no room for caution in a life lived to its fullest.",
                "I nurse a silent resentment towards anyone who's ever insulted me.",
                "I am slow to trust other bgs or tribe members.",
                "Violence is always the answer.",
                "Don't expect me to save those who won't save themselves."
                ]
        
        get_quirks()

    if chosen_bg == "SAGE":

        sage_specialty = [
                    "ALCHEMIST",
                    "ASTRONOMER",
                    "DISCREDITED ACADEMIC",
                    "LIBRARIAN",
                    "PROFESSOR",
                    "RESEARCHER",
                    "WIZARD'S APPRENTICE",
                    "SCRIBE",
                    ]
        chosen_specialty = get_item(sage_specialty)
        chosen_bg = "SAGE ({0})".format(chosen_specialty)

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("RESEARCHER: If you don't know something, you know where to find it.")
        bg_features.append("          : DM will determine what you have to do to get there")
        bg_features.append("")

        background_skills("ARCANA", "HISTORY")

        for i in range(2):
            get_proficiency("GET", languages)

        inventory.append("Bottle of black ink")
        inventory.append("Quill")
        inventory.append("Small knife")
        inventory.append("Letter from a Dead Colleague")
        inventory.append("Common clothes")
        inventory.append("Belt Pouch with 10g")

        bg_trait = [
                "I use polysyllabic words to convey the impression of erudition.",
                "I've read every book in the library and can tell you a little about anything.",
                "I have no problem patiently explaining any advanced concept.",
                "I jump at the chance to solve any kind of mystery.",
                "I must listen to all sides of any argument before coming to a conclusion.",
                "I speak to people as if they were five year olds.",
                "I am terribly awkward in social situations.",
                "I am convinced that people are trying to steal my secrets."
                ]
        bg_ideal = [
                "The path to self-improvement is through knowledge.",
                "What is beautiful points us beyond itself to what is true.",
                "Emotions must not cloud our logical thinking.",
                "Nothing should fetter the inifinite possibility inherent in existence.",
                "Knowledge is the best way to power and domination.",
                "Those who don't study history are doomed to repeat it."
                ]
        bg_bond = [
                "I must protect / avenge my students.",
                "I must not let this ancient text fall into the wrong hands.",
                "I work to preserve / protect an ancient library/university/monastery",
                "I dedicated my life to the study of a particular set of tomes.",
                "I've been searching for the answer to a specific question.",
                "I sold my soul for knowledge and I must redeem myself."
                ]
        bg_flaw = [
                "I am easily distracted by the promise of information.",
                "I will get too busy taking notes on a new creature to realize it's hostile.",
                "I would burn a civilization to the ground to unlock an ancient mystery.",
                "I overlook obvious solutions while I come up with a complex theory.",
                "I have no filter whatsoever.",
                "I can't keep a secret to save my life."
                ]
        
        get_quirks()

    if chosen_bg == "SAILOR":

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("SHIP'S PASSAGE: Can secure free passage on a ship for you and allies")
        bg_features.append("              : Expected to assist the crew during journey")
        bg_features.append("")
        
        background_skills("ATHLETICS", "PERCEPTION")

        get_proficiency("NAVIGATOR'S TOOLS", tools)
        get_proficiency("Vehicles (WATER)")

        inventory.append("BELAYING PIN (CLUB)")
        inventory.append("SILK ROPE (50ft)")
        inventory.append("LUCKY CHARM (Trinket)")
        inventory.append("COMMON CLOTHES")
        inventory.append("BELT POUCH W/ 10g")

        bg_trait = [
                "My crew knows they can rely on me, no matter what.",
                "I work hard so that I can play hard at the end of the day.",
                "I'm always willing to make a new friend over a flagon of ale.",
                "I often stretch the truth in the interest of a good story.",
                "No better way to introduce yourself to a new city than a good tavern brawl.",
                "I never pass up a friendly wager.",
                "I've picked up several foreign curse words in my travels and use them often.",
                "If you want it done right, you have to do it yourself."
                ]
        bg_ideal = [
                "Mutual respect between Captain and Crew makes a ship sail smoothly.",
                "Everyone who shares in the work gets a piece of the reward.",
                "The sea represents freedom to go where you want and do what you wish.",
                "I'm a predator, and the sea is my hunting ground.",
                "I'm committed to my crew, not to any principles.",
                "My Captain has my absolute loyalty, and I expect the same from my crew."
                ]
        bg_bond = [
                "Someday I'll own my own ship and chart my own destiny.",
                "My last crew mutinied and stole my ship, and I will get it back or sink it trying.",
                "There's a certain someone in a harbor town that I hope to see again someday.",
                "I was cheated out of a bounty, and I will get my due.",
                "Pirates raided my ship and killed my crew, and I will be revenged.",
                "I have a map to a buried treasure that no one but me knows about."
                ]
        bg_flaw = [
                "I'll follow orders even if I know they're wrong.",
                "I'll say or do anything to get out of physical labor.",
                "If my courage is in question, I will do literally anything.",
                "Once I start drinking, I don't stop until I'm unconscious.",
                "I pocket any loose change or trinkets I find sitting around.",
                "I always have to one-up anyone's tale of courage or daring."
                ]
        
        get_quirks()

    if chosen_bg == "SOLDIER":

        soldier_rank = [
                    "OFFICER",
                    "SCOUT",
                    "INFANTRY",
                    "CAVALRY",
                    "HEALER",
                    "QUARTERMASTER",
                    "STANDARD-BEARER",
                    "SUPPORT STAFF",
                    ]
        chosen_rank = get_item(soldier_rank)
        chosen_bg = "SOLDIER ({0})".format(chosen_rank)

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("MILITARY RANK: Fellow soldiers recognize your authority/influence")
        bg_features.append("             : Gain access to friendly military encampments/fortresses")
        bg_features.append("")

        background_skills("ATHLETICS", "INTIMIDATION")

        get_proficiency("GET", gaming_sets)

        get_proficiency("Vehicles (LAND)")

        inventory.append("Insignia of Rank")
        inventory.append("Trophy from a Fallen Enemy")
        inventory.append("Common clothes")
        inventory.append("Belt Pouch with 10g")

        bg_trait = [
                "I'm ever polite and respectful to anyone I meet.",
                "I'm haunted by memories of war and violence.",
                "I've lost too many friends to bother making new ones.",
                "I have a harrowing tale of combat for any situation.",
                "I'll stare down an Elder Dragon without flinching.",
                "I love the feel of breaking things with my hands.",
                "I have peculiar sense of humor that no one else seems to share.",
                "The simplest, most direct course of action is always the best."
                ]
        bg_ideal = [
                "I risk my life to keep others safe.",
                "A strict code of honor and chain of command is essential to civilization.",
                "When people follow orders blindly, they embbg tyranny.",
                "Might makes right.",
                "I don't fight for ideals, I just love to hit and get hit back.",
                "My city/nation and the people in it are all that matters."
                ]
        bg_bond = [
                "I was sent on a secret mission to retrieve something.",
                "I never leave a man behind on the battlefield.",
                "I would do anything to preserve my honor.",
                "I made a mistake that cost many lives, and I won't let that happen again.",
                "I will not rest until every enemy lays dead.",
                "I will not abide someone preying on the weak."
                ]
        bg_flaw = [
                "I have an unreasonable fear of a certain type of beast.",
                "I have little respect for civilians who have never tasted battle.",
                "I have killed to keep a terrible secret hidden, and I will again if need be.",
                "I obey the law no matter who suffers as a result.",
                "I will literally never admit that I'm wrong.",
                "I will hit on anything remotely attractive to me."
                ]

        get_quirks()

    if chosen_bg == "URCHIN":

        bg_features.append(chosen_bg)
        bg_features.append("")
        bg_features.append("CITY SECRETS: Know secret patterns and flows to cities")
        bg_features.append("       : Travel 2x as fast through city outside combat")
        bg_features.append("")
        
        background_skills("SLEIGHT OF HAND", "STEALTH")

        get_proficiency("DISGUISE KIT", tools)
        get_proficiency("THIEVES' TOOLS", tools)

        inventory.append("Small knife")
        inventory.append("Map of the city you grew up in")
        inventory.append("Pet mouse")
        inventory.append("Token from your parents")
        inventory.append("Common clothes")
        inventory.append("Belt Pouch with 10g")

        bg_trait = [
                "I hide scraps of food and trinkets in my pockets.",
                "I ask questions about EVERYTHING.",
                "I have to explore every nook and cranny I find.",
                "I can only #sleep in a well-protected area with all my belongings close by.",
                "I eat with my hands and very noisily.",
                "I distrust anyone I don't know that approaches me as a friend.",
                "I'm not a fan of bathing.",
                "I have no filter to my thoughts."
                ]
        bg_ideal = [
                "We all deserve respect regardless of class.",
                "We have to take care of each other so we all prosper.",
                "The low are lifted up, and the mighty brought down. Change is natural.",
                "We must show the rich what it's really like to go without.",
                "I help people that help me, and I kill those that hurt me.",
                "I will steal a better life if I can't make it myself."
                ]
        bg_bond = [
                "No one knows my city like I do, and I will fight to defend it.",
                "A piece of my loot always goes to the orphanage I grew up in.",
                "I was cast aside by my noble family, and I will be revenged.",
                "I was taken in by someone and I have pledged my life to them.",
                "I can't watch somoene go hungry without doing something to help.",
                "I fought tooth and nail to get what I've got an no one is taking it from me."
                ]
        bg_flaw = [
                "I will run away if the odds are against me.",
                "I would do anything for a bit of gold.",
                "I don't fully trust anyone but myself.",
                "I would stab someone in the back before facing them head on every time.",
                "It's not stealing if I need it more than they do.",
                "People who can't defend themselves deserve to get trampled on."
                ]

        get_quirks()

    return chosen_bg
 
print (get_bg())
print ()

char_history = []
def get_story():

    birthplaces = [
        "at home",
        "at the home of a family friend",
        "at the home of a healer or midwife",
        "in a carriage, cart, or wagon",
        "in a barn, shed, or other outbuilding",
        "in a cave",
        "in a field",
        "in a forest",
        "in a temple",
        "on a battlefield",
        "in an alley or street",
        "in a brothel",
        "in a tavern or inn",
        "in a castle, keep, tower, or palace",
        "in a sewer or rubbish heap",
        "among people of a difierent race",
        "on board a boat or a ship",
        "in a prison",
        "in the headquarters of a secret organization",
        "in a sage’s laboratory",
        "in the Feywild",
        "in the Shadowfell",
        "on the Astral Plane",
        "on the Ethereal Plane",
        "on an Inner Plane (Air, Earth, Fire, Water)",
        "on an Outer Plane (Upper, Lower, Law, Chaos)"
        ]
    family = [
        "no one",
        "an institution or asylum",
        "a temple",
        "an orphanage",
        "a guardian",
        "your extended family",
        "your tribe or clan",
        "your grandparents",
        "an adoptive family",
        "a single father",
        "your mother and stepfather",
        "a single mother",
        "your father and stepmother",
        "your mother and father",
        ]
    occupations = [
                "an academic",
                "an adventurer",
                "an aristocrat",
                "an artisan/guild member",
                "a criminal",
                "an entertainer",
                "an exile/hermit/refugee",
                "an explorer/wanderer",
                "a farmer/herder",
                "a hunter/trapper",
                "a laborer",
                "a merchant",
                "a politician/bureaucrat",
                "a priest",
                "a sailor",
                "a soldier",
                ]
    causes_of_death = [
        "under mysterious circumstances",
        "trying to prevent a crime",
        "in battle",
        "in an accident",
        "of natural causes",
        "of apparent suicide",
        "in a wild animal attack",
        "in a natural disaster",
        "in a monster attack.",
        "in jail / by execution",
        "in a bizarre, once-in-a-lifetime event."
        ]
    absent_parent = [
            "died",
            "went to prison/a slave camp",
            "abandoned you",
            "disappeared without explanation"
            ]
    lifestyles = [
        "wretched",
        "squalid",
        "poor",
        "modest",
        "comfortable",
        "wealthy",
        "aristocratic",
        ]
    lifestyle_bonus = {
        "wretched" : -40,
        "squalid" : -20,
        "poor" : -10,
        "modest" : 0,
        "comfortable" : 10,
        "wealthy" : 20,
        "aristocratic" : 40
        }

    chosen_parents = randint(1,100)
    if chosen_parents >= 96:
        chosen_parents = "You do not know who your parents were."
    else:
        chosen_mother = get_item(occupations)
        chosen_father = get_item(occupations)
        chosen_parents = "Your mother was {0} and your father was {1}.".format(chosen_mother, chosen_father)     
    
    chosen_birthplace = get_item(birthplaces)
    chosen_birthplace = "You were born {0}.".format(chosen_birthplace)
    
    char_history.append(chosen_parents)
    char_history.append(chosen_birthplace)
    char_history.append("")

    chosen_family = get_item(family)
    
    if chosen_family != "your mother and father":
        
        chosen_absence = get_item(absent_parent)

        if chosen_absence == "died":
            cause_of_death = get_item(causes_of_death)
            chosen_absence = "died {0}".format(cause_of_death)

        if chosen_family == "your father and stepmother" or chosen_family == "a single father":
            chosen_absence = "your mother {0}".format(chosen_absence)
        elif chosen_family == "your mother and stepfather" or chosen_family == "a single mother":
            chosen_absence = "your father {0}".format(chosen_absence)
        else:
            chosen_absence = "your parents {0}".format(chosen_absence)

        chosen_family = "You were raised by {0} after {1}.".format(chosen_family, chosen_absence)            
    else:
        chosen_family = "You were raised by {0}.".format(chosen_family)
    
    char_history.append(chosen_family)
    char_history.append("")

    num_siblings = randint(1,10)
    if num_siblings < 3:
        num_siblings = 0
    elif num_siblings < 5:
        num_siblings = randint(1,2)
    elif num_siblings < 7:
        num_siblings = randint(1,2) + 1
    elif num_siblings < 9:
        num_siblings = randint(1,3) + 1
    else:
        num_siblings = randint(1,2) + 2
    
    sibling_names = []

    def get_sibling():

        birth_order = randint(1,6) + randint(1,6)
        if birth_order < 3:
            birth_order = "a twin"
        elif birth_order < 8:
            birth_order = "an older"
        else:
            birth_order = "a younger"        
                    
        gender = randint(1,2)
        if gender == 1:
            gender = "brother"
        else:
            gender = "sister"

        sibling = birth_order + " " + gender
        sibling_names.append(sibling)

        relationship = randint(1,4) + randint(1,4) + randint(1,4)
        if relationship < 5:
            relationship = "hostile"
        elif relationship < 11:
            relationship = "friendly"
        else:
            relationship = "indifferent"
        
        sib_story = "You have {0} {1} to whom you are {2}.".format(birth_order, gender, relationship)
        char_history.append(sib_story)

        occupation = get_item(occupations)

        status = randint(1,6) + randint(1,6) + randint(1,6)
        if status < 6:
            status = "dead"
        elif status < 9:
            status = "missing / whereabouts unknown"
        elif status < 13:
            status = "alive, but doing poorly"
        elif status < 17:
            status = "alive and well"
        else:
            status = "alive and quite successfull"

        if status == "dead":
            cause_of_death = get_item(causes_of_death)
            sib_status = "They were {0}, but they died {1}".format(occupation, cause_of_death)
        else:
            sib_status = "They are {0} and currently {1}.".format(occupation, status)
    
        char_history.append(sib_status)
        char_history.append("") 

    while len(sibling_names) < num_siblings:
        get_sibling()
    
    if len(sibling_names) == 0:
        char_history.append("You were an only child.")
        char_history.append("")

    chosen_lifestyle = get_item(lifestyles)
    childhood_home = randint(1,100) + lifestyle_bonus[chosen_lifestyle]
    if childhood_home < 1:
        childhood_home = "on the streets"
    elif childhood_home < 21:
        childhood_home = "in a run-down shack"
    elif childhood_home < 31:
        childhood_home = "on the move, never settling down"
    elif childhood_home < 41:
        childhood_home = "in an encampment or village in the wilderness"
    elif childhood_home < 51:
        childhood_home = "in an apartment"
    elif childhood_home < 71:
        childhood_home = "in a small house"
    elif childhood_home < 91:
        childhood_home = "in a large house"
    elif childhood_home < 111:
        childhood_home = "in a mansion"
    else:
        childhood_home = "in a palace or castle"
    family_lifestyle = "Your family's lifestyle was {0}, and you grew up {1}.".format(chosen_lifestyle, childhood_home)
    
    child_memories = randint(1,6) + randint(1,6) + randint(1,6) + ability_modifiers["CHARISMA"]
    if child_memories < 4:
        child_memories = "You are still haunted by your childhood, when you were treated badly by your peers."
    elif child_memories < 6:
        child_memories = "You spent most of your childhood alone, with no close friends."
    elif child_memories < 9:
        child_memories = "Others saw you as being diiferent or strange, and so you had few companions."
    elif child_memories < 13:
        child_memories = "You had a few close friends and lived an ordinary childhood."
    elif child_memories < 16:
        child_memories = "You had several friends, and your childhood was generally a happy one."
    elif child_memories < 18:
        child_memories = "You always found it easy to make friends, and you loved being around people."
    else:
        child_memories = "Everyone knew who you were, and you had friends everywhere you went."
    
    char_history.append(family_lifestyle)
    char_history.append(child_memories)
    char_history.append("")

get_story()
    
###
#       FINAL FEATURE LISTS / CHARACTER SHEET
###

#sleep(1)
print ("----------------------------")
print ("ATTRIBUTES / MODIFIERS: ")
print ("----------------------------")
print ()
#sleep(1)

for item in ability_scores:
    if ability_modifiers[(item)] > 0:
        print ("{0}: {1} (Mod: +{2})".format(item, ability_scores[item], ability_modifiers[item]))
    else:
        print ("{0}: {1} (Mod: {2})".format(item, ability_scores[item], ability_modifiers[item]))
    print ()
    ##sleep(1)

print ("----------------------------")
print ("SKILL CHECK BONUS: ")
print ("----------------------------")
print ()
#sleep(1)

for skill in skill_modifiers:
    skill_modifiers[skill] += ability_modifiers[skill_to_ability[skill]]

    if skill_modifiers[skill] != 0:                               
        if skill_modifiers[skill] > 0:                                     
            print ("{0}: +{1}".format(skill, skill_modifiers[(skill)]))     
        else:
            print ("{0}: {1}".format(skill, skill_modifiers[(skill)]))
        #sleep(1)

print ()
print ("----------------------------")
print ("RACIAL FEATURES:")
print ("----------------------------")
print ()
#sleep(1)

for item in race_features:
    print (item)
    ##sleep(1)

print ()
print ("----------------------------")
print ("CLASS FEATURES:")
print ("----------------------------")
print ()
#sleep(1)

for item in class_features:
    print (item)
    #sleep(1)

print ()
print ("----------------------------")
print ("BACKGROUND FEATURES:")
print ("----------------------------")
print ()
#sleep(1)

for item in bg_features:
    print (item)
    #sleep(1)

print ()
print ("----------------------------")
print ("CHARACTER HISTORY:")
print ("----------------------------")
print ()
#sleep(1)

for item in char_history:
    print (item)
    #sleep(1)

print ()
print ("----------------------------")
print ("PROFICIENCIES: ")
print ("----------------------------")
print ()
#sleep(1)

# proficiencies = unique_everseen(proficiencies)
proficiencies = sorted(proficiencies)   # Alphabetize list to sort by type
for item in proficiencies:
    print (item)
    #sleep(1)

print ()
print ("----------------------------")
print ("INVENTORY:")
print ("----------------------------")
print ()
#sleep(1)

for item in inventory:
    print (item)
    #sleep(1)
print ()

if len(spellbook_0) > 2 or len(spellbook_1) > 2:  # Only print Spellbook for Spellcasters
    print ("----------------------------")          
    print ("SPELLBOOK:")                            
    print ("----------------------------")
    print ()
    #sleep(1)

    for book in spellbook:
        for item in book:
            print (item)
        print ()
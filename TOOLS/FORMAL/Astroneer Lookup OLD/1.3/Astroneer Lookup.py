import os, sys, check_version, time

class Resource():
    def __init__(self, name, planets=["ALL"]):
        self.name = name
        self.planets = planets
        self.type = "Resource"

        if "RESOURCES" not in ALL_RESOURCES:
            ALL_RESOURCES["RESOURCES"] = {}

        ALL_RESOURCES["RESOURCES"][self.name] = self

class RefinedResource():
    def __init__(self, name, smeltedFrom):
        self.name = name
        self.type = "Smelted"
        self.smeltedFrom = smeltedFrom

        if "SMELTED_RESOURCES" not in ALL_RESOURCES:
            ALL_RESOURCES["SMELTED_RESOURCES"] = {}

        ALL_RESOURCES["SMELTED_RESOURCES"][self.name] = self

    def render(self):
        resource = self.smeltedFrom.upper()

        for i in ALL_RESOURCES:
            if resource in ALL_RESOURCES[i]:
                self.smeltedFrom = ALL_RESOURCES[i][resource]

                return

        print("ERROR: Smelted resource not found: " + resource)
        sys.exit(1)

class AtmoResource():
    def __init__(self, name, planetsAndPPU):
        self.name = name
        self.planetsAndPPU = planetsAndPPU
        self.type = "Gas"

        if "ATMO_RESOURCES" not in ALL_RESOURCES:
            ALL_RESOURCES["ATMO_RESOURCES"] = {}

        ALL_RESOURCES["ATMO_RESOURCES"][self.name] = self

class CompResource():
    def __init__(self, name, *resources):
        self.name = name
        self.resources = resources
        self.type = "Composite"

        if "COMP_RESOURCES" not in ALL_RESOURCES:
            ALL_RESOURCES["COMP_RESOURCES"] = {}

        ALL_RESOURCES["COMP_RESOURCES"][self.name] = self

    def render(self):
        resources = self.resources

        self.resources = []

        for resource in resources:
            resource = resource.upper()

            for i in ALL_RESOURCES:
                if resource in ALL_RESOURCES[i]:
                    self.resources.append(ALL_RESOURCES[i][resource])

class Object():
    def __init__(self, name, bytes=0, tier=1, *resources):
        self.name = name
        self.resources = resources
        self.bytes = bytes
        self.tier = tier
        self.type = "Object / Building"

        if "BUILDINGS" not in ALL_RESOURCES:
            ALL_RESOURCES["BUILDINGS"] = {}

        ALL_RESOURCES["BUILDINGS"][self.name] = self

    def render(self):
        resources = self.resources

        self.resources = []

        for resource in resources:
            resource = resource.upper()

            for i in ALL_RESOURCES:
                if resource in ALL_RESOURCES[i]:
                    self.resources.append(ALL_RESOURCES[i][resource])

ALL_RESOURCES = {}

    
# All Resources
# From all planets
Resource("SOIL")
Resource("ORGANIC")
Resource("COMPOUND")
Resource("RESIN")
Resource("CLAY")
Resource("QUARTZ")
Resource("AMMONIUM")
Resource("GRAPHITE")
Resource("LATERITE")
Resource("ASTRONIUM")

# From specific planets
# ---- Organized - Used for official changes to the codebase ----
# Resource("SOIL",     ["EARTH",   "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE"])
# Resource("WATER",    ["EARTH",   "MARS", "SATURN",  "URANUS", "NEPTUNE"])
Resource("SPHALERITE", ["SYLVA",   "DESOLO"])
Resource("WOLFRAMITE", ["DESOLO",  "CALIDOR"])
Resource("MALACHITE",  ["SYLVA",   "CALIDOR"])
Resource("LITHIUM",    ["VESANIA", "NOVUS"])
Resource("HEMATITE",   ["NOVUS",   "GLACIO"])
Resource("TITANITE",   ["VESANIA", "DESOLO"])
# ---- Unorganized - Used for testing and development ----
# -- Add new resources here if you want to avoid the burden of managing looks --
# Resource("SOIL", ["EARTH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE"])
# Resource("WATER", ["EARTH", "MARS", "SATURN", "URANUS", "NEPTUNE"])

# ------------------------------------------------------------------------------

# All Smelted Resources
# ---- Organized - Used for official changes to the codebase ----
# RefinedResource("REFINED SOIL",  "SOIL")
# RefinedResource("REFINED WATER", "WATER")
RefinedResource("CARBON",   "ORGANIC")
RefinedResource("CERAMIC",  "CLAY")
RefinedResource("GLASS",    "QUARTZ")
RefinedResource("ALUMINUM", "LATERITE")
RefinedResource("ZINC",     "SPHALERITE")
RefinedResource("COPPER",   "MALACHITE")
RefinedResource("TUNGSTEN", "WOLFRAMITE")
RefinedResource("IRON",     "HEMATITE")
RefinedResource("TITANIUM", "TITANITE")
# ---- Unorganized - Used for testing and development ----
# -- Add new resources here if you want to avoid the burden of managing looks --
# RefinedResource("REFINED SOIL", ["EARTH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE"])
# RefinedResource("REFINED WATER", ["EARTH", "MARS", "SATURN", "URANUS", "NEPTUNE"])

# ------------------------------------------------------------------------------

# All Gases
# ---- Organized - Used for official changes to the codebase ----
# AtmoResource("RADIATION", {"EARTH": 100, "MARS": 25})
# AtmoResource("OZONE",     {"EARTH": 100})
AtmoResource("HELIUM",   {"ATROX":   25})
AtmoResource("ARGON",    {"GLACIO":  100, "VESANIA": 50})
AtmoResource("METHANE",  {"ATROX":   100, "NOVUS":   75})
AtmoResource("SULFUR",   {"CALIDOR": 100, "ATROX":   75})
AtmoResource("NITROGEN", {"SYLVA":   100, "VESANIA": 75, "ATROX":   50})
AtmoResource("HYDROGEN", {"VESANIA": 100, "SYLVA":   75, "CALIDOR": 50, "NOVUS": 25})
# ---- Unorganized - Used for testing and development ----
# -- Add new resources here if you want to avoid the burden of managing looks --
# AtmoResource("RADIATION", ["EARTH", "MARS"])
# AtmoResource("OZONE", ["EARTH"])

# ------------------------------------------------------------------------------

# All Composite Resources
# ---- Organized - Used for official changes to the codebase ----
# CompResource("GRAPHENE",       "GRAPHITE",       "HYDRAZINE")
# CompResource("DIAMOND",        "GRAPHENE",       "GRAPHENE")
CompResource("RUBBER",           "ORGANIC",        "RESIN")
CompResource("PLASTIC",          "CARBON",         "COMPOUND")
CompResource("ALUMINUM ALLOY",   "ALUMINUM",       "COPPER")
CompResource("TUNGSTEN CARBIDE", "TUNGSTEN",       "CARBON")
CompResource("GRAPHENE",         "GRAPHITE",       "HYDRAZINE")
CompResource("DIAMOND",          "GRAPHENE",       "GRAPHENE")
CompResource("SILICONE",         "RESIN",          "QUARTZ",   "METHANE")
CompResource("EXPLOSIVE POWDER", "CARBON",         "CARBON",   "SULFUR")
CompResource("STEEL",            "IRON",           "CARBON",   "ARGON")
CompResource("TITANIUM ALLOY",   "TITANIUM",       "GRAPHENE", "NITROGEN")
CompResource("NANOCARBON ALLOY", "TITANIUM ALLOY", "STEEL",    "HELIUM")
CompResource("HYDRAZINE",        "AMMONIUM",       "AMMONIUM", "AMMONIUM", "HYDROGEN")
# ---- Unorganized - Used for testing and development ----
# -- Add new resources here if you want to avoid the burden of managing looks --
# CompResource("GRAPHENE", "GRAPHITE", "HYDRAZINE")
# CompResource("DIAMOND", "GRAPHENE", "GRAPHENE")

# ------------------------------------------------------------------------------

# All Buildings
# All Composite Resources
# ---- Organized - Used for official changes to the codebase ----
# CompResource("COMPUTER",       500,  1, "GLASS",            "EXO CHIP")
# CompResource("SUPER COMPUTER", 1000, 3, "NANOCARBON ALLOY", "TITANIUM ALLOY", "EXO CHIP")
# Tier 1
Object("SMALL PRINTER",        0,     1, "COMPOUND")
Object("PACKAGER",             1000,  1, "GRAPHITE")
Object("TETHERS",              0,     1, "COMPOUND")
Object("OXYGEN FILTERS",       0,     1, "RESIN")
Object("OXYGEN TANK",          2000,  1, "GLASS")
Object("PORTABLE OXYGENATOR",  10000, 1, "NANOCARBON ALLOY")
Object("SMALL CANISTER",       0,     1, "RESIN")
Object("BEACON",               0,     1, "QUARTZ")
Object("WORKLIGHT",            0,     1, "COPPER")
Object("GLOWSTICKS",           350,   1, "ORGANIC")
Object("FLOODLIGHT",           2000,  1, "TUNGSTEN")
Object("SMALL GENERATOR",      0,     1, "COMPOUND")
Object("POWER CELLS",          800,   1, "GRAPHITE")
Object("SMALL SOLAR PANEL",    300,   1, "COPPER")
Object("SMALL WIND TURBINE",   300,   1, "CERAMIC")
Object("SMALL BATTERY",        2000,  1, "ZINC")
Object("BOOST MOD",            1000,  1, "ZINC")
Object("WIDE MOD",             1000,  1, "ZINC")
Object("NARROW MOD",           1000,  1, "ZINC")
Object("INHIBITOR MOD",        1000,  1, "ZINC")
Object("ALIGNMENT MOD",        1000,  1, "ZINC")
Object("DRILL MOD 1",          1000,  1, "CERAMIC")
Object("DRILL MOD 2",          2500,  1, "TUNGSTEN CARBIDE")
Object("DRILL MOD 3",          3750,  1, "DIAMOND")
Object("DYNAMITE",             3750,  1, "EXPLOSIVE POWDER")
Object("FIREWORKS",            3750,  1, "EXPLOSIVE POWDER")
Object("SMALL TRUMPET HORN",   1000,  1, "PLASTIC")
Object("HOLOGRAPHIC FIGURINE", 3000,  1, "PLASTIC")
Object("TERRAIN ANALYZER",     2000,  1, "ZINC")
Object("PROBE SCANNER",        3000,  1, "STEEL")
Object("SOLID-FUEL JUMP JET",  5000,  1, "ALUMINUM ALLOY")
Object("HYDRAZINE JET PACK",   15000, 1, "TITANIUM ALLOY")
Object("LEVELING BLOCK",       500,   1, "SMALL CANISTER")
Object("EXO CHIP",             0,     1, "DYNAMITE")
Object("SMALL CAMERA",         2500,  1, "EXO CHIP")
Object("HOVERBOARD",           0,     1, "EXO CHIP")

# Tier 2
Object("TALL STORAGE",                 400,   2, "CERAMIC")
Object("BUTTON REPEATER",              300,   2, "ZINC")
Object("DELAY REPEATER",               1000,  2, "ZINC")
Object("COUNT REPEATER",               1000,  2, "ZINC")
Object("EXTENDERS",                    500,   2, "COPPER")
Object("POWER SWITCH",                 750,   2, "COPPER")
Object("TALL PLATFORM",                750,   2, "CERAMIC")
Object("MEDIUM PLATFORM A",            0,     2, "RESIN")
Object("MEDIUM PLATFORM C",            400,   2, "RESIN")
Object("MEDIUM PLATFORM B",            250,   2, "RESIN",            "RESIN")
Object("MEDIUM PRINTER",               0,     2, "COMPOUND",         "COMPOUND")
Object("OXYGENATOR",                   1800,  2, "ALUMINUM",         "CERAMIC")
Object("MEDIUM SHREDDER",              1250,  2, "IRON",             "IRON")
Object("FIELD SHELTER",                8000,  2, "SILICONE",         "GRAPHENE")
Object("AUTO ARM",                     1500,  2, "ALUMINUM",         "GRAPHITE")
Object("MEDIUM RESOURCE CANISTER",     2000,  2, "PLASTIC",          "GLASS")
Object("MEDIUM FLUID & SOIL CANISTER", 2500,  2, "PLASTIC",          "GLASS")
Object("MEDIUM GAS CANISTER",          4000,  2, "SILICONE",         "GLASS")
Object("POWER SENSOR",                 500,   2, "ZINC",             "COPPER")
Object("STORAGE SENSOR",               750,   2, "ZINC",             "QUARTZ")
Object("BATTERY SENSOR",               750,   2, "ZINC",             "GRAPHITE")
Object("SPLITTER",                     1000,  2, "COPPER",           "GRAPHITE")
Object("MEDIUM GENERATOR",             2000,  2, "ALUMINUM",         "TUNGSTEN")
Object("MEDIUM SOLAR PANEL",           2000,  2, "COPPER",           "GLASS")
Object("MEDIUM GENERATOR",             2500,  2, "ALUMINUM",         "CERAMIC")
Object("MEDIUM BATTERY",               3750,  2, "LITHIUM",          "ZINC")
Object("RTG",                          12500, 2, "NANOCARBON ALLOY", "LITHIUM")
Object("MEDIUM T-PLATFORM",            400,   2, "RESIN",            "RESIN")
Object("MEDIUM STORAGE",               0,     2, "RESIN",            "RESIN")
Object("MEDIUM STORAGE SILO",          3000,  2, "TITANIUM",         "TITANIUM")
Object("ROVER SEAT",                   0,     2, "COMPOUND",         "COMPOUND")
Object("TRACTOR",                      1000,  2, "ALUMINUM",         "ALUMINUM")
Object("TRAILER",                      1500,  2, "COMPOUND",         "ALUMINUM")
Object("MEDIUM BUGGY HORN",            1000,  2, "PLASTIC",          "RUBBER")
Object("PAVER",                        5000,  2, "ALUMINUM ALLOY",   "SILICONE")
Object("DRILL STRENGTH 1",             2500,  2, "CERAMIC",          "TUNGSTEN CARBIDE")
Object("DRILL STRENGTH 2",             5000,  2, "TITANIUM ALLOY",   "TUNGSTEN CARBIDE")
Object("DRILL STRENGTH 3",             7500,  2, "DIAMOND",          "TITANIUM ALLOY")
Object("SOLID FUEL THRUSTER",          500,   2, "ALUMINUM",         "AMMONIUM")
Object("WINCH",                        3750,  2, "EXO CHIP",         "RUBBER")
Object("HYDRAZINE THRUSTER",           3750,  2, "EXO CHIP",         "STEEL")

# Tier 3
Object("BUGGY",                   1500, 3, "COMPOUND",         "ALUMINUM")
Object("RECREATIONAL SPHERE",     4500, 3, "ALUMINUM ALLOY",   "RUBBER")
Object("LARGE EXTENDED PLATFORM", 500,  3, "RESIN",            "RESIN")
Object("LARGE PLATFORM A",        0,    3, "RESIN",            "RESIN")
Object("LARGE PLATFORM B",        500,  3, "RESIN",            "RESIN",    "RESIN")
Object("LARGE PLATFORM C",        1000, 3, "RESIN",            "CERAMIC",  "IRON")
Object("LARGE PRINTER",           0,    3, "COMPOUND",         "COMPOUND", "COMPOUND")
Object("SMELTING FURNACE",        250,  3, "COMPOUND",         "RESIN",    "RESIN")
Object("SOIL CENTRIFUGE",         750,  3, "COMPOUND",         "COMPOUND", "ALUMINUM")
Object("CHEMISTRY LAB",           1600, 3, "CERAMIC",          "GLASS",    "TUNGSTEN")
Object("ATMOSPHERIC CONDENSER",   2200, 3, "PLASTIC",          "GLASS",    "IRON")
Object("RESEARCH CHAMBER",        0,    3, "COMPOUND",         "COMPOUND", "RESIN")
Object("EXO REQUEST PLATFORM",    0,    3, "RESIN",            "RESIN",    "CERAMIC")
Object("LARGE SOLAR PANEL",       4000, 3, "ALUMINUM ALLOY",   "GLASS",    "COPPER")
Object("LARGE WIND TURBINE",      3500, 3, "ALUMINUM ALLOY",   "GLASS",    "CERAMIC")
Object("LARGE T-PLATFORM",        1000, 3, "ALUMINUM",         "ALUMINUM", "RESIN")
Object("LARGE CURVED PLATFORM",   1000, 3, "COMPOUND",         "CERAMIC",  "CERAMIC")
Object("LARGE RESOURCE CANISTER", 5000, 3, "GLASS",            "TITANIUM", "NANOCARBON ALLOY")
Object("LARGE STORAGE",           2000, 3, "CERAMIC",          "CERAMIC",  "CERAMIC")
Object("LARGE STORAGE SILO A",    5000, 3, "ALUMINUM",         "ALUMINUM", "STEEL")
Object("LARGE STORAGE SILO B",    7500, 3, "STEEL",            "STEEL",    "STEEL")
Object("LARGE ACTIVE STORAGE",    2000, 3, "ZINC",             "ALUMINUM", "RESIN")
Object("LARGE ROVER SEAT",        2000, 3, "PLASTIC",          "PLASTIC",  "COMPOUND")
Object("MEDIUM ROVER",            3750, 3, "PLASTIC",          "PLASTIC",  "RUBBER")
Object("CRANE",                   4500, 3, "STEEL",            "SILICONE", "TITANIUM")
Object("LARGE FOG HORN",          4000, 3, "PLASTIC",          "RUBBER",   "STEEL")
Object("TRADE PLATFORM",          2500, 3, "IRON",             "TUNGSTEN", "EXO CHIP")
Object("LARGE SHREDDER",          2500, 3, "TUNGSTEN CARBIDE", "IRON",     "EXO CHIP")
Object("VTOL",                    0,    3, "TUNGSTEN CARBIDE", "SILICONE", "EXO CHIP")

# Tier 4
Object("MEDIUM SENSOR ARCH",          500,  4, "ZINC",             "QUARTZ")
Object("LARGE SENSOR RING",           500,  4, "ZINC",             "QUARTZ")
Object("SMALL SHUTTLE",               1500, 4, "ALUMINUM",         "ALUMINUM")
Object("LARGE SENSOR HOOP A",         750,  4, "ZINC",             "QUARTZ",  "QUARTZ")
Object("LARGE SENSOR HOOP B",         750,  4, "ZINC",             "ZINC",    "QUARTZ")
Object("XL EXTENDED PLATFORM",        750,  4, "RESIN",            "RESIN",   "RESIN")
Object("LANDING PAD",                 750,  4, "ALUMINUM",         "CERAMIC", "CERAMIC")
Object("MEDIUM SHUTTLE",              3750, 4, "ALUMINUM ALLOY",   "CERAMIC", "CERAMIC")
Object("SHELTER",                     0,    4, "PLASTIC",          "PLASTIC", "SILICONE", "SILICONE")
Object("SOLAR ARRAY",                 6000, 4, "COPPER",           "GLASS",   "GRAPHENE", "ALUMINUM ALLOY")
Object("XL WIND TURBINE",             4500, 4, "IRON",             "CERAMIC", "GRAPHENE", "ALUMINUM ALLOY")
Object("XL SENSOR ARCH",              1000, 4, "ZINC",             "ZINC",    "QUARTZ",   "QUARTZ")
Object("XL SENSOR CANOPY",            1000, 4, "ZINC",             "ZINC",    "QUARTZ",   "QUARTZ")
Object("XL SENSOR HOOP A",            750,  4, "ZINC",             "ZINC",    "QUARTZ",   "QUARTZ")
Object("XL SENSOR HOOP B",            1000, 4, "ZINC",             "ZINC",    "ZINC",     "QUARTZ")
Object("EXTRA LARGE PLATFORM A",      2000, 4, "IRON",             "IRON",    "CERAMIC",  "CERAMIC")
Object("EXTRA LARGE PLATFORM B",      3000, 4, "IRON",             "IRON",    "IRON",     "IRON")
Object("EXTRA LARGE PLATFORM C",      2000, 4, "RESIN",            "RESIN",   "IRON",     "IRON")
Object("EXTRA LARGE CURVED PLATFORM", 2000, 4, "CERAMIC",          "CERAMIC", "COMPOUND", "COMPOUND")
Object("FIGURINE PLATFORM",           3000, 4, "IRON",             "IRON",    "IRON",     "IRON")
Object("EXTRA LARGE STORAGE",         2000, 4, "IRON",             "IRON",    "CERAMIC",  "CERAMIC")
Object("AUTO EXTRACTOR",              7500, 4, "TUNGSTEN CARBIDE", "RUBBER",  "STEEL",    "EXO CHIP")
Object("EXTRA LARGE SHREDDER",        5000, 4, "TUNGSTEN CARBIDE", "STEEL",   "EXO CHIP", "EXO CHIP")
Object("LARGE ROVER",                 5000, 4, "ALUMINUM ALLOY",   "RUBBER",  "EXO CHIP", "EXO CHIP")
Object("LARGE SHUTTLE",               5000, 4, "TITANIUM ALLOY",   "CERAMIC", "EXO CHIP", "EXO CHIP")
# ---- Unorganized - Used for testing and development ----
# -- Add new resources here if you want to avoid the burden of managing looks --
# CompResource("COMPUTER", 500, 1, "GLASS", "EXO CHIP")
# CompResource("SUPER COMPUTER", 1000, 3, "NANOCARBON ALLOY", "TITANIUM ALLOY", "EXO CHIP")

# ------------------------------------------------------------------------------


# Parse the resources from the above list into objects instead of strings
# Example:
# Object("LARGE SHUTTLE", 5000, 4, "TITANIUM ALLOY", "CERAMIC", "EXO CHIP", "EXO CHIP")
#                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                  ALL_RESOURCES["COMP_RESOURCES"]["TITANIUM ALLOY"], ALL_RESOURCES["REFINED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["COMP_RESOURCES"]["EXO CHIP"], ALL_RESOURCES["COMP_RESOURCES"]["EXO CHIP"]
for i in ALL_RESOURCES:
    for v in ALL_RESOURCES[i]:
        try:
            ALL_RESOURCES[i][v].render()
        except AttributeError:
            pass

def _tab(t):
    return "    " * t

def get_item_info(tab, times, item):
    return f"{_tab(tab)}{times}{item.name} ({item.type}"

def lookup(item, tab=1, times=""):

    if isinstance(item, Resource): # Is Resource
        return f"{get_item_info(tab - 1, times, item)}):\n{_tab(tab)}Planets: {', '.join(item.planets)}"
    
    elif isinstance(item, RefinedResource): # Is Smelted Resource
        return f"{get_item_info(tab - 1, times, item)}):\n{lookup(item.smeltedFrom, tab + 1)}"
    
    elif isinstance(item, AtmoResource): # Is Atmospheric Resource (aka Gas)
        atmo = ""
        for i in item.planetsAndPPU:
            atmo += f"{_tab(tab)}{i} ({item.planetsAndPPU[i]} PPU),\n"
        return f"{get_item_info(tab - 1, '', item)}):\n{atmo[:-2]}"

    elif isinstance(item, CompResource) or isinstance(item, Object): # Is Composite Resource or Building
        # Check how many of each resource is in item.resources
        # If there is more than one, recursively call lookup() with an 'x2' or 'x3' or whatever the number is
        # If there is only one, recursively call lookup() without any 'x'        
        on_item = 0

        show_tier = ""

        try:
            show_tier = f" | Tier {item.tier}"
        except AttributeError:
            pass

        info = f"{get_item_info(tab - 1, times, item)}{show_tier}):\n"

        resources = item.resources.copy()

        while on_item < len(item.resources):

            try:
                dupe = set([x for x in resources if resources.count(x) > 1]).pop()
            except KeyError:
                info += lookup(resources[0], tab + 1)
                if info.endswith("\n"):
                    info = info[:-1]
                info += "\n"
                on_item += 1

                # Remove element from resources
                try:
                    resources.pop(0)
                except ValueError:
                    pass

                continue

            dupe_num = 0

            for v in resources:
                if v.name == dupe.name:
                    dupe_num += 1

            info += lookup(dupe, tab + 1, f"x{dupe_num} ")[:-1]
            if info.endswith("\n"):
                info = info[:-1]
            info += "\n"
            on_item += dupe_num

            # Remove all instances of the resource with the same name from resources
            for i in range(dupe_num):
                resources.remove(dupe)

        if isinstance(item, Object): info += f"{_tab(tab)}{item.bytes} BYTES"
                
        return info

def clear():
    if sys.platform == "win32": os.system("cls")
    else: os.system("clear")

def close():
    clear()
    print("Goodbye!\n")
    time.sleep(2)
    sys.exit()

def help():
    print("Please wait...")
    # Possible version return values: ["OK", "ERROR", "OUTDATED", "AHEAD"]
    version_return = check_version.run(1.3, "astroneerlookup")

    clear()

    if version_return == "OK":
        print("Astroneer Lookup is up to date!")
    elif version_return == "ERROR":
        print("There was an error checking for updates.")
    elif version_return == "OUTDATED":
        print("Astroneer Lookup is out of date!\nhttps://github.com/Isangedal/Astroneer-Lookup/releases/latest/download/Astroneer.Lookup.exe")
    elif version_return == "AHEAD":
        print("This version of Astroneer Lookup is ahead of the latest release!\nhttps://github.com/Isangedal/Astroneer-Lookup/releases/latest/download/Astroneer.Lookup.exe")
    else:
        print("An impossible error occurred. If you are seeing this, the program has been modified to allow this error to happen.")

    print('\n\nWelcome to Astroneer Lookup!\n\nType a resource name or the name of a building to find out how to make it!\nType "/items" or "/buildings" (without the double quotes) to see which items and buildings you can ask for\nType "/exit" to close the program\nType "/help" to view this message at any time\n\n')

def title():
    if sys.platform == "win32": os.system("title Astroneer Lookup") # How to rename window in windows
    else: print('\33]0;Astroneer Lookup\a', end='', flush=True) # How to rename window in linux/mac

title()
clear()
help()

while True:
    
    req = input("Lookup: ").lower()

    clear()

    if req.startswith("/"): # Commands

        if req == "/items": # Display all items

            for i in ALL_RESOURCES:
                m = f"{i.replace('_', ' ')}:\n"
                for v in ALL_RESOURCES[i]:
                    m += f"    {v.lower().capitalize()}\n"
                print(m)
            print("\n")

        elif req == "/buildings": # Display all buildings

            highest_tier = 1
            lowest_tier = 1

            for i in ALL_RESOURCES["BUILDINGS"]:
                i = ALL_RESOURCES["BUILDINGS"][i]

                if i.tier > highest_tier:
                    highest_tier = i.tier
                if i.tier < lowest_tier:
                    lowest_tier = i.tier

            tier = input("Which tier of buildings do you want to see?\n")

            clear()

            if int(tier) > 4 or int(tier) < 1:
                print(f"Could not find tier \"{tier}\"\nThe available tiers are: {lowest_tier}-{highest_tier}\n\n")
                continue

            print(f"Tier {tier} buildings:\n")
            for i in ALL_RESOURCES["BUILDINGS"]:
                if ALL_RESOURCES["BUILDINGS"][i].tier == int(tier):
                    print(f"{i.lower().capitalize()}")
            print("\n")
                    
        elif req == "/exit": # Exit program
            close()
        
        elif req == "/help": # Display the help message
            help()

        else:
            print("Could not find a command with this name!\n")
            
        continue

    req = req.upper()

    try:
        print(f"RESOURCE FOUND!\n\n{lookup(ALL_RESOURCES[[x for x in ALL_RESOURCES if req in ALL_RESOURCES[x]][0]][req])}\n")
    except:
        print("Could not find a resource with this name!\n")

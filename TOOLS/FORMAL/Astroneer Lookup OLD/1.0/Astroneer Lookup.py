import os,sys,check_version

class Resource():
    def __init__(self, name, planets=["ALL"]):
        self.name = name
        self.planets = planets
        self.type = "Resource"

class RefinedResource():
    def __init__(self, name, smeltedFrom):
        self.name = name
        self.type = "Smelted"
        self.smeltedFrom = smeltedFrom

class AtmoResource():
    def __init__(self, name, planetsAndPPU):
        self.name = name
        self.planetsAndPPU = planetsAndPPU
        self.type = "Gas"

class CompResource():
    def __init__(self, name, res1, res2, gas=None):
        self.name = name
        self.res1 = res1
        self.res2 = res2
        self.gas = gas
        self.type = "Composite"

class Object():
    def __init__(self, name, res1, res2=None, res3=None, res4=None, bytes=0):
        self.name = name
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3
        self.res4 = res4
        self.bytes = bytes
        self.type = "Object / Building"

RESOURCES = {
    # From all planets
    "SOIL": Resource("SOIL"),
    "ORGANIC": Resource("ORGANIC"),
    "COMPOUND": Resource("COMPOUND"),
    "RESIN": Resource("RESIN"),
    "CLAY": Resource("CLAY"),
    "QUARTZ": Resource("QUARTZ"),
    "AMMONIUM": Resource("AMMONIUM"),
    "GRAPHITE": Resource("GRAPHITE"),
    "LATERITE": Resource("LATERITE"),
    "ASTRONIUM": Resource("ASTRONIUM"),

    # From specific planets
    "SPHALERITE": Resource("SPHALERITE", ["SYLVA", "DESOLO"]),
    "WOLFRAMITE": Resource("WOLFRAMITE", ["DESOLO", "CALIDOR"]),
    "MALACHITE": Resource("MALACHITE", ["SYLVA", "CALIDOR"]),
    "LITHIUM": Resource("LITHIUM", ["VESANIA", "NOVUS"]),
    "HEMATITE": Resource("HEMATITE", ["NOVUS", "GLACIO"]),
    "TITANITE": Resource("TITANITE", ["VESANIA", "DESOLO"])
}

SMELTED_RESOURCES = {
    "CARBON": RefinedResource("CARBON", RESOURCES["ORGANIC"]),
    "CERAMIC": RefinedResource("CERAMIC", RESOURCES["CLAY"]),
    "GLASS": RefinedResource("GLASS", RESOURCES["QUARTZ"]),
    "ALUMINUM": RefinedResource("ALUMINUM", RESOURCES["LATERITE"]),
    "ZINC": RefinedResource("ZINC", RESOURCES["SPHALERITE"]),
    "COPPER": RefinedResource("COPPER", RESOURCES["MALACHITE"]),
    "TUNGSTEN": RefinedResource("TUNGSTEN", RESOURCES["WOLFRAMITE"]),
    "IRON": RefinedResource("IRON", RESOURCES["HEMATITE"]),
    "TITANIUM": RefinedResource("TITANIUM", RESOURCES["TITANITE"])
}

ATMO_RESOURCES = {
    "HYDROGEN": AtmoResource("HYDROGEN", {"VESANIA": 100, "SYLVA": 75, "CALIDOR": 50, "NOVUS": 25}),
    "ARGON": AtmoResource("ARGON", {"GLACIO": 100, "VESANIA": 50}),
    "METHANE": AtmoResource("METHANE", {"ATROX": 100, "NOVUS": 75}),
    "NITROGEN": AtmoResource("NITROGEN", {"SYLVA": 100, "VESANIA": 75, "ATROX": 50}),
    "SULFUR": AtmoResource("SULFUR", {"CALIDOR": 100, "ATROX": 75}),
    "HELIUM": AtmoResource("HELIUM", {"ATROX": 25})
}

COMP_RESOURCES_1 = {
    "RUBBER": CompResource("RUBBER", RESOURCES["ORGANIC"], RESOURCES["RESIN"]),
    "PLASTIC": CompResource("PLASTIC", SMELTED_RESOURCES["CARBON"], RESOURCES["COMPOUND"]),
    "ALUMINUM ALLOY": CompResource("ALUMINUM ALLOY", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["COPPER"]),
    "TUNGSTEN CARBIDE": CompResource("TUNGSTEN CARBIDE", SMELTED_RESOURCES["TUNGSTEN"], SMELTED_RESOURCES["CARBON"]),
    "HYDRAZINE": CompResource("HYDRAZINE", RESOURCES["AMMONIUM"], RESOURCES["AMMONIUM"], ATMO_RESOURCES["HYDROGEN"]),
    "SILICONE": CompResource("SILICONE", RESOURCES["RESIN"], RESOURCES["QUARTZ"], ATMO_RESOURCES["METHANE"]),
    "EXPLOSIVE POWDER": CompResource("EXPLOSIVE POWDER", SMELTED_RESOURCES["CARBON"], SMELTED_RESOURCES["CARBON"], ATMO_RESOURCES["SULFUR"]),
    "STEEL": CompResource("STEEL", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["CARBON"], ATMO_RESOURCES["ARGON"]),
}
COMP_RESOURCES_2 = {
    "GRAPHENE": CompResource("GRAPHENE", RESOURCES["GRAPHITE"], COMP_RESOURCES_1["HYDRAZINE"])
}
COMP_RESOURCES_3 = {
    "DIAMOND": CompResource("DIAMOND", COMP_RESOURCES_2["GRAPHENE"], COMP_RESOURCES_2["GRAPHENE"]),
    "TITANIUM ALLOY": CompResource("TITANIUM ALLOY", SMELTED_RESOURCES["TITANIUM"], COMP_RESOURCES_2["GRAPHENE"], ATMO_RESOURCES["NITROGEN"])
}
COMP_RESOURCES_4 = {
    "NANOCARBON ALLOY": CompResource("NANOCARBON ALLOY", COMP_RESOURCES_3["TITANIUM ALLOY"], COMP_RESOURCES_1["STEEL"], ATMO_RESOURCES["HELIUM"])
}

BUILDINGS = {
    # Tier 1
    "SMALL PRINTER": Object("SMALL PRINTER", RESOURCES["COMPOUND"]),
    "PACKAGER": Object("PACKAGER", RESOURCES["GRAPHITE"], bytes=1000),
    "TETHERS": Object("TETHERS", RESOURCES["COMPOUND"]),
    "OXYGEN FILTERS": Object("OXYGEN FILTERS", RESOURCES["RESIN"]),
    "OXYGEN TANK": Object("OXYGEN TANK", SMELTED_RESOURCES["GLASS"], bytes=2000),
    "PORTABLE OXYGENATOR": Object("PORTABLE OXYGENATOR", COMP_RESOURCES_4["NANOCARBON ALLOY"], bytes=10000),
    "SMALL CANISTER": Object("SMALL CANISTER", RESOURCES["RESIN"]),
    "BEACON": Object("BEACON", RESOURCES["QUARTZ"]),
    "WORKLIGHT": Object("WORKLIGHT", SMELTED_RESOURCES["COPPER"]),
    "GLOWSTICKS": Object("GLOWSTICKS", RESOURCES["ORGANIC"], bytes=350),
    "FLOODLIGHT": Object("FLOODLIGHT", SMELTED_RESOURCES["TUNGSTEN"], bytes=2000),
    "SMALL GENERATOR": Object("SMALL GENERATOR", RESOURCES["COMPOUND"]),
    "POWER CELLS": Object("POWER CELLS", RESOURCES["GRAPHITE"], bytes=800),
    "SMALL SOLAR PANEL": Object("SMALL SOLAR PANEL", SMELTED_RESOURCES["COPPER"], bytes=300),
    "SMALL WIND TURBINE": Object("SMALL WIND TURBINE", SMELTED_RESOURCES["CERAMIC"], bytes=300),
    "SMALL BATTERY": Object("SMALL BATTERY", SMELTED_RESOURCES["ZINC"], bytes=2000),
    "BOOST MOD": Object("BOOST MOD", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "WIDE MOD": Object("WIDE MOD", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "NARROW MOD": Object("NARROW MOD", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "INHIBITOR MOD": Object("INHIBITOR MOD", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "ALIGNMENT MOD": Object("ALIGNMENT MOD", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "DRILL MOD 1": Object("DRILL MOD 1", SMELTED_RESOURCES["CERAMIC"], bytes=1000),
    "DRILL MOD 2": Object("DRILL MOD 2", COMP_RESOURCES_1["TUNGSTEN CARBIDE"], bytes=2500),
    "DRILL MOD 3": Object("DRILL MOD 3", COMP_RESOURCES_3["DIAMOND"], bytes=3750),
    "DYNAMITE": Object("DYNAMITE", COMP_RESOURCES_1["EXPLOSIVE POWDER"], bytes=3750),
    "FIREWORKS": Object("FIREWORKS", COMP_RESOURCES_1["EXPLOSIVE POWDER"], bytes=3750),
    "SMALL TRUMPET HORN": Object("SMALL TRUMPET HORN", COMP_RESOURCES_1["PLASTIC"], bytes=1000),
    "HOLOGRAPHIC FIGURINE": Object("HOLOGRAPHIC FIGURINE", COMP_RESOURCES_1["PLASTIC"], bytes=3000),
    "TERRAIN ANALYZER": Object("TERRAIN ANALYZER", SMELTED_RESOURCES["ZINC"], bytes=2000),
    "PROBE SCANNER": Object("PROBE SCANNER", COMP_RESOURCES_1["STEEL"], bytes=3000),
    "SOLID-FUEL JUMP JET": Object("SOLID-FUEL JUMP JET", COMP_RESOURCES_1["ALUMINUM ALLOY"], bytes=5000),
    "HYDRAZINE JET PACK": Object("HYDRAZINE JET PACK", COMP_RESOURCES_3["TITANIUM ALLOY"], bytes=15000),

    # Tier 2
    "MEDIUM PRINTER": Object("MEDIUM PRINTER", RESOURCES["COMPOUND"], RESOURCES["COMPOUND"]),
    "OXYGENATOR": Object("OXYGENATOR", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["CERAMIC"], bytes=1800),
    "MEDIUM SHREDDER": Object("MEDIUM SHREDDER", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], bytes=1250),
    "FIELD SHELTER": Object("FIELD SHELTER", COMP_RESOURCES_1["SILICONE"], COMP_RESOURCES_2["GRAPHENE"], bytes=8000),
    "AUTO ARM": Object("AUTO ARM", SMELTED_RESOURCES["ALUMINUM"], RESOURCES["GRAPHITE"], bytes=1500),
    "MEDIUM RESOURCE CANISTER": Object("MEDIUM RESOURCE CANISTER", COMP_RESOURCES_1["PLASTIC"], SMELTED_RESOURCES["GLASS"], bytes=2000),
    "MEDIUM FLUID & SOIL CANISTER": Object("MEDIUM FLUID & SOIL CANISTER", COMP_RESOURCES_1["PLASTIC"], SMELTED_RESOURCES["GLASS"], bytes=2500),
    "MEDIUM GAS CANISTER": Object("MEDIUM GAS CANISTER", COMP_RESOURCES_1["SILICONE"], SMELTED_RESOURCES["GLASS"], bytes=4000),
    "POWER SENSOR": Object("POWER SENSOR", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["COPPER"], bytes=500),
    "STORAGE SENSOR": Object("STORAGE SENSOR", SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], bytes=750),
    "BATTERY SENSOR": Object("BATTERY SENSOR", SMELTED_RESOURCES["ZINC"], RESOURCES["GRAPHITE"], bytes=750),
    "BUTTON REPEATER": Object("BUTTON REPEATER", SMELTED_RESOURCES["ZINC"], bytes=300),
    "DELAY REPEATER": Object("DELAY REPEATER", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "COUNT REPEATER": Object("COUNT REPEATER", SMELTED_RESOURCES["ZINC"], bytes=1000),
    "EXTENDERS": Object("EXTENDERS", SMELTED_RESOURCES["COPPER"], bytes=500),
    "POWER SWITCH": Object("POWER SWITCH", SMELTED_RESOURCES["COPPER"], bytes=750),
    "SPLITTER": Object("SPLITTER", SMELTED_RESOURCES["COPPER"], RESOURCES["GRAPHITE"], bytes=1000),
    "MEDIUM GENERATOR": Object("MEDIUM GENERATOR", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["TUNGSTEN"], bytes=2000),
    "MEDIUM SOLAR PANEL": Object("MEDIUM SOLAR PANEL", SMELTED_RESOURCES["COPPER"], SMELTED_RESOURCES["GLASS"], bytes=2000),
    "MEDIUM WIND TURBINE": Object("MEDIUM GENERATOR", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["CERAMIC"], bytes=2500),
    "MEDIUM BATTERY": Object("MEDIUM BATTERY", RESOURCES["LITHIUM"], SMELTED_RESOURCES["ZINC"], bytes=3750),
    "RTG": Object("RTG", COMP_RESOURCES_4["NANOCARBON ALLOY"], RESOURCES["LITHIUM"], bytes=12500),
    "MEDIUM PLATFORM A": Object("MEDIUM PLATFORM A", RESOURCES["RESIN"]),
    "MEDIUM PLATFORM B": Object("MEDIUM PLATFORM B", RESOURCES["RESIN"], RESOURCES["RESIN"], bytes=250),
    "MEDIUM PLATFORM C": Object("MEDIUM PLATFORM C", RESOURCES["RESIN"], bytes=400),
    "TALL PLATFORM": Object("TALL PLATFORM", SMELTED_RESOURCES["CERAMIC"], bytes=750),
    "MEDIUM T-PLATFORM": Object("MEDIUM T-PLATFORM", RESOURCES["RESIN"], RESOURCES["RESIN"], bytes=400),
    "MEDIUM STORAGE": Object("MEDIUM STORAGE", RESOURCES["RESIN"], RESOURCES["RESIN"]),
    "MEDIUM STORAGE SILO": Object("MEDIUM STORAGE SILO", SMELTED_RESOURCES["TITANIUM"], SMELTED_RESOURCES["TITANIUM"], bytes=3000),
    "TALL STORAGE": Object("TALL STORAGE", SMELTED_RESOURCES["CERAMIC"], bytes=400),
    "ROVER SEAT": Object("ROVER SEAT", RESOURCES["COMPOUND"], RESOURCES["COMPOUND"]),
    "TRACTOR": Object("TRACTOR", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["ALUMINUM"], bytes=1000),
    "TRAILER": Object("TRAILER", RESOURCES["COMPOUND"], SMELTED_RESOURCES["ALUMINUM"], bytes=1500),
    "MEDIUM BUGGY HORN": Object("MEDIUM BUGGY HORN", COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["RUBBER"], bytes=1000),
    "PAVER": Object("PAVER", COMP_RESOURCES_1["ALUMINUM ALLOY"], COMP_RESOURCES_1["SILICONE"], bytes=5000),
    "DRILL STRENGTH 1": Object("DRILL STRENGTH 1", SMELTED_RESOURCES["CERAMIC"], COMP_RESOURCES_1["TUNGSTEN CARBIDE"], bytes=2500),
    "DRILL STRENGTH 2": Object("DRILL STRENGTH 2", COMP_RESOURCES_3["TITANIUM ALLOY"], COMP_RESOURCES_1["TUNGSTEN CARBIDE"], bytes=5000),
    "DRILL STRENGTH 3": Object("DRILL STRENGTH 3", COMP_RESOURCES_3["DIAMOND"], COMP_RESOURCES_3["TITANIUM ALLOY"], bytes=7500),
    "SOLID FUEL THRUSTER": Object("SOLID FUEL THRUSTER", SMELTED_RESOURCES["ALUMINUM"], RESOURCES["AMMONIUM"], bytes=500),
    
    # Tier 3
    "LARGE PRINTER": Object("LARGE PRINTER", RESOURCES["COMPOUND"], RESOURCES["COMPOUND"], RESOURCES["COMPOUND"]),
    "SMELTING FURNACE": Object("SMELTING FURNACE", RESOURCES["COMPOUND"], RESOURCES["RESIN"], RESOURCES["RESIN"], bytes=250),
    "SOIL CENTRIFUGE": Object("SOIL CENTRIFUGE", RESOURCES["COMPOUND"], RESOURCES["COMPOUND"], SMELTED_RESOURCES["ALUMINUM"], bytes=750),
    "CHEMISTRY LAB": Object("CHEMISTRY LAB", SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["GLASS"], SMELTED_RESOURCES["TUNGSTEN"], bytes=1600),
    "ATMOSPHERIC CONDENSER": Object("ATMOSPHERIC CONDENSER", COMP_RESOURCES_1["PLASTIC"], SMELTED_RESOURCES["GLASS"], SMELTED_RESOURCES["IRON"], bytes=2200),
    "RESEARCH CHAMBER": Object("RESEARCH CHAMBER", RESOURCES["COMPOUND"], RESOURCES["COMPOUND"], RESOURCES["RESIN"]),
    "EXO REQUEST PLATFORM": Object("EXO REQUEST PLATFORM", RESOURCES["RESIN"], RESOURCES["RESIN"], SMELTED_RESOURCES["CERAMIC"]),
    "LARGE SOLAR PANEL": Object("LARGE SOLAR PANEL", COMP_RESOURCES_1["ALUMINUM ALLOY"], SMELTED_RESOURCES["GLASS"], SMELTED_RESOURCES["COPPER"], bytes=4000),
    "LARGE WIND TURBINE": Object("LARGE WIND TURBINE", COMP_RESOURCES_1["ALUMINUM ALLOY"], SMELTED_RESOURCES["GLASS"], SMELTED_RESOURCES["CERAMIC"], bytes=3500),
    "LARGE PLATFORM A": Object("LARGE PLATFORM A", RESOURCES["RESIN"], RESOURCES["RESIN"]),
    "LARGE PLATFORM B": Object("LARGE PLATFORM B", RESOURCES["RESIN"], RESOURCES["RESIN"], RESOURCES["RESIN"], bytes=500),
    "LARGE PLATFORM C": Object("LARGE PLATFORM C", RESOURCES["RESIN"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["IRON"], bytes=1000),
    "LARGE T-PLATFORM": Object("LARGE T-PLATFORM", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["ALUMINUM"], RESOURCES["RESIN"], bytes=1000),
    "LARGE CURVED PLATFORM": Object("LARGE CURVED PLATFORM", RESOURCES["COMPOUND"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], bytes=1000),
    "LARGE EXTENDED PLATFORM": Object("LARGE EXTENDED PLATFORM", RESOURCES["RESIN"], RESOURCES["RESIN"], bytes=500),
    "LARGE RESOURCE CANISTER": Object("LARGE RESOURCE CANISTER", SMELTED_RESOURCES["GLASS"], SMELTED_RESOURCES["TITANIUM"], COMP_RESOURCES_4["NANOCARBON ALLOY"], bytes=5000),
    "LARGE STORAGE": Object("LARGE STORAGE", SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], bytes=2000),
    "LARGE STORAGE SILO A": Object("LARGE STORAGE SILO A", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["ALUMINUM"], COMP_RESOURCES_1["STEEL"], bytes=5000),
    "LARGE STORAGE SILO B": Object("LARGE STORAGE SILO B", COMP_RESOURCES_1["STEEL"], COMP_RESOURCES_1["STEEL"], COMP_RESOURCES_1["STEEL"], bytes=7500),
    "LARGE ACTIVE STORAGE": Object("LARGE ACTIVE STORAGE", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ALUMINUM"], RESOURCES["RESIN"], bytes=2000),
    "BUGGY": Object("BUGGY", RESOURCES["COMPOUND"], SMELTED_RESOURCES["ALUMINUM"], bytes=1500),
    "LARGE ROVER SEAT": Object("LARGE ROVER SEAT", COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["PLASTIC"], RESOURCES["COMPOUND"], bytes=2000),
    "MEDIUM ROVER": Object("MEDIUM ROVER", COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["RUBBER"], bytes=3750),
    "CRANE": Object("CRANE", COMP_RESOURCES_1["STEEL"], COMP_RESOURCES_1["SILICONE"], SMELTED_RESOURCES["TITANIUM"], bytes=4500),
    "LARGE FOG HORN": Object("LARGE FOG HORN", COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["RUBBER"], COMP_RESOURCES_1["STEEL"], bytes=4000),
    "RECREATIONAL SPHERE": Object("RECREATIONAL SPHERE", COMP_RESOURCES_1["ALUMINUM ALLOY"], COMP_RESOURCES_1["RUBBER"], bytes=4500),

    # Tier 4
    "SHELTER": Object("SHELTER", COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["PLASTIC"], COMP_RESOURCES_1["SILICONE"], COMP_RESOURCES_1["SILICONE"]),
    "SOLAR ARRAY": Object("SOLAR ARRAY", SMELTED_RESOURCES["COPPER"], SMELTED_RESOURCES["GLASS"], COMP_RESOURCES_2["GRAPHENE"], COMP_RESOURCES_1["ALUMINUM ALLOY"], bytes=6000),
    "XL WIND TURBINE": Object("XL WIND TURBINE", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["CERAMIC"], COMP_RESOURCES_2["GRAPHENE"], COMP_RESOURCES_1["ALUMINUM ALLOY"], bytes=4500),
    "MEDIUM SENSOR ARCH": Object("MEDIUM SENSOR ARCH", SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], bytes=500),
    "XL SENSOR ARCH": Object("XL SENSOR ARCH", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], RESOURCES["QUARTZ"], bytes=1000),
    "XL SENSOR CANOPY": Object("XL SENSOR CANOPY", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], RESOURCES["QUARTZ"], bytes=1000),
    "LARGE SENSOR RING": Object("LARGE SENSOR RING", SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], bytes=500),
    "LARGE SENSOR HOOP A": Object("LARGE SENSOR HOOP A", SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], RESOURCES["QUARTZ"], bytes=750),
    "LARGE SENSOR HOOP B": Object("LARGE SENSOR HOOP B", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], bytes=750),
    "XL SENSOR HOOP A": Object("XL SENSOR HOOP A", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], RESOURCES["QUARTZ"], bytes=750),
    "XL SENSOR HOOP B": Object("XL SENSOR HOOP B", SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ZINC"], SMELTED_RESOURCES["ZINC"], RESOURCES["QUARTZ"], bytes=1000),
    "EXTRA LARGE PLATFORM A": Object("EXTRA LARGE PLATFORM A", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], bytes=2000),
    "EXTRA LARGE PLATFORM B": Object("EXTRA LARGE PLATFORM B", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], bytes=3000),
    "EXTRA LARGE PLATFORM C": Object("EXTRA LARGE PLATFORM C", RESOURCES["RESIN"], RESOURCES["RESIN"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], bytes=2000),
    "EXTRA LARGE CURVED PLATFORM": Object("EXTRA LARGE CURVED PLATFORM", SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], RESOURCES["COMPOUND"], RESOURCES["COMPOUND"], bytes=2000),
    "XL EXTENDED PLATFORM": Object("XL EXTENDED PLATFORM", RESOURCES["RESIN"], RESOURCES["RESIN"], RESOURCES["RESIN"], bytes=750),
    "FIGURINE PLATFORM": Object("FIGURINE PLATFORM", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], bytes=3000),
    "EXTRA LARGE STORAGE": Object("EXTRA LARGE STORAGE", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], bytes=2000),
    "LANDING PAD": Object("LANDING PAD", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], bytes=750),
    "SMALL SHUTTLE": Object("SMALL SHUTTLE", SMELTED_RESOURCES["ALUMINUM"], SMELTED_RESOURCES["ALUMINUM"], bytes=1500),
    "MEDIUM SHUTTLE": Object("MEDIUM SHUTTLE", COMP_RESOURCES_1["ALUMINUM ALLOY"], SMELTED_RESOURCES["CERAMIC"], SMELTED_RESOURCES["CERAMIC"], bytes=3750),
}
BUILDINGS_2 = {
    # Tier 1
    "LEVELING BLOCK": Object("LEVELING BLOCK", BUILDINGS["SMALL CANISTER"], bytes=500),
    "EXO CHIP": Object("EXO CHIP", BUILDINGS["DYNAMITE"])
}
BUILDINGS_3 = {
    # Tier 1
    "SMALL CAMERA": Object("SMALL CAMERA", BUILDINGS_2["EXO CHIP"], bytes=2500),
    "HOVERBOARD": Object("HOVERBOARD", BUILDINGS_2["EXO CHIP"]),
    
    # Tier 2
    "WINCH": Object("WINCH", BUILDINGS_2["EXO CHIP"], COMP_RESOURCES_1["RUBBER"], bytes=3750),
    "HYDRAZINE THRUSTER": Object("HYDRAZINE THRUSTER", BUILDINGS_2["EXO CHIP"], COMP_RESOURCES_1["STEEL"], bytes=3750),
    
    # Tier 3
    "TRADE PLATFORM": Object("TRADE PLATFORM", SMELTED_RESOURCES["IRON"], SMELTED_RESOURCES["TUNGSTEN"], BUILDINGS_2["EXO CHIP"], bytes=2500),
    "LARGE SHREDDER": Object("LARGE SHREDDER", COMP_RESOURCES_1["TUNGSTEN CARBIDE"], SMELTED_RESOURCES["IRON"], BUILDINGS_2["EXO CHIP"], bytes=2500),
    "VTOL": Object("VTOL", COMP_RESOURCES_1["TUNGSTEN CARBIDE"], COMP_RESOURCES_1["SILICONE"], BUILDINGS_2["EXO CHIP"]),

    # Tier 4
    "AUTO EXTRACTOR": Object("AUTO EXTRACTOR", COMP_RESOURCES_1["TUNGSTEN CARBIDE"], COMP_RESOURCES_1["RUBBER"], COMP_RESOURCES_1["STEEL"], BUILDINGS_2["EXO CHIP"], bytes=7500),
    "EXTRA LARGE SHREDDER": Object("EXTRA LARGE SHREDDER", COMP_RESOURCES_1["TUNGSTEN CARBIDE"], COMP_RESOURCES_1["STEEL"], BUILDINGS_2["EXO CHIP"], BUILDINGS_2["EXO CHIP"], bytes=5000),
    "LARGE ROVER": Object("LARGE ROVER", COMP_RESOURCES_1["ALUMINUM ALLOY"], COMP_RESOURCES_1["RUBBER"], BUILDINGS_2["EXO CHIP"], BUILDINGS_2["EXO CHIP"], bytes=5000),
    "LARGE SHUTTLE": Object("LARGE SHUTTLE", COMP_RESOURCES_3["TITANIUM ALLOY"], SMELTED_RESOURCES["CERAMIC"], BUILDINGS_2["EXO CHIP"], BUILDINGS_2["EXO CHIP"], bytes=5000),
}

def lookup(item, tab=1, times=""):

    if isinstance(item, Resource): # Is Resource
        return f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{'    '*(tab+0)}Planets: {', '.join(item.planets)}"
    
    elif isinstance(item, RefinedResource): # Is Smelted Resource
        return f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{'    '*(tab+0)}{item.smeltedFrom.name} ({item.smeltedFrom.type}):\n{'    '*(tab+1)}Planets: {', '.join(item.smeltedFrom.planets)}"
    
    elif isinstance(item, AtmoResource): # Is Atmospheric Resource (aka Gas)
        atmo = ""
        for i in item.planetsAndPPU:
            atmo += f"{'    '*(tab+0)}{i} ({item.planetsAndPPU[i]} PPU),\n"
        return f"{'    '*(tab-1)}{item.name} ({item.type}):\n{atmo[:-2]}"

    elif isinstance(item, CompResource): # Is Composite Resource
        if item.res1 == item.res2:
            info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1, 'x2 ')}"
        else:
            info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}"
        if item.gas: info += "\n"+lookup(item.gas, tab+1)
        return info

    elif isinstance(item, Object): # Is Building / Object
        if item.res1 == item.res2:
            if item.res2 == item.res3:
                if item.res3 == item.res4:
                    info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1, 'x4 ')}"
                else:
                    info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1, 'x3 ')}"
                    if item.res4:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
            else:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1, 'x2 ')}"
                if item.res3:
                    if item.res3 == item.res4:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1, 'x2 ')}"
                    else:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1)}"
                        if item.res4:
                            info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
        elif item.res2 and item.res2 == item.res3:
            info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}"
            if item.res3 == item.res4:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res3, tab+1, 'x3 ')}"
            else:
                info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1, 'x2 ')}"
                if item.res4:
                    info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
        else:
            if not item.res2:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}"
            elif not item.res3:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}"
            elif not item.res4:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}\n{lookup(item.res3, tab+1)}"
            else:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}"
                if item.res3:
                    if item.res3 == item.res4:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1, 'x2 ')}"
                    else:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1)}"
                        if item.res4:
                            info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
                else:
                    info = f"{'    '*(tab-1)}{times}{item.name} ({item.type}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}\n{lookup(item.res3, tab+1)}\n{lookup(item.res4, tab+1)}"
        info += f"\n{'    '*(tab+0)}{item.bytes} BYTES"
        return info

os.system("title Astroneer Lookup")

def clear():
    if sys.platform == "win32": os.system("cls")
    else: os.system("clear")

clear()

check_version.run(1.0, "astroneerlookup", "https://github.com/Isangedal/Astroneer-Lookup/releases/latest/download/Astroneer.Lookup.exe")

helpMsg = "\n\nWelcome to Astroneer Lookup!\n\nType a resource name or the name of a building to find out how to make it!\nType \"/items\" or \"/buildings\" (without the \"\") to see which items and buildings you can ask for\nType \"/exit\" to close the program\nType \"/help\" to view this message at any time\n\n"
print(helpMsg)

def foundFunc(item):
    print(f"RESOURCE FOUND!\n\n{lookup(item)}\n")

while True:
    
    req = input("Lookup: ")

    clear()

    if req.startswith("/"): # Commands
        nl = '\n'
        if req.lower() == "/items": # Display all items

            print(f"{f',{nl}'.join(RESOURCES)},\n\n{f',{nl}'.join(SMELTED_RESOURCES)},\n\n{f',{nl}'.join(ATMO_RESOURCES)},\n\n{f',{nl}'.join(COMP_RESOURCES_1)},\n{f',{nl}'.join(COMP_RESOURCES_2)},\n{f',{nl}'.join(COMP_RESOURCES_3)},\n{f',{nl}'.join(COMP_RESOURCES_4)}\n\n")
        
        elif req.lower() == "/buildings": # Display all buildings
            
            print(f"{f',{nl}'.join(BUILDINGS)},\n{f',{nl}'.join(BUILDINGS_2)},\n{f',{nl}'.join(BUILDINGS_3)}\n\n")

        else:
            print("Could not find a command with this name!\n")
            
        continue
    
    i = req.upper()
    if i in RESOURCES: foundFunc(RESOURCES[i])
    elif i in SMELTED_RESOURCES: foundFunc(SMELTED_RESOURCES[i])
    elif i in ATMO_RESOURCES: foundFunc(ATMO_RESOURCES[i])
    elif i in COMP_RESOURCES_1: foundFunc(COMP_RESOURCES_1[i])
    elif i in COMP_RESOURCES_2: foundFunc(COMP_RESOURCES_2[i])
    elif i in COMP_RESOURCES_3: foundFunc(COMP_RESOURCES_3[i])
    elif i in COMP_RESOURCES_4: foundFunc(COMP_RESOURCES_4[i])
    elif i in BUILDINGS: foundFunc(BUILDINGS[i])
    elif i in BUILDINGS_2: foundFunc(BUILDINGS_2[i])
    elif i in BUILDINGS_3: foundFunc(BUILDINGS_3[i])

    else:
        print("Could not find a resource with this name!\n")
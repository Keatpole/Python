import os,sys,check_version,time

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
    def __init__(self, name, res1, res2=None, res3=None, res4=None, bytes=0, tier=1):
        self.name = name
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3
        self.res4 = res4
        self.bytes = bytes
        self.tier = tier
        self.type = "Object / Building"

ALL_RESOURCES = {}

# All Resources
ALL_RESOURCES["RESOURCES"] = {
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

# All Smelted Resources
ALL_RESOURCES["SMELTED_RESOURCES"] = {
    "CARBON": RefinedResource("CARBON", ALL_RESOURCES["RESOURCES"]["ORGANIC"]),
    "CERAMIC": RefinedResource("CERAMIC", ALL_RESOURCES["RESOURCES"]["CLAY"]),
    "GLASS": RefinedResource("GLASS", ALL_RESOURCES["RESOURCES"]["QUARTZ"]),
    "ALUMINUM": RefinedResource("ALUMINUM", ALL_RESOURCES["RESOURCES"]["LATERITE"]),
    "ZINC": RefinedResource("ZINC", ALL_RESOURCES["RESOURCES"]["SPHALERITE"]),
    "COPPER": RefinedResource("COPPER", ALL_RESOURCES["RESOURCES"]["MALACHITE"]),
    "TUNGSTEN": RefinedResource("TUNGSTEN", ALL_RESOURCES["RESOURCES"]["WOLFRAMITE"]),
    "IRON": RefinedResource("IRON", ALL_RESOURCES["RESOURCES"]["HEMATITE"]),
    "TITANIUM": RefinedResource("TITANIUM", ALL_RESOURCES["RESOURCES"]["TITANITE"])
}

# All Gases
ALL_RESOURCES["ATMO_RESOURCES"] = {
    "HYDROGEN": AtmoResource("HYDROGEN", {"VESANIA": 100, "SYLVA": 75, "CALIDOR": 50, "NOVUS": 25}),
    "ARGON": AtmoResource("ARGON", {"GLACIO": 100, "VESANIA": 50}),
    "METHANE": AtmoResource("METHANE", {"ATROX": 100, "NOVUS": 75}),
    "NITROGEN": AtmoResource("NITROGEN", {"SYLVA": 100, "VESANIA": 75, "ATROX": 50}),
    "SULFUR": AtmoResource("SULFUR", {"CALIDOR": 100, "ATROX": 75}),
    "HELIUM": AtmoResource("HELIUM", {"ATROX": 25})
}
# All Composite Resources
ALL_RESOURCES["COMP_RESOURCES_1"] = {
    "RUBBER": CompResource("RUBBER", ALL_RESOURCES["RESOURCES"]["ORGANIC"], ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "PLASTIC": CompResource("PLASTIC", ALL_RESOURCES["SMELTED_RESOURCES"]["CARBON"], ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "ALUMINUM ALLOY": CompResource("ALUMINUM ALLOY", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"]),
    "TUNGSTEN CARBIDE": CompResource("TUNGSTEN CARBIDE", ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], ALL_RESOURCES["SMELTED_RESOURCES"]["CARBON"]),
    "HYDRAZINE": CompResource("HYDRAZINE", ALL_RESOURCES["RESOURCES"]["AMMONIUM"], ALL_RESOURCES["RESOURCES"]["AMMONIUM"], ALL_RESOURCES["ATMO_RESOURCES"]["HYDROGEN"]),
    "SILICONE": CompResource("SILICONE", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["ATMO_RESOURCES"]["METHANE"]),
    "EXPLOSIVE POWDER": CompResource("EXPLOSIVE POWDER", ALL_RESOURCES["SMELTED_RESOURCES"]["CARBON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CARBON"], ALL_RESOURCES["ATMO_RESOURCES"]["SULFUR"]),
    "STEEL": CompResource("STEEL", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CARBON"], ALL_RESOURCES["ATMO_RESOURCES"]["ARGON"]),
}
ALL_RESOURCES["COMP_RESOURCES_2"] = {
    "GRAPHENE": CompResource("GRAPHENE", ALL_RESOURCES["RESOURCES"]["GRAPHITE"], ALL_RESOURCES["COMP_RESOURCES_1"]["HYDRAZINE"])
}
ALL_RESOURCES["COMP_RESOURCES_3"] = {
    "DIAMOND": CompResource("DIAMOND", ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"]),
    "TITANIUM ALLOY": CompResource("TITANIUM ALLOY", ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], ALL_RESOURCES["ATMO_RESOURCES"]["NITROGEN"])
}
ALL_RESOURCES["COMP_RESOURCES_4"] = {
    "NANOCARBON ALLOY": CompResource("NANOCARBON ALLOY", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["ATMO_RESOURCES"]["HELIUM"])
}
# All Buildings
ALL_RESOURCES["BUILDINGS"] = {
    # Tier 1
    "SMALL PRINTER": Object("SMALL PRINTER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], tier=1),
    "PACKAGER": Object("PACKAGER", ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=1000, tier=1),
    "TETHERS": Object("TETHERS", ALL_RESOURCES["RESOURCES"]["COMPOUND"], tier=1),
    "OXYGEN FILTERS": Object("OXYGEN FILTERS", ALL_RESOURCES["RESOURCES"]["RESIN"], tier=1),
    "OXYGEN TANK": Object("OXYGEN TANK", ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2000, tier=1),
    "PORTABLE OXYGENATOR": Object("PORTABLE OXYGENATOR", ALL_RESOURCES["COMP_RESOURCES_4"]["NANOCARBON ALLOY"], bytes=10000, tier=1),
    "SMALL CANISTER": Object("SMALL CANISTER", ALL_RESOURCES["RESOURCES"]["RESIN"], tier=1),
    "BEACON": Object("BEACON", ALL_RESOURCES["RESOURCES"]["QUARTZ"], tier=1),
    "WORKLIGHT": Object("WORKLIGHT", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], tier=1),
    "GLOWSTICKS": Object("GLOWSTICKS", ALL_RESOURCES["RESOURCES"]["ORGANIC"], bytes=350, tier=1),
    "FLOODLIGHT": Object("FLOODLIGHT", ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], bytes=2000, tier=1),
    "SMALL GENERATOR": Object("SMALL GENERATOR", ALL_RESOURCES["RESOURCES"]["COMPOUND"], tier=1),
    "POWER CELLS": Object("POWER CELLS", ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=800, tier=1),
    "SMALL SOLAR PANEL": Object("SMALL SOLAR PANEL", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=300, tier=1),
    "SMALL WIND TURBINE": Object("SMALL WIND TURBINE", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=300, tier=1),
    "SMALL BATTERY": Object("SMALL BATTERY", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=2000, tier=1),
    "BOOST MOD": Object("BOOST MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=1),
    "WIDE MOD": Object("WIDE MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=1),
    "NARROW MOD": Object("NARROW MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=1),
    "INHIBITOR MOD": Object("INHIBITOR MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=1),
    "ALIGNMENT MOD": Object("ALIGNMENT MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=1),
    "DRILL MOD 1": Object("DRILL MOD 1", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=1000, tier=1),
    "DRILL MOD 2": Object("DRILL MOD 2", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], bytes=2500, tier=1),
    "DRILL MOD 3": Object("DRILL MOD 3", ALL_RESOURCES["COMP_RESOURCES_3"]["DIAMOND"], bytes=3750, tier=1),
    "DYNAMITE": Object("DYNAMITE", ALL_RESOURCES["COMP_RESOURCES_1"]["EXPLOSIVE POWDER"], bytes=3750, tier=1),
    "FIREWORKS": Object("FIREWORKS", ALL_RESOURCES["COMP_RESOURCES_1"]["EXPLOSIVE POWDER"], bytes=3750, tier=1),
    "SMALL TRUMPET HORN": Object("SMALL TRUMPET HORN", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], bytes=1000, tier=1),
    "HOLOGRAPHIC FIGURINE": Object("HOLOGRAPHIC FIGURINE", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], bytes=3000, tier=1),
    "TERRAIN ANALYZER": Object("TERRAIN ANALYZER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=2000, tier=1),
    "PROBE SCANNER": Object("PROBE SCANNER", ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=3000, tier=1),
    "SOLID-FUEL JUMP JET": Object("SOLID-FUEL JUMP JET", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], bytes=5000, tier=1),
    "HYDRAZINE JET PACK": Object("HYDRAZINE JET PACK", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], bytes=15000, tier=1),

    # Tier 2
    "MEDIUM PRINTER": Object("MEDIUM PRINTER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], tier=2),
    "OXYGENATOR": Object("OXYGENATOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=1800, tier=2),
    "MEDIUM SHREDDER": Object("MEDIUM SHREDDER", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=1250, tier=2),
    "FIELD SHELTER": Object("FIELD SHELTER", ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], bytes=8000, tier=2),
    "AUTO ARM": Object("AUTO ARM", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=1500, tier=2),
    "MEDIUM RESOURCE CANISTER": Object("MEDIUM RESOURCE CANISTER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2000, tier=2),
    "MEDIUM FLUID & SOIL CANISTER": Object("MEDIUM FLUID & SOIL CANISTER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2500, tier=2),
    "MEDIUM GAS CANISTER": Object("MEDIUM GAS CANISTER", ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=4000, tier=2),
    "POWER SENSOR": Object("POWER SENSOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=500, tier=2),
    "STORAGE SENSOR": Object("STORAGE SENSOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750, tier=2),
    "BATTERY SENSOR": Object("BATTERY SENSOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=750, tier=2),
    "BUTTON REPEATER": Object("BUTTON REPEATER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=300, tier=2),
    "DELAY REPEATER": Object("DELAY REPEATER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=2),
    "COUNT REPEATER": Object("COUNT REPEATER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000, tier=2),
    "EXTENDERS": Object("EXTENDERS", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=500, tier=2),
    "POWER SWITCH": Object("POWER SWITCH", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=750, tier=2),
    "SPLITTER": Object("SPLITTER", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=1000, tier=2),
    "MEDIUM GENERATOR": Object("MEDIUM GENERATOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], bytes=2000, tier=2),
    "MEDIUM SOLAR PANEL": Object("MEDIUM SOLAR PANEL", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2000, tier=2),
    "MEDIUM WIND TURBINE": Object("MEDIUM GENERATOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2500, tier=2),
    "MEDIUM BATTERY": Object("MEDIUM BATTERY", ALL_RESOURCES["RESOURCES"]["LITHIUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=3750, tier=2),
    "RTG": Object("RTG", ALL_RESOURCES["COMP_RESOURCES_4"]["NANOCARBON ALLOY"], ALL_RESOURCES["RESOURCES"]["LITHIUM"], bytes=12500, tier=2),
    "MEDIUM PLATFORM A": Object("MEDIUM PLATFORM A", ALL_RESOURCES["RESOURCES"]["RESIN"], tier=2),
    "MEDIUM PLATFORM B": Object("MEDIUM PLATFORM B", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=250, tier=2),
    "MEDIUM PLATFORM C": Object("MEDIUM PLATFORM C", ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=400, tier=2),
    "TALL PLATFORM": Object("TALL PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=750, tier=2),
    "MEDIUM T-PLATFORM": Object("MEDIUM T-PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=400, tier=2),
    "MEDIUM STORAGE": Object("MEDIUM STORAGE", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], tier=2),
    "MEDIUM STORAGE SILO": Object("MEDIUM STORAGE SILO", ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], bytes=3000, tier=2),
    "TALL STORAGE": Object("TALL STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=400, tier=2),
    "ROVER SEAT": Object("ROVER SEAT", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], tier=2),
    "TRACTOR": Object("TRACTOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1000, tier=2),
    "TRAILER": Object("TRAILER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1500, tier=2),
    "MEDIUM BUGGY HORN": Object("MEDIUM BUGGY HORN", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=1000, tier=2),
    "PAVER": Object("PAVER", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], bytes=5000, tier=2),
    "DRILL STRENGTH 1": Object("DRILL STRENGTH 1", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], bytes=2500, tier=2),
    "DRILL STRENGTH 2": Object("DRILL STRENGTH 2", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], bytes=5000, tier=2),
    "DRILL STRENGTH 3": Object("DRILL STRENGTH 3", ALL_RESOURCES["COMP_RESOURCES_3"]["DIAMOND"], ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], bytes=7500, tier=2),
    "SOLID FUEL THRUSTER": Object("SOLID FUEL THRUSTER", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["AMMONIUM"], bytes=500, tier=2),
    
    # Tier 3
    "LARGE PRINTER": Object("LARGE PRINTER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], tier=3),
    "SMELTING FURNACE": Object("SMELTING FURNACE", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=250, tier=3),
    "SOIL CENTRIFUGE": Object("SOIL CENTRIFUGE", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=750, tier=3),
    "CHEMISTRY LAB": Object("CHEMISTRY LAB", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], bytes=1600, tier=3),
    "ATMOSPHERIC CONDENSER": Object("ATMOSPHERIC CONDENSER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=2200, tier=3),
    "RESEARCH CHAMBER": Object("RESEARCH CHAMBER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["RESIN"], tier=3),
    "EXO REQUEST PLATFORM": Object("EXO REQUEST PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], tier=3),
    "LARGE SOLAR PANEL": Object("LARGE SOLAR PANEL", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=4000, tier=3),
    "LARGE WIND TURBINE": Object("LARGE WIND TURBINE", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=3500, tier=3),
    "LARGE PLATFORM A": Object("LARGE PLATFORM A", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], tier=3),
    "LARGE PLATFORM B": Object("LARGE PLATFORM B", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=500, tier=3),
    "LARGE PLATFORM C": Object("LARGE PLATFORM C", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=1000, tier=3),
    "LARGE T-PLATFORM": Object("LARGE T-PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=1000, tier=3),
    "LARGE CURVED PLATFORM": Object("LARGE CURVED PLATFORM", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=1000, tier=3),
    "LARGE EXTENDED PLATFORM": Object("LARGE EXTENDED PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=500, tier=3),
    "LARGE RESOURCE CANISTER": Object("LARGE RESOURCE CANISTER", ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], ALL_RESOURCES["COMP_RESOURCES_4"]["NANOCARBON ALLOY"], bytes=5000, tier=3),
    "LARGE STORAGE": Object("LARGE STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2000, tier=3),
    "LARGE STORAGE SILO A": Object("LARGE STORAGE SILO A", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=5000, tier=3),
    "LARGE STORAGE SILO B": Object("LARGE STORAGE SILO B", ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=7500, tier=3),
    "LARGE ACTIVE STORAGE": Object("LARGE ACTIVE STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=2000, tier=3),
    "BUGGY": Object("BUGGY", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1500, tier=3),
    "LARGE ROVER SEAT": Object("LARGE ROVER SEAT", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], bytes=2000, tier=3),
    "MEDIUM ROVER": Object("MEDIUM ROVER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=3750, tier=3),
    "CRANE": Object("CRANE", ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], bytes=4500, tier=3),
    "LARGE FOG HORN": Object("LARGE FOG HORN", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=4000, tier=3),
    "RECREATIONAL SPHERE": Object("RECREATIONAL SPHERE", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=4500, tier=3),

    # Tier 4
    "SHELTER": Object("SHELTER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], tier=4),
    "SOLAR ARRAY": Object("SOLAR ARRAY", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], bytes=6000, tier=4),
    "XL WIND TURBINE": Object("XL WIND TURBINE", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], bytes=4500, tier=4),
    "MEDIUM SENSOR ARCH": Object("MEDIUM SENSOR ARCH", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=500, tier=4),
    "XL SENSOR ARCH": Object("XL SENSOR ARCH", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=1000, tier=4),
    "XL SENSOR CANOPY": Object("XL SENSOR CANOPY", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=1000, tier=4),
    "LARGE SENSOR RING": Object("LARGE SENSOR RING", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=500, tier=4),
    "LARGE SENSOR HOOP A": Object("LARGE SENSOR HOOP A", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750, tier=4),
    "LARGE SENSOR HOOP B": Object("LARGE SENSOR HOOP B", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750, tier=4),
    "XL SENSOR HOOP A": Object("XL SENSOR HOOP A", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750, tier=4),
    "XL SENSOR HOOP B": Object("XL SENSOR HOOP B", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=1000, tier=4),
    "EXTRA LARGE PLATFORM A": Object("EXTRA LARGE PLATFORM A", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2000, tier=4),
    "EXTRA LARGE PLATFORM B": Object("EXTRA LARGE PLATFORM B", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=3000, tier=4),
    "EXTRA LARGE PLATFORM C": Object("EXTRA LARGE PLATFORM C", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=2000, tier=4),
    "EXTRA LARGE CURVED PLATFORM": Object("EXTRA LARGE CURVED PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], bytes=2000, tier=4),
    "XL EXTENDED PLATFORM": Object("XL EXTENDED PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=750, tier=4),
    "FIGURINE PLATFORM": Object("FIGURINE PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=3000, tier=4),
    "EXTRA LARGE STORAGE": Object("EXTRA LARGE STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2000, tier=4),
    "LANDING PAD": Object("LANDING PAD", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=750, tier=4),
    "SMALL SHUTTLE": Object("SMALL SHUTTLE", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1500, tier=4),
    "MEDIUM SHUTTLE": Object("MEDIUM SHUTTLE", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=3750, tier=4),
}
ALL_RESOURCES["BUILDINGS_2"] = {
    # Tier 1
    "LEVELING BLOCK": Object("LEVELING BLOCK", ALL_RESOURCES["BUILDINGS"]["SMALL CANISTER"], bytes=500, tier=1),
    "EXO CHIP": Object("EXO CHIP", ALL_RESOURCES["BUILDINGS"]["DYNAMITE"], tier=1)
}
ALL_RESOURCES["BUILDINGS_3"] = {
    # Tier 1
    "SMALL CAMERA": Object("SMALL CAMERA", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=2500, tier=1),
    "HOVERBOARD": Object("HOVERBOARD", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], tier=1),
    
    # Tier 2
    "WINCH": Object("WINCH", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=3750, tier=2),
    "HYDRAZINE THRUSTER": Object("HYDRAZINE THRUSTER", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=3750, tier=2),
    
    # Tier 3
    "TRADE PLATFORM": Object("TRADE PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=2500, tier=3),
    "LARGE SHREDDER": Object("LARGE SHREDDER", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=2500, tier=3),
    "VTOL": Object("VTOL", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], tier=3),

    # Tier 4
    "AUTO EXTRACTOR": Object("AUTO EXTRACTOR", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=7500, tier=4),
    "EXTRA LARGE SHREDDER": Object("EXTRA LARGE SHREDDER", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=5000, tier=4),
    "LARGE ROVER": Object("LARGE ROVER", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=5000, tier=4),
    "LARGE SHUTTLE": Object("LARGE SHUTTLE", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=5000, tier=4),
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
                    info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1, 'x4 ')}"
                else:
                    info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1, 'x3 ')}"
                    if item.res4:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
            else:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1, 'x2 ')}"
                if item.res3:
                    if item.res3 == item.res4:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1, 'x2 ')}"
                    else:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1)}"
                        if item.res4:
                            info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
        elif item.res2 and item.res2 == item.res3:
            info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1)}"
            if item.res3 == item.res4:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res3, tab+1, 'x3 ')}"
            else:
                info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1, 'x2 ')}"
                if item.res4:
                    info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
        else:
            if not item.res2:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1)}"
            elif not item.res3:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}"
            elif not item.res4:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}\n{lookup(item.res3, tab+1)}"
            else:
                info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}"
                if item.res3:
                    if item.res3 == item.res4:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1, 'x2 ')}"
                    else:
                        info += f"\n{'    '*(tab-1)}{lookup(item.res3, tab+1)}"
                        if item.res4:
                            info += f"\n{'    '*(tab-1)}{lookup(item.res4, tab+1)}"
                else:
                    info = f"{'    '*(tab-1)}{times}{item.name} ({item.type} | Tier {item.tier}):\n{lookup(item.res1, tab+1)}\n{lookup(item.res2, tab+1)}\n{lookup(item.res3, tab+1)}\n{lookup(item.res4, tab+1)}"
        info += f"\n{'    '*(tab+0)}{item.bytes} BYTES"
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
    check_version.run(1.2, "astroneerlookup", "https://github.com/Isangedal/Astroneer-Lookup/releases/latest/download/Astroneer.Lookup.exe")
    print("\n\nWelcome to Astroneer Lookup!\n\nType a resource name or the name of a building to find out how to make it!\nType \"/items\" or \"/buildings\" (without the \"\") to see which items and buildings you can ask for\nType \"/exit\" to close the program\nType \"/help\" to view this message at any time\n\n")

os.system("title Astroneer Lookup")
clear()
help()

try:
    while True:
        
        req = input("Lookup: ")

        clear()

        if req.startswith("/"): # Commands

            if req.lower() == "/items": # Display all items
                for i in ALL_RESOURCES:
                    if i in ["RESOURCES", "SMELTED_RESOURCES", "ATMO_RESOURCES"]:
                        m = f"{i.replace('_', ' ')}:\n"
                        for v in ALL_RESOURCES[i]:
                            m += f"    {v.lower().capitalize()}\n"
                        print(m)
                    elif i in ["COMP_RESOURCES_1", "COMP_RESOURCES_2", "COMP_RESOURCES_3", "COMP_RESOURCES_4"]:
                        if i == "COMP_RESOURCES_1":
                            print("COMP RESOURCES:")
                        for v in ALL_RESOURCES[i]:
                            print(f"    {v.lower().capitalize()}")
                print("\n")

            elif req.lower() == "/buildings": # Display all buildings
                tier = input("Which tier of buildings do you want to see?\n")
                clear()
                try:
                    if int(tier) > 4 or int(tier) < 1: 0+""
                except:
                    print(f"Could not find tier \"{tier}\"\nThe available tiers are: 1, 2, 3, 4\n\n")
                    continue
                print(f"Tier {tier} buildings:\n")
                for i in ALL_RESOURCES:
                    if i in ["BUILDINGS", "BUILDINGS_2", "BUILDINGS_3"]:
                        for v in ALL_RESOURCES[i]:
                            a = ALL_RESOURCES[i][v]
                            if a.tier == int(tier):
                                print(f"{v.lower().capitalize()}")
                print("\n")
                        
            elif req.lower() == "/exit": # Exit program
                close()
            
            elif req.lower() == "/help": # Display the help message
                help()

            else:
                print("Could not find a command with this name!\n")
                
            continue
            
        found = False
        for i in ALL_RESOURCES:
            if req.upper() in ALL_RESOURCES[i]:
                print(f"RESOURCE FOUND!\n\n{lookup(ALL_RESOURCES[i][req.upper()])}\n")
                found = True

        if not found:
            print("Could not find a resource with this name!\n")
except KeyboardInterrupt:
    close()

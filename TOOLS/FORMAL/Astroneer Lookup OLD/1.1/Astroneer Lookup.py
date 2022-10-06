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

ALL_RESOURCES = {}

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
ALL_RESOURCES["ATMO_RESOURCES"] = {
    "HYDROGEN": AtmoResource("HYDROGEN", {"VESANIA": 100, "SYLVA": 75, "CALIDOR": 50, "NOVUS": 25}),
    "ARGON": AtmoResource("ARGON", {"GLACIO": 100, "VESANIA": 50}),
    "METHANE": AtmoResource("METHANE", {"ATROX": 100, "NOVUS": 75}),
    "NITROGEN": AtmoResource("NITROGEN", {"SYLVA": 100, "VESANIA": 75, "ATROX": 50}),
    "SULFUR": AtmoResource("SULFUR", {"CALIDOR": 100, "ATROX": 75}),
    "HELIUM": AtmoResource("HELIUM", {"ATROX": 25})
}
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
ALL_RESOURCES["BUILDINGS"] = {
    # Tier 1
    "SMALL PRINTER": Object("SMALL PRINTER", ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "PACKAGER": Object("PACKAGER", ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=1000),
    "TETHERS": Object("TETHERS", ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "OXYGEN FILTERS": Object("OXYGEN FILTERS", ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "OXYGEN TANK": Object("OXYGEN TANK", ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2000),
    "PORTABLE OXYGENATOR": Object("PORTABLE OXYGENATOR", ALL_RESOURCES["COMP_RESOURCES_4"]["NANOCARBON ALLOY"], bytes=10000),
    "SMALL CANISTER": Object("SMALL CANISTER", ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "BEACON": Object("BEACON", ALL_RESOURCES["RESOURCES"]["QUARTZ"]),
    "WORKLIGHT": Object("WORKLIGHT", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"]),
    "GLOWSTICKS": Object("GLOWSTICKS", ALL_RESOURCES["RESOURCES"]["ORGANIC"], bytes=350),
    "FLOODLIGHT": Object("FLOODLIGHT", ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], bytes=2000),
    "SMALL GENERATOR": Object("SMALL GENERATOR", ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "POWER CELLS": Object("POWER CELLS", ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=800),
    "SMALL SOLAR PANEL": Object("SMALL SOLAR PANEL", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=300),
    "SMALL WIND TURBINE": Object("SMALL WIND TURBINE", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=300),
    "SMALL BATTERY": Object("SMALL BATTERY", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=2000),
    "BOOST MOD": Object("BOOST MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "WIDE MOD": Object("WIDE MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "NARROW MOD": Object("NARROW MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "INHIBITOR MOD": Object("INHIBITOR MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "ALIGNMENT MOD": Object("ALIGNMENT MOD", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "DRILL MOD 1": Object("DRILL MOD 1", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=1000),
    "DRILL MOD 2": Object("DRILL MOD 2", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], bytes=2500),
    "DRILL MOD 3": Object("DRILL MOD 3", ALL_RESOURCES["COMP_RESOURCES_3"]["DIAMOND"], bytes=3750),
    "DYNAMITE": Object("DYNAMITE", ALL_RESOURCES["COMP_RESOURCES_1"]["EXPLOSIVE POWDER"], bytes=3750),
    "FIREWORKS": Object("FIREWORKS", ALL_RESOURCES["COMP_RESOURCES_1"]["EXPLOSIVE POWDER"], bytes=3750),
    "SMALL TRUMPET HORN": Object("SMALL TRUMPET HORN", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], bytes=1000),
    "HOLOGRAPHIC FIGURINE": Object("HOLOGRAPHIC FIGURINE", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], bytes=3000),
    "TERRAIN ANALYZER": Object("TERRAIN ANALYZER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=2000),
    "PROBE SCANNER": Object("PROBE SCANNER", ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=3000),
    "SOLID-FUEL JUMP JET": Object("SOLID-FUEL JUMP JET", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], bytes=5000),
    "HYDRAZINE JET PACK": Object("HYDRAZINE JET PACK", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], bytes=15000),

    # Tier 2
    "MEDIUM PRINTER": Object("MEDIUM PRINTER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "OXYGENATOR": Object("OXYGENATOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=1800),
    "MEDIUM SHREDDER": Object("MEDIUM SHREDDER", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=1250),
    "FIELD SHELTER": Object("FIELD SHELTER", ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], bytes=8000),
    "AUTO ARM": Object("AUTO ARM", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=1500),
    "MEDIUM RESOURCE CANISTER": Object("MEDIUM RESOURCE CANISTER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2000),
    "MEDIUM FLUID & SOIL CANISTER": Object("MEDIUM FLUID & SOIL CANISTER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2500),
    "MEDIUM GAS CANISTER": Object("MEDIUM GAS CANISTER", ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=4000),
    "POWER SENSOR": Object("POWER SENSOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=500),
    "STORAGE SENSOR": Object("STORAGE SENSOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750),
    "BATTERY SENSOR": Object("BATTERY SENSOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=750),
    "BUTTON REPEATER": Object("BUTTON REPEATER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=300),
    "DELAY REPEATER": Object("DELAY REPEATER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "COUNT REPEATER": Object("COUNT REPEATER", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=1000),
    "EXTENDERS": Object("EXTENDERS", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=500),
    "POWER SWITCH": Object("POWER SWITCH", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=750),
    "SPLITTER": Object("SPLITTER", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], ALL_RESOURCES["RESOURCES"]["GRAPHITE"], bytes=1000),
    "MEDIUM GENERATOR": Object("MEDIUM GENERATOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], bytes=2000),
    "MEDIUM SOLAR PANEL": Object("MEDIUM SOLAR PANEL", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], bytes=2000),
    "MEDIUM WIND TURBINE": Object("MEDIUM GENERATOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2500),
    "MEDIUM BATTERY": Object("MEDIUM BATTERY", ALL_RESOURCES["RESOURCES"]["LITHIUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], bytes=3750),
    "RTG": Object("RTG", ALL_RESOURCES["COMP_RESOURCES_4"]["NANOCARBON ALLOY"], ALL_RESOURCES["RESOURCES"]["LITHIUM"], bytes=12500),
    "MEDIUM PLATFORM A": Object("MEDIUM PLATFORM A", ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "MEDIUM PLATFORM B": Object("MEDIUM PLATFORM B", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=250),
    "MEDIUM PLATFORM C": Object("MEDIUM PLATFORM C", ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=400),
    "TALL PLATFORM": Object("TALL PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=750),
    "MEDIUM T-PLATFORM": Object("MEDIUM T-PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=400),
    "MEDIUM STORAGE": Object("MEDIUM STORAGE", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "MEDIUM STORAGE SILO": Object("MEDIUM STORAGE SILO", ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], bytes=3000),
    "TALL STORAGE": Object("TALL STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=400),
    "ROVER SEAT": Object("ROVER SEAT", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "TRACTOR": Object("TRACTOR", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1000),
    "TRAILER": Object("TRAILER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1500),
    "MEDIUM BUGGY HORN": Object("MEDIUM BUGGY HORN", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=1000),
    "PAVER": Object("PAVER", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], bytes=5000),
    "DRILL STRENGTH 1": Object("DRILL STRENGTH 1", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], bytes=2500),
    "DRILL STRENGTH 2": Object("DRILL STRENGTH 2", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], bytes=5000),
    "DRILL STRENGTH 3": Object("DRILL STRENGTH 3", ALL_RESOURCES["COMP_RESOURCES_3"]["DIAMOND"], ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], bytes=7500),
    "SOLID FUEL THRUSTER": Object("SOLID FUEL THRUSTER", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["AMMONIUM"], bytes=500),
    
    # Tier 3
    "LARGE PRINTER": Object("LARGE PRINTER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"]),
    "SMELTING FURNACE": Object("SMELTING FURNACE", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=250),
    "SOIL CENTRIFUGE": Object("SOIL CENTRIFUGE", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=750),
    "CHEMISTRY LAB": Object("CHEMISTRY LAB", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], bytes=1600),
    "ATMOSPHERIC CONDENSER": Object("ATMOSPHERIC CONDENSER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=2200),
    "RESEARCH CHAMBER": Object("RESEARCH CHAMBER", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "EXO REQUEST PLATFORM": Object("EXO REQUEST PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"]),
    "LARGE SOLAR PANEL": Object("LARGE SOLAR PANEL", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], bytes=4000),
    "LARGE WIND TURBINE": Object("LARGE WIND TURBINE", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=3500),
    "LARGE PLATFORM A": Object("LARGE PLATFORM A", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"]),
    "LARGE PLATFORM B": Object("LARGE PLATFORM B", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=500),
    "LARGE PLATFORM C": Object("LARGE PLATFORM C", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=1000),
    "LARGE T-PLATFORM": Object("LARGE T-PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=1000),
    "LARGE CURVED PLATFORM": Object("LARGE CURVED PLATFORM", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=1000),
    "LARGE EXTENDED PLATFORM": Object("LARGE EXTENDED PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=500),
    "LARGE RESOURCE CANISTER": Object("LARGE RESOURCE CANISTER", ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], ALL_RESOURCES["COMP_RESOURCES_4"]["NANOCARBON ALLOY"], bytes=5000),
    "LARGE STORAGE": Object("LARGE STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2000),
    "LARGE STORAGE SILO A": Object("LARGE STORAGE SILO A", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=5000),
    "LARGE STORAGE SILO B": Object("LARGE STORAGE SILO B", ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=7500),
    "LARGE ACTIVE STORAGE": Object("LARGE ACTIVE STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=2000),
    "BUGGY": Object("BUGGY", ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1500),
    "LARGE ROVER SEAT": Object("LARGE ROVER SEAT", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], bytes=2000),
    "MEDIUM ROVER": Object("MEDIUM ROVER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=3750),
    "CRANE": Object("CRANE", ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["SMELTED_RESOURCES"]["TITANIUM"], bytes=4500),
    "LARGE FOG HORN": Object("LARGE FOG HORN", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=4000),
    "RECREATIONAL SPHERE": Object("RECREATIONAL SPHERE", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=4500),

    # Tier 4
    "SHELTER": Object("SHELTER", ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["PLASTIC"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"]),
    "SOLAR ARRAY": Object("SOLAR ARRAY", ALL_RESOURCES["SMELTED_RESOURCES"]["COPPER"], ALL_RESOURCES["SMELTED_RESOURCES"]["GLASS"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], bytes=6000),
    "XL WIND TURBINE": Object("XL WIND TURBINE", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["COMP_RESOURCES_2"]["GRAPHENE"], ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], bytes=4500),
    "MEDIUM SENSOR ARCH": Object("MEDIUM SENSOR ARCH", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=500),
    "XL SENSOR ARCH": Object("XL SENSOR ARCH", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=1000),
    "XL SENSOR CANOPY": Object("XL SENSOR CANOPY", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=1000),
    "LARGE SENSOR RING": Object("LARGE SENSOR RING", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=500),
    "LARGE SENSOR HOOP A": Object("LARGE SENSOR HOOP A", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750),
    "LARGE SENSOR HOOP B": Object("LARGE SENSOR HOOP B", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750),
    "XL SENSOR HOOP A": Object("XL SENSOR HOOP A", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=750),
    "XL SENSOR HOOP B": Object("XL SENSOR HOOP B", ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["SMELTED_RESOURCES"]["ZINC"], ALL_RESOURCES["RESOURCES"]["QUARTZ"], bytes=1000),
    "EXTRA LARGE PLATFORM A": Object("EXTRA LARGE PLATFORM A", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2000),
    "EXTRA LARGE PLATFORM B": Object("EXTRA LARGE PLATFORM B", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=3000),
    "EXTRA LARGE PLATFORM C": Object("EXTRA LARGE PLATFORM C", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=2000),
    "EXTRA LARGE CURVED PLATFORM": Object("EXTRA LARGE CURVED PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], ALL_RESOURCES["RESOURCES"]["COMPOUND"], bytes=2000),
    "XL EXTENDED PLATFORM": Object("XL EXTENDED PLATFORM", ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], ALL_RESOURCES["RESOURCES"]["RESIN"], bytes=750),
    "FIGURINE PLATFORM": Object("FIGURINE PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], bytes=3000),
    "EXTRA LARGE STORAGE": Object("EXTRA LARGE STORAGE", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=2000),
    "LANDING PAD": Object("LANDING PAD", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=750),
    "SMALL SHUTTLE": Object("SMALL SHUTTLE", ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], ALL_RESOURCES["SMELTED_RESOURCES"]["ALUMINUM"], bytes=1500),
    "MEDIUM SHUTTLE": Object("MEDIUM SHUTTLE", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], bytes=3750),
}
ALL_RESOURCES["BUILDINGS_2"] = {
    # Tier 1
    "LEVELING BLOCK": Object("LEVELING BLOCK", ALL_RESOURCES["BUILDINGS"]["SMALL CANISTER"], bytes=500),
    "EXO CHIP": Object("EXO CHIP", ALL_RESOURCES["BUILDINGS"]["DYNAMITE"])
}
ALL_RESOURCES["BUILDINGS_3"] = {
    # Tier 1
    "SMALL CAMERA": Object("SMALL CAMERA", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=2500),
    "HOVERBOARD": Object("HOVERBOARD", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"]),
    
    # Tier 2
    "WINCH": Object("WINCH", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], bytes=3750),
    "HYDRAZINE THRUSTER": Object("HYDRAZINE THRUSTER", ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], bytes=3750),
    
    # Tier 3
    "TRADE PLATFORM": Object("TRADE PLATFORM", ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["SMELTED_RESOURCES"]["TUNGSTEN"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=2500),
    "LARGE SHREDDER": Object("LARGE SHREDDER", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["SMELTED_RESOURCES"]["IRON"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=2500),
    "VTOL": Object("VTOL", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["COMP_RESOURCES_1"]["SILICONE"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"]),

    # Tier 4
    "AUTO EXTRACTOR": Object("AUTO EXTRACTOR", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=7500),
    "EXTRA LARGE SHREDDER": Object("EXTRA LARGE SHREDDER", ALL_RESOURCES["COMP_RESOURCES_1"]["TUNGSTEN CARBIDE"], ALL_RESOURCES["COMP_RESOURCES_1"]["STEEL"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=5000),
    "LARGE ROVER": Object("LARGE ROVER", ALL_RESOURCES["COMP_RESOURCES_1"]["ALUMINUM ALLOY"], ALL_RESOURCES["COMP_RESOURCES_1"]["RUBBER"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=5000),
    "LARGE SHUTTLE": Object("LARGE SHUTTLE", ALL_RESOURCES["COMP_RESOURCES_3"]["TITANIUM ALLOY"], ALL_RESOURCES["SMELTED_RESOURCES"]["CERAMIC"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], ALL_RESOURCES["BUILDINGS_2"]["EXO CHIP"], bytes=5000),
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

check_version.run(1.1, "astroneerlookup", "https://github.com/Isangedal/Astroneer-Lookup/releases/latest/download/Astroneer.Lookup.exe")

helpMsg = "\n\nWelcome to Astroneer Lookup!\n\nType a resource name or the name of a building to find out how to make it!\nType \"/items\" or \"/buildings\" (without the \"\") to see which items and buildings you can ask for\nType \"/exit\" to close the program\nType \"/help\" to view this message at any time\n\n"
print(helpMsg)

while True:
    
    req = input("Lookup: ")

    clear()

    if req.startswith("/"): # Commands
        nl = '\n'

        if req.lower() == "/items": # Display all items
            for i in ALL_RESOURCES:
                if i in ["RESOURCES", "SMELTED_RESOURCES", "ATMO_RESOURCES"]:
                    print(f"{i.replace('_', ' ')}:\n    {f'{nl}    '.join(ALL_RESOURCES[i])}\n")
                elif i in ["COMP_RESOURCES_1", "COMP_RESOURCES_2", "COMP_RESOURCES_3", "COMP_RESOURCES_4"]:
                    if i == "COMP_RESOURCES_1":
                        print("COMP RESOURCES:")
                    print(f"    {f'{nl}    '.join(ALL_RESOURCES[i])}")
            print("\n")

        elif req.lower() == "/buildings": # Display all buildings
            for i in ALL_RESOURCES:
                if i in ["BUILDINGS", "BUILDINGS_2", "BUILDINGS_3"]:
                    print(f"{f'{nl}'.join(ALL_RESOURCES[i])}")
            print("\n")
                    
        elif req.lower() == "/exit": # Exit program
            sys.exit()
        
        elif req.lower() == "/help": # Display the help message
            print(helpMsg)
            check_version.run(1.1, "https://astroneerlookup.7m.pl/check_version.php", "https://github.com/Isangedal/Astroneer-Lookup/releases/latest/download/Astroneer.Lookup.exe")

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
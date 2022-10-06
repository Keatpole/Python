import os, sys, check_version

ZONES = {
    "CLIFFS": "cf",
    "CROSSROADS": "cr",
    "GREENPATH": "gp",
    "CANYON": "cy",
    "WASTES": "wt",
    "CITY": "ct",
    "WATERWAYS": "ww",
    "DEEPNEST": "dn",
    "BASIN": "bs",
    "EDGE": "eg",
    "PEAK": "pa",
    "GROUNDS": "gu",
    "GARDENS": "ga",
    "PALACE": "pc",
    "TRAM": "ta"
}

AREAS = {
    "CF": {
        "DIRTMOUTH": "d",
        "MATO": "m"
    },
    "CR": {
        "HOT SPRINGS": "h",
        "STAG": "st",
        "SALUBRA": "su",
        "ANCESTRAL MOUND": "a",
        "BLACK EGG TEMPLE": "b"
    },
    "GP": {
        "WATERFALL": "w",
        "STONE SANCTUARY": "sa",
        "TOLL": "t",
        "STAG": "st",
        "LAKE OF UNN": "l",
        "SHEO": "sh"
    },
    "CY": {
        "ARCHIVES": "a"
    },
    "WT": {
        "QUEEN'S STATION": "s",
        "LEG EATER": "l",
        "BRETTA": "b",
        "MANTIS VILLAGE": "v"
    },
    "CT": {
        "QUIRREL": "q",
        "TOLL": "t",
        "CITY STOREROOMS": "st",
        "WATCHER'S SPIRE": "sp",
        "KING'S STATION": "si",
        "PLEASURE HOUSE": "h"
    },
    "WW": {
        "WATERWAYS": "ww",
        "GODHOME ATRIUM": "a",
        "GODHOME ROOF": "r",
        "HALL OF GODS": "h"
    },
    "DN": {
        "HOT SPRINGS": "s",
        "FAILED TRAMWAY": "t",
        "BEAST'S DEN": "d"
    },
    "BS": {
        "TOLL": "t",
        "HIDDEN STATION": "s"
    },
    "EG": {
        "ORO": "o",
        "CAMP": "ca",
        "COLOSSEUM": "co",
        "HIVE": "h"
    },
    "PA": {
        "DARK ROOM": "d",
        "CRYSTAL GUARDIAN": "g"
    },
    "GU": {
        "STAG": "s",
        "GREY MOURNER": "m"
    },
    "GA": {
        "CORNIFER": "c",
        "TOLL": "t",
        "STAG": "s"
    },
    "PC": {
        "ENTRANCE": "e",
        "ATRIUM": "a",
        "BALCONY": "b"
    },
    "TA": {
        "UPPER TRAM": "u",
        "LOWER TRAM": "l"
    }
}

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

clear()

def enc():
    def help():
        check_version.run(1.0, "hkbw", "https://github.com/Isangedal/HKBW/releases/latest/download/hkbw.exe")
        print("\n\nEnter the zone and area of the bench here.\nDo \"/benches\" (without the \"\") to see all benches.\nDo \"/help\" to see this message again.\nDo \"/decrypt\" to change your mind and decrypt a code.\nExample: Cliffs Dirtmouth\n")
    help()
    while True:
        req = input("\nBench: ")
        clear()

        if req.startswith("/"):
            if req.lower() == "/help":
                help()
            elif req.lower() == "/benches":
                for i in ZONES:
                    print(f"{i}:")
                    for v in AREAS[ZONES[i].upper()]:
                        print(f"    {v}")
                    print()
            elif req.lower() == "/decrypt":
                dec()
            else:
                print(f"Could not find command: \"{req}\"")

            continue

        req = [req.split(" ")[0], req[len(req.split(" ")[0]+" "):]]

        if len(req) == 1:
            print(f"Could not find zone / area.")
            continue

        if not req[0].upper() in ZONES:
            print(f"Could not find zone: \"{req[0]}\"")
            continue

        zone = ZONES[req[0].upper()].upper()
        
        if not req[1].upper() in AREAS[zone]:
            print(f"Could not find area: \"{req[1]}\"")
            continue

        area = AREAS[zone][req[1].upper()]

        print(zone.lower()+area)

def dec():
    def help():
        check_version.run(1.0, "hkbw", "https://github.com/Isangedal/HKBW/releases/latest/download/hkbw.exe")
        print("\n\nEnter the code given to you here.\nDo \"/help\" to see this message again.\nDo \"/encrypt\" to change your mind and encrypt a code.\nExample: cfd\n")
    help()
    while True:
        req = input("\nCode: ")
        clear()

        if req.startswith("/"):
            if req.lower() == "/help":
                help()
            elif req.lower() == "/encrypt":
                enc()
            else:
                print(f"Could not find command: \"{req}\"")

            continue

        if len(req) == 0:
            print(f"Could not validate code. (ZoneOrAreaInvalid)")
            continue

        req = [req[:2], req[2:]]

        zone = None
        for i in ZONES:
            if req[0] == ZONES[i]:
                zone = i
        if not zone:
            print("Could not validate code. (ZoneInvalid)")
            continue

        area = None
        for i in AREAS[req[0].upper()]:
            if req[1] == AREAS[req[0].upper()][i]:
                area = i
        if not area:
            print("Could not validate code. (AreaInvalid)")
            continue

        b = ""
        m = 1
        for i in area.split(" "):
            if m == len(area.split(" ")):
                break
            b += " "+area.split(" ")[m].lower().capitalize()
            m += 1

        print(f"{zone.lower().capitalize()} {area.split(' ')[0].lower().capitalize()}{b}")

while True:
    c = input("Would you like to encrypt or decrypt? ").lower()
    clear()
    if c == "e" or c == "encrypt":
        enc()
    elif c == "d" or c == "decrypt":
        dec()
    else:
        print("Please put \"encrypt\" or \"decrypt\".\n")
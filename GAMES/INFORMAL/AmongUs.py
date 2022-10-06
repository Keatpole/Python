# Among Us Turn thing
import random, os, sys

# Settings
maxImposters = 1
maxPlayers = 3

colors = {"red", "blue", "pink", "brown", "white", "black", "gray", "green", "yellow", "orange"}
locations = ["Start", "Lab", "Electrical", "Meeting"]
meetingroom = "Meeting"

class Player():
    def __init__(self, color):
        self.color = color
        self.type = "Crewmate"
        self.location = "Meeting"
        self.dead = False
        self.killTarget = None
        self.seen = {}
        

players = {}

while len(players) < maxPlayers:
    for c in colors:
        if len(players) < maxPlayers:
            players[c] = Player(c)


def cls():
    if sys.platform == "win32": os.system("cls")
    else: os.system("clear")


def StartGame():

    cls()

    imposters = 0

    while imposters < maxImposters:
        for p in players:
            if imposters >= maxImposters:
                break

            if random.randint(0, maxImposters) == 0:
                players[p].type = "Imposter"
                imposters += 1

    StartTurn(list(players.values())[0], 0)


def StartTurn(p, pi):
    # Players turn

    if p.killTarget:
        for plr in players:
            plr = players[plr]

            if plr.location == p.killTarget.location and plr != p:
                plr.seen[p.color] = "Murder"

        p.killTarget.dead = True
        print(f"You killed {p.killTarget.color.capitalize()}\n")
        p.killTarget = None


    if p.dead:
        input("You are dead.\n")
        del players[p.color]
        if pi + 1 >= len(players.values()): pi = -1
        StartTurn(list(players.values())[pi+1], pi+1)

    if len(p.seen) > 0:
        for i in p.seen:
            saw = p.seen[i]

            if saw == "Murder":
                saw = "murder someone"

            print(f"You saw {i} {saw}.\n")

    actions = "go to (location), search, call a meeting"
    if p.type == "Imposter": actions += ", kill (player), sabotage (sabotage name)"

    print(f"{p.color.capitalize()}'s turn!")
    print(f"The actions are: {actions}")

    action = input()

    cls()

    if action.startswith("go to "):
        newloc = action.split("go to ")[1].lower()

        if newloc != p.location.lower() and newloc in locations:
            newloc = newloc.capitalize()

            p.location = newloc
            print(f"Went to {newloc}\n")

    elif action.startswith("search"):
        i = []

        for plr in players:
            if players[plr].location == p.location and plr != p.color:
                i.append(plr.capitalize())

        print(f"The people here are: {', '.join(i)}\n")

        StartTurn(p, pi)

    elif action.startswith("call a meeting"):
        if p.location == meetingroom:
            
            # Call a meeting
            pass

        else:
            print(f"You need to be in \"{meetingroom}\" to call a meeting.\n")
            StartTurn(p, pi)

    # Imposter Actions
    elif p.type == "Imposter":

        if action.startswith("kill "):
            target = players[action.split("kill ")[1].lower()]

            if target.location == p.location and target.color != p.color:
                p.killTarget = target

                print(f"You are getting ready to kill {target.color.capitalize()}\n")


    if pi + 1 >= len(players.values()): pi = -1
    StartTurn(list(players.values())[pi+1], pi+1)


StartGame()

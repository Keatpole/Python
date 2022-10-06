import random
import os
import sys

MAX_SIGILS = 4


class Card:
    def __init__(self, name, attack, hp, blood_cost=None, bone_cost=None, sigils=None):
        if sigils is None:
            sigils = []
        self.name = name
        self.attack = attack
        self.hp = hp
        self.blood_cost = blood_cost
        self.bone_cost = bone_cost
        self.sigils = sigils
        self.stinkyed = False
        if blood_cost is None and bone_cost is None:
            self.blood_cost = 0

    def get(self, var):
        return self.__dict__.get(var)

    def set(self, var, val):
        self.__dict__[var] = val

    def add_sigil(self, sigil):
        if len(self.sigils) >= MAX_SIGILS:
            return False
        self.sigils.append(sigil)
        return True

    def rem_sigil(self, sigil):
        self.sigils.remove(sigil)

    def contains_sigil(self, sigil):
        for i in self.sigils:
            if i == sigil:
                return True
        return False


CARDS = {
    "Stoat": Card("Stoat", 1, 3, 1),
    "Stinkbug": Card("Stinkbug", 1, 2, None, 2, ["Stinky"]),
    "Stunted Wolf": Card("Stunted Wolf", 2, 2, 2),
    "Wolf": Card("Wolf", 3, 2, 2),
    "Coyote": Card("Coyote", 2, 1, None, 4),
    "Grizzly": Card("Grizzly", 4, 6, 3),
    "Geck": Card("Geck", 1, 1),
    "Ring Worm": Card("Ring Worm", 0, 1, 1),
    "Worker Ant": Card("Worker Ant", 0, 2, 1, None, ["Cooperation"]),
    "Bullfrog": Card("Bullfrog", 1, 3, 1, None, ["Mighty Leap"]),
    "Magpie": Card("Magpie", 1, 1, 2, None, ["Airborne", "Hoarder"]),  # Not done hoarder
    "Sparrow": Card("Sparrow", 1, 2, 1, None, ["Airborne"]),
    "Turkey Vulture": Card("Turkey Vulture", 3, 3, None, 8, ["Airborne"]),
    "Bat": Card("Bat", 2, 1, 1, None, ["Airborne"]),
    "Kingfisher": Card("Kingfisher", 1, 1, 1, None, ["Waterborne", "Airborne"]),
    "River Otter": Card("River Otter", 1, 1, 1, None, ["Waterborne"]),
    "Great White": Card("Great White", 4, 2, 3, None, ["Waterborne"]),
    "Mantis": Card("Mantis", 1, 1, 1, None, ["Bifurcated Strike"]),
    "Mantis God": Card("Mantis God", 1, 1, 1, None, ["Trifurcated Strike"]),
    "Ant Queen": Card("Ant Queen", 0, 3, 2, None, ["Cooperation"]),
    "Cat": Card("Cat", 0, 1, 1, None, ["Many Lives"]),
    "Child 13": Card("Child 13", 0, 1, 1, None, ["Many Lives"]),
    "Card Tentacle": Card("Card Tentacle", 0, 2, 1, None, ["Card Counter"]),
    "Mirror Tentacle": Card("Mirror Tentacle", 0, 2, 1, None, ["Other Attack Counter"]),
    "Bell Tentacle": Card("Bell Tentacle", 0, 2, 1, None, ["Bell Ringer"]),
    "Mole Man": Card("Mole Man", 0, 6, 1, None, ["Mighty Leap"]),
    "Cockroach": Card("Cockroach", 1, 1, None, 4, ["Unkillable"]),
    "Elk": Card("Elk", 2, 4, 2),
    "Blood Goat": Card("Blood Goat", 0, 1, 1, None, ["Good Sacrifice"]),
    "Boulder": Card("Boulder", 0, 5, sigils=["Cannot Sacrifice"]),
    "Pack Rat": Card("Pack Rat", 2, 2, 2, None, ["Hoarder"])  # not done
}

squirrel = Card("Squirrel", 0, 1)

squirrel_deck = []
deck = []
hand = []
battlefield = [[], []]

queue = []

blood = 0
bones = 0

health = 0

bell_rung = 0

OPPONENT_AI = False
DEBUG = True

if DEBUG:
    #for i in range(3):
    #    battlefield[1].append(CARDS["Magpie"])
    for _ in range(30):
        squirrel_deck.append(squirrel)
        #deck.append(CARDS["Bullfrog"])
    for i in range(10):
        card = random.choice(list(CARDS.items()))
        deck.append(card[1])


def cls():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def print_info():
    cls()
    print("-----------------------")
    print("----- INSCRYPTION -----")
    print("-----------------------\n")
    print("--- STATS ---")
    print(f"Health: {health}")
    print(f"Bones: {bones}")
    print(f"Blood: {blood}")
    print("-------------\n")
    print("--- HAND ---")
    for i in range(len(hand)):
        print(hand[i].get("name"))
    print("------------\n")


def print_battle_info():
    print("-------------")
    print("--- QUEUE ---")
    sb = ""
    for i in queue:
        sigils = f" | [{', '.join(i.sigils)}]" if len(i.sigils) > 0 else ""
        sb += f"({i.name}: {i.attack} / {i.hp}{sigils}) | "
    if sb != "":
        print(sb[:-3])
    new_line = "   (EMPTY)\n" if len(queue) <= 0 else ""
    print(f"{new_line}-------------\n")
    print("--- BATTLEFIELD ---")
    sb = ""
    for i in battlefield[1]:
        sigils = f" | [{', '.join(i.sigils)}]" if len(i.sigils) > 0 else ""
        sb += f"({i.name}: {i.attack} / {i.hp}{sigils}) | "
    if sb != "":
        print(sb[:-3])
    new_line = "      (EMPTY)\n" if len(battlefield[1]) <= 0 else ""
    print(f"{new_line}-------------------")
    sb = ""
    for i in battlefield[0]:
        sigils = f" | [{', '.join(i.sigils)}]" if len(i.sigils) > 0 else ""
        sb += f"({i.name}: {i.attack} / {i.hp}{sigils}) | "
    if sb != "":
        print(sb[:-3])
    new_line = "      (EMPTY)\n" if len(battlefield[0]) <= 0 else ""
    print(f"{new_line}-------------------\n")


def opponent_turn():
    if OPPONENT_AI:

        for i, v in enumerate(queue):
            try:
                battlefield[1][i]
            except IndexError:
                battlefield[1].insert(i, v)
                del queue[i]

        r = random.choice(list(CARDS.items()))

        queue.append(r[1])

        attack(1)

    player_turn()


def draw_card():
    print_info()
    print_battle_info()
    if len(squirrel_deck) > 0:
        if len(deck) > 0:
            card_to_draw = input(
                "Do you want to get a random card in your deck or a \"Squirrel\"?\n[1: Random, 2: Squirrel]\n").lower()
            if card_to_draw == "1" or card_to_draw.startswith("rand"):
                random.shuffle(deck)
                hand.append(deck.pop())
            elif card_to_draw == "2" or card_to_draw.startswith("squ"):
                hand.append(squirrel_deck.pop())
            else:
                input("\nPlease enter a valid option!\n")
                draw_card()
        else:
            input("Your deck is empty\nDrew a \"Squirrel\".\n")
            hand.append(squirrel_deck.pop())
    else:
        if len(deck) > 0:
            input("You have no more squirrels\nDrew a random card.\n")
            random.shuffle(deck)
            hand.append(deck.pop())


def sacrifice_card(needed_blood):
    global blood, bones

    cls()

    print_info()
    print_battle_info()

    if len(battlefield[0]) <= 0:
        input("You do not have any more cards to sacrifice!\n")
        place_card()

    print("Type \"back\" to go back.\n")

    sb = "Choose a card to sacrifice.\n["
    for i, v in enumerate(battlefield[0]):
        sigils = f" | [{', '.join(v.sigils)}]" if len(v.sigils) > 0 else ""
        cost = f"{v.bone_cost} Bones" if v.bone_cost is not None else f"{v.blood_cost} Blood"
        sb += f"{i + 1}: ({v.name} {{{cost}}} : {v.attack} / {v.hp}{sigils}),\n"
    sb = sb[:-2] + "]\n"

    card_to_sac = input(sb).lower()

    if card_to_sac == "back":
        place_card()

    try:
        card_to_sac = battlefield[0][int(card_to_sac) - 1]
    except ValueError:
        print_info()
        print_battle_info()
        input("Please enter a valid number.\n")
        sacrifice_card(needed_blood)

    if card_to_sac.contains_sigil("Cannot Sacrifice"):
        print_info()
        print_battle_info()
        input("You cannot sacrifice that card.\n")
        sacrifice_card(needed_blood)

    gained_blood = 1

    if card_to_sac.contains_sigil("Good Sacrifice"):
        gained_blood = 3

    if not card_to_sac.contains_sigil("Many Lives"):
        battlefield[0].remove(card_to_sac)
        bones += 1
        if card_to_sac.contains_sigil("Unkillable"):
            hand.append(card_to_sac)

    blood += gained_blood

    if len(battlefield[0]) > 0 and blood < needed_blood:
        sacrifice_card(needed_blood)


def place_card():
    global blood, bones

    cls()

    print_info()
    print_battle_info()

    print("Type \"back\" to go back.\n")

    sb = "Which card do you want to place?\n"
    for i, v in enumerate(hand):
        sigils = f" | [{', '.join(v.sigils)}]" if len(v.sigils) > 0 else ""
        cost = f"{v.bone_cost} Bones" if v.bone_cost is not None else f"{v.blood_cost} Blood"
        sb += f"{i + 1}: ({v.name} {{{cost}}} : {v.attack} / {v.hp}{sigils}),\n"
    sb = sb[:-2] + "\n"

    card_to_place = input(sb).lower()

    if card_to_place == "back":
        player_turn(False)

    try:
        card_to_place = hand[int(card_to_place) - 1]
    except ValueError:
        print_info()
        print_battle_info()
        input("Please enter a valid number.\n")
        place_card()

    if card_to_place.bone_cost is not None:
        # Costs bones
        if bones >= card_to_place.bone_cost:
            bones -= card_to_place.bone_cost
        else:
            print_info()
            print_battle_info()
            input("You cannot afford that!\n")
            place_card()
    elif card_to_place.blood_cost > 0:
        # Costs blood
        if blood >= card_to_place.blood_cost:
            blood -= card_to_place.blood_cost
        else:
            sacrifice_card(card_to_place.blood_cost)
            if blood >= card_to_place.blood_cost:
                blood -= card_to_place.blood_cost
            else:
                print_info()
                print_battle_info()
                input("You cannot afford that!\n")
                place_card()

    if len(battlefield[0]) >= 4:
        input("Your side of the battlefield is full!\n")
        player_turn(False)

    hand.remove(card_to_place)
    battlefield[0].append(card_to_place)

    for i, v in enumerate(battlefield[0]):
        if v.contains_sigil("Stinky") and len(battlefield[1]) >= i and battlefield[1][i].attack > 0 and not battlefield[i][i].stinkyed:
            battlefield[1][i].attack -= 1
            battlefield[1][i].stinkyed = True
        if v.contains_sigil("Cooperation"):
            damage = 0
            for i in battlefield[0]:
                if i.contains_sigil("Cooperation"):
                    damage += 1
            v.attack = damage
        if v.contains_sigil("Card Counter"):
            v.attack = len(hand)
        if v.contains_sigil("Bell Ringer"):
            v.attack = bell_rung
        if v.contains_sigil("Other Attack Counter"):
            damage = 0
            for i in battlefield[1]:
                damage += i.attack
            v.attack = damage

    print_info()
    print_battle_info()


def finish_battle(win):
    cls()
    if win:
        print("You won!")
    else:
        print("You lost!")
    sys.exit(0)


def attack(plr):
    global health, bones

    other_plr = 1 if plr == 0 else 0

    for i, v in enumerate(battlefield[plr]):
        ob = battlefield[other_plr]
        damage = 0
        damage_times = 1
        damage_face = False
        if v.contains_sigil("Bifurcated Strike"):
            damage_times = 2
        if v.contains_sigil("Trifurcated Strike"):
            damage_times = 3
        if len(ob) > i and ob[i] is not None:
            if v.contains_sigil("Airborne") and not ob[i].contains_sigil("Mighty Leap"):
                damage_face = True
                if plr == 0:
                    for i in range(damage_times):
                        health += v.attack
                else:
                    for i in range(damage_times):
                        health -= v.attack
            elif not ob[i].contains_sigil("Waterborne"):
                for _ in range(damage_times):
                    ob[i].hp -= v.attack
        else:
            damage_face = True
            if plr == 0:
                for _ in range(damage_times):
                    health += v.attack
            else:
                for _ in range(damage_times):
                    health -= v.attack
        if not damage_face and ob[i].hp <= 0:
            del battlefield[other_plr][i]
            if other_plr == 0:
                bones += 1
                if ob[i].contains_sigil("Unkillable"):
                    hand.append(ob[i])
    print_info()
    print_battle_info()
    if health >= 5:
        input()
        finish_battle(True)
    elif health <= -5:
        input()
        finish_battle(False)


def player_turn(draw=True):
    global health, blood, bell_rung

    print_info()

    if draw:
        draw_card()

    print_info()

    while True:
        print_info()
        print_battle_info()

        action = input("[1: Place a card, 2: End Turn, 3: Use Item]\n").lower()

        if action == "1" or action.startswith("place"):
            place_card()
        elif action == "2" or action.startswith("end"):
            break
        elif action == "3" or action.startswith("use"):
            # TODO: Implement items
            print_info()
            print_battle_info()
            input("You want to use an item.")
            pass
        else:
            print_info()
            print_battle_info()
            input("Please enter a valid option!\n")

    attack(0)

    blood = 0

    for i in battlefield[0]:
        if i.contains_sigil("Cannot Sacrifice After Many Lives"):
            i.rem_sigil("Cannot Sacrifice After Many Lives")

    bell_rung += 1

    opponent_turn()


def start_battle():
    hand.append(squirrel)
    for i in range(3):
        random.shuffle(deck)
        hand.append(deck.pop())
    player_turn(False)


start_battle()

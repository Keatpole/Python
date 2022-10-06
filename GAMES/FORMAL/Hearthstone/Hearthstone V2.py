import random, os, sys

#cards = {
#    "Mage": {
#        "Test Minion 1": ["Test 1", "Battlecry: Test stuff", "Minion", 1, [""], [1,1]],
#        "Test Minion 2": ["Test 2", "Battlecry: Test more stuff", "Minion", 2, [""], [2,2]],
#        "Test Minion 3": ["Test 3", "Battlecry: Test even more stuff", "Minion", 3, [""], [3,3]],
#        "Test Minion 4": ["Test 4", "Battlecry: Test all the stuff", "Minion", 4, [""], [4,4]],
#        "Test Minion 5": ["Test 5", "Battlecry: Test nothing but the stuff", "Minion", 5, [""], [5,5]]
#    },
#    "Uncollectible": {
#        "The Coin": ["The Coin", "Gain 1 mana crystal this turn only.", "Spell", 0, ["spell tm 1"]],
#        "Free Cards": ["Free Cards", "All cards are free!", "Spell", 0, ["spell cca 0"]],
#        "Draw 1 Card": ["Draw 1 Card", "Draw 1 card, return this card to your hand", "Spell", 2, ["spell dc 1", "spell ac Draw_1_Card"]],
#        "The Boomer": ["The Boomer", "Take 1 damage from old age, add \"Die\" to your hand", "Spell", 0, ["spell doh 1", "spell ac Die_From_Old_Age"]],
#        "Die From Old Age": ["Die", "Die from old age", "Spell", 0, ["spell doh 9999"]]
#    }
#}

class Card():
    def __init__(self, name, desc, type, cost, effects, stats):
        self.name = name
        self.desc = desc
        self.type = type
        self.cost = cost
        self.effects = effects
        self.stats = stats
        pass
    def changeHealth(self, hp):
        self.stats[1] -= hp
    def defTurn(self, turn_summoned):
        self.turn_summoned = turn_summoned

cards = {
    "Mage": {
        "Test Minion 1": Card("Test 1", "Battlecry: Test stuff", "Minion", 1, [""], [1,1]),
        "Test Minion 2": Card("Test 2", "Battlecry: Test more stuff", "Minion", 2, [""], [2,2]),
        "Test Minion 3": Card("Test 3", "Battlecry: Test even more stuff", "Minion", 3, [""], [3,3]),
        "Test Minion 4": Card("Test 4", "Battlecry: Test all the stuff", "Minion", 4, [""], [4,4]),
        "Test Minion 5": Card("Test 5", "Battlecry: Test nothing but the stuff", "Minion", 5, [""], [5,5])
    },
    "Uncollectible": {
        "The Coin": Card("The Coin", "Gain 1 mana crystal this turn only.", "Spell", 0, ["spell tm 1"], [0,0])
    }
}

decks = {1: [], 2: []}
hands = {1: [], 2: []}

battlefield = {
    1: ["", "", "", "", "", "", ""],
    2: ["", "", "", "", "", "", ""]
}

# Build Test Deck
#for _ in range(6):
#    for v in range(5):
#        decks[1].append(cards["Mage"][f"Test Minion {v+1}"])
#        decks[2].append(cards["Mage"][f"Test Minion {v+1}"])

for _ in range(30):
    card = cards["Mage"]["Test Minion 1"]

    card1 = Card(card.name, card.desc, card.type, card.cost, card.effects, card.stats)
    card2 = Card(card.name, card.desc, card.type, card.cost, card.effects, card.stats)

    decks[1].append(card1)
    decks[2].append(card2)

health = {1: 30, 2: 30}
fatigue = {1: 1, 2: 1}
mana = {1: [1, 1], 2: [1, 1]} # [Empty mana, Current mana]

turn = 1

classes = ["Mage", "Mage"]

def clear():
    if sys.platform == "win32": os.system("cls")
    else: os.system("clear")


def other_player(p):
    if p == 1:
        return 2
    elif p == 2:
        return 1


def check_dead(p, reason):
    if health[p] <= 0:
        end_game(other_player(p), reason)


def draw_card(p):
    if len(decks[p]) < 1:
        health[p] -= fatigue[p]
        fatigue[p] += 1
        check_dead(p, "fatigue")
        return
    card = decks[p].pop()
    to_add = Card(card.name, card.desc, card.type, card.cost, card.effects, card.stats)
    if len(hands[p]) >= 10:
        clear()
        input(f"Player {p} just burned a {to_add.name}\n")
    else:
        hands[p].append(to_add)


def end_game(p, reason):
    clear()
    input(f"Player {p} won by {reason}!\n")
    clear()
    sys.exit()


def start_game():
    clear()

    first = random.randint(1,2)
    second = None

    if first == 1: second = 2
    elif first == 2: second = 1

    draw_card(first);draw_card(first);draw_card(first)
    draw_card(second);draw_card(second);draw_card(second);draw_card(second)

    hands[second].append(cards["Uncollectible"]["The Coin"])
    
    draw_card(first)
    play_cards(first)


def end_turn(p):
    global turn
    if p == 1:
        turn += 1
    if mana[p][0] < 10:
        mana[p][0] += 1
    mana[p][1] = mana[p][0]
    draw_card(other_player(p))
    play_cards(other_player(p))


def show_info(p):
    print(f"\nPlayer {str(p)}:\n")
    print(f"You have {len(decks[p])} cards left in your deck")
    print(f"You have {len(hands[p])} cards in your hand")
    print(f"You have {health[p]}/30 health")
    print(f"You have {mana[p][1]}/{mana[p][0]} mana\n")
    print("----- Battlefield -----\n")
    shown_battlefield = f"Player {other_player(p)}: "
    dashes = ""
    for i in battlefield[other_player(p)]:
        if i != "":
            shown_battlefield += f"{i.name} [{i.stats[0]} / {i.stats[1]}] - "
            dashes += "-"*len(i.name)
        else:
            shown_battlefield += "(empty) - "
            dashes += "-"*len("(empty) - ")
    print(shown_battlefield)
    print("\n"+dashes)
    shown_battlefield = f"Player {p}: "
    for i in battlefield[p]:
        if i != "": 
            shown_battlefield += f"{i.name} [{i.stats[0]} / {i.stats[1]}] - "
        else:
            shown_battlefield += "(empty) - "
    print("\n"+shown_battlefield)
    print("\n-----------------------\n")


def use_battlefield(p):
    clear()
    show_info(p)
    to_attack_num = input("Choose a minion to attack with (1 - 7) (Type \"return\" to go back)\n")
    if to_attack_num.lower() == "return":
        play_cards(p)
        return
    try:
        to_attack_num = int(to_attack_num)
        to_attack = battlefield[p][to_attack_num-1]
    except:
        clear()
        input("That is not a valid minion.\n")
        use_battlefield(p)
    clear()

    if turn <= to_attack.turn_summoned:
        input(f"This minion cannot attack this turn. Wait 1 turn.\n")
        use_battlefield(p)
        return

    show_info(p)

    target_num = input("Choose a target to attack (1 - 7) (Type \"hero\" to attack the hero) (Type \"return\" to go back)\n")
    if target_num.lower() == "return":
        play_cards(p)
        return

    if target_num.lower() == "hero":
        clear()
        health[other_player(p)] -= to_attack.stats[0]
        input(f"Player {other_player(p)} has {health[other_player(p)]} health left!\n")
        play_cards(p)
        return

    try:
        target_num = int(target_num)
        target = battlefield[other_player(p)][target_num-1]
    except:
        clear()
        input("That is not a valid target.\n")
        use_battlefield(p)

    #target.stats[1] -= to_attack.stats[0] # Target loses health
    #to_attack.stats[1] -= target.stats[0] # Attacker loses health

    target.changeHealth(to_attack.stats[0]) # Target loses health
    to_attack.changeHealth(target.stats[0]) # Attacker loses health

    if target.stats[1] < 0:
        target.stats[1] = 0
    if to_attack.stats[1] < 0:
        to_attack.stats[1] = 0

    clear()
    input(f"{to_attack.name} attacked {target.name}.\n{target.name} now has {target.stats[1]} health left.\n{to_attack.name} now has {to_attack.stats[1]} health left.\n")
    if to_attack.stats[1] <= 0:
        battlefield[p].remove(to_attack)
        battlefield[p].insert(len(battlefield[p]), "")
    if target.stats[1] <= 0:
        battlefield[other_player(p)].remove(target)
        battlefield[other_player(p)].insert(len(battlefield[other_player(p)]), "")

    play_cards(p)


def play_cards(p):
    clear()
    show_info(p)
    if len(hands[p]) == 0:
        print("You have no cards.")
    else:
        for card in hands[p]:
            if card.type == "Minion":
                print(f"{card.name} - Minion - {card.cost} Mana - {card.stats[0]} / {card.stats[1]} - {card.desc}")
            elif card.type == "Spell":
                print(f"{card.name} - Spell - {card.cost} Mana - {card.desc}")
    to_play = input("\nWhat card do you want to play? (Name of card) (Type \"end\" to end turn) (Type \"attack\" to attack with a minion on the battlefield)\n")
    if to_play.lower() == "end":
        end_turn(p)
        return
    elif to_play.lower() == "attack":
        use_battlefield(p)
        return
    allg = False
    enough_space = False
    for card in hands[p]:
        if to_play.lower() == card.name.lower():
            print(battlefield[p])
            if (mana[p][1] >= card.cost):
                for i,v in enumerate(battlefield[p]):
                    if v == "":
                        enough_space = True
                        hands[p].remove(card)
                        handle_card_text(card, p)
                        mana[p][1] -= card.cost
                        if (card.type == "Minion"):
                            new_card = Card(card.name, card.desc, card.type, card.cost, card.effects, card.stats)
                            battlefield[p][i] = new_card
                            new_card.defTurn(turn)
                        break
                allg = True
                break
            else:
                clear()
                input("You do not have enough mana to place this down!\n")
                play_cards(p)
                return
    if not enough_space:
        clear()
        input("You do not have enough space on the battlefield to place this card!\n")
    if not allg:
        clear()
        input("Please check that you typed the name of the card correctly\n")
    play_cards(p)


def handle_card_text(card, p):
    for i in range(len(card.effects)):
        _card = card.effects[i].split(" ")
        if _card[0] == "bc" or _card[0] == "spell":
            if _card[1] == "tm": # Temporary mana
                mana[p][1] += int(_card[2])
                if mana[p][1] > 10:
                    mana[p][1] = 10
            elif _card[1] == "dc": # Draw card
                for _ in range(int(_card[2])):
                    draw_card(p)
            elif _card[1] == "cca": # Change cost all
                for i in decks[p]:
                    i.cost = int(_card[2])
                for i in hands[p]:
                    i.cost = int(_card[2])
            elif _card[1] == "ac": # Add card
                for a in cards:
                    for v in cards[a]:
                        if v == _card[2].replace("_", " "):
                            if len(hands[p]) >= 10:
                                clear()
                                input(f"Player {p} just burned a {hands[p][len(hands[p])-1].name}\n")
                                hands[p] = hands[p][:-1]
                            hands[p].append(cards[a][v])
                            break
            elif _card[1] == "acint": # Add card if not there
                for a in cards:
                    for v in cards[a]:
                        if v == _card[2].replace("_", " "):
                            for f in hands[p]:
                                if f == cards[a][v]:
                                    return
                            if len(hands[p]) >= 10:
                                clear()
                                input(f"Player {p} just burned a {hands[p][len(hands[p])-1].name}\n")
                                hands[p] = hands[p][:-1]
                            hands[p].append(cards[a][v])
                            break
            elif _card[1] == "rc": # Remove card
                for v in hands[p]:
                    if v[0] == _card[2].replace("_", " "):
                        hands[p].remove(v)
            elif _card[1] == "acd": # Add card to deck
                for a in cards:
                    for v in cards[a]:
                        if v == _card[2].replace("_", " "):
                            decks[p].append(v)
            elif _card[1] == "doh": # Damage own hero
                health[p] -= int(_card[2])
                check_dead(p, "reasons")
            elif _card[1] == "deh": # Damage enemy hero
                health[other_player(p)] -= int(_card[2])
                check_dead(other_player(p), "reasons")


start_game()
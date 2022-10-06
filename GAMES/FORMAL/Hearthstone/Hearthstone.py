import random, os, sys

cards = {
    "Mage": {
        "Test Minion 1": ["Test 1", "Battlecry: Test stuff", "Minion", 1, [""], [1,1]],
        "Test Minion 2": ["Test 2", "Battlecry: Test more stuff", "Minion", 2, [""], [2,2]],
        "Test Minion 3": ["Test 3", "Battlecry: Test even more stuff", "Minion", 3, [""], [3,3]],
        "Test Minion 4": ["Test 4", "Battlecry: Test all the stuff", "Minion", 4, [""], [4,4]],
        "Test Minion 5": ["Test 5", "Battlecry: Test nothing but the stuff", "Minion", 5, [""], [5,5]]
    },
    "Uncollectible": {
        "The Coin": ["The Coin", "Gain 1 mana crystal this turn only.", "Spell", 0, ["spell tm 1"]],
        "Free Cards": ["Free Cards", "All cards are free!", "Spell", 0, ["spell cca 0"]],
        "Draw 1 Card": ["Draw 1 Card", "Draw 1 card, return this card to your hand", "Spell", 2, ["spell dc 1", "spell ac Draw_1_Card"]],
        "The Boomer": ["The Boomer", "Take 1 damage from old age, add \"Die\" to your hand", "Spell", 0, ["spell doh 1", "spell ac Die_From_Old_Age"]],
        "Die From Old Age": ["Die", "Die from old age", "Spell", 0, ["spell doh 9999"]]
    }
}

decks = {1: [], 2: []}
hands = {1: [], 2: []}

# Build Test Deck
for _ in range(6):
    for v in range(5):
        decks[1].append(cards["Mage"][f"Test Minion {v+1}"])
        decks[2].append(cards["Mage"][f"Test Minion {v+1}"])

health = {1: 30, 2: 30}
fatigue = {1: 1, 2: 1}
mana = {1: [1, 1], 2: [1, 1]} # [Empty mana, Current mana]

turn = 1

classes = ["Mage", "Mage"]

def clear():
    if sys.platform == "win32": os.system("cls")
    else: os.system("clear")
def get_other_player(p):
    if p == 1:
        return 2
    elif p == 2:
        return 1
def check_dead(p, reason):
    if health[p] <= 0:
        end_game(get_other_player(p), reason)
def draw_card(p):
    if len(decks[p]) < 1:
        health[p] -= fatigue[p]
        fatigue[p] += 1
        check_dead(p, "fatigue")
        return
    to_add = decks[p][random.randint(0, len(decks[p])-1)]
    if len(hands[p]) >= 10:
        clear()
        input(f"Player {p} just burned a {to_add[0]}\n")
    else:
        hands[p].append(to_add)
    decks[p].remove(to_add)

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
    hands[second].append(cards["Uncollectible"]["Draw 1 Card"])
    hands[second].append(cards["Uncollectible"]["Free Cards"])
    hands[second].append(cards["Uncollectible"]["The Boomer"])
    draw_card(first)
    play_cards(first)

def end_turn(p):
    global turn
    turn += 1
    if mana[p][0] < 10:
        mana[p][0] += 1
    mana[p][1] = mana[p][0]
    draw_card(get_other_player(p))
    play_cards(get_other_player(p))

def play_cards(p):
    clear()
    print(f"\nPlayer {str(p)}:\n")
    print(f"You have {len(decks[p])} cards left in your deck")
    print(f"You have {len(hands[p])} cards in your hand")
    print(f"You have {health[p]}/30 health")
    print(f"You have {mana[p][1]}/{mana[p][0]} mana\n")
    if len(hands[p]) == 0:
        print("You have no cards.")
    else:
        for card in hands[p]:
            if card[2] == "Minion":
                print(f"{card[0]} - Minion - {card[3]} Mana - {card[5][0]} / {card[5][1]} - {card[1]}")
            elif card[2] == "Spell":
                print(f"{card[0]} - Spell - {card[3]} Mana - {card[1]}")
    to_play = input("\nWhat card do you want to play? (Name of card) (Type \"end\" to end turn)\n")
    if to_play.lower() == "end":
        end_turn(p)
        return
    allg = False
    for card in hands[p]:
        if to_play.lower() == card[0].lower():
            if (mana[p][1] >= card[3]):
                hands[p].remove(card)
                handle_card_text(card, p)
                mana[p][1] -= card[3]
                allg = True
                break
            else:
                clear()
                input("You do not have enough mana to place this down!\n")
                play_cards(p)
                return
    if not allg:
        clear()
        input("Please check that you typed the name of the card correctly\n")
    play_cards(p)

def handle_card_text(card, p):
    for i in range(len(card[4])):
        _card = card[4][i].split(" ")
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
                    i[3] = int(_card[2])
                for i in hands[p]:
                    i[3] = int(_card[2])
            elif _card[1] == "ac": # Add card
                for a in cards:
                    for v in cards[a]:
                        if v == _card[2].replace("_", " "):
                            if len(hands[p]) >= 10:
                                clear()
                                input(f"Player {p} just burned a {hands[p][len(hands[p])-1][0]}\n")
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
                                input(f"Player {p} just burned a {hands[p][len(hands[p])-1][0]}\n")
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
                health[get_other_player(p)] -= int(_card[2])
                check_dead(get_other_player(p), "reasons")

start_game()
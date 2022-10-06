import random, os, sys

cards = {"Colors": ["Red", "Green", "Blue", "Yellow"], "Specials": ["Wildcard", "+4"], "SpecialsC": ["Skip", "Reverse", "+2"]}

ais = 1
humans = 1
players = ais + humans

minPlayers = 2
maxPlayers = 15
maxDrawnCards = 3

table = f"{cards.get('Colors')[random.randint(0, len(cards.get('Colors')) - 1)]} {random.randint(1, 9)}"
hands = {}

normal_card_chance = [5, 0]
special_card_chance = [10, 9]
specialc_card_chance = [8, 6]

table_wc_val = None
direction = "cw"

def draw_card(p, n):
    drawn = 0
    while drawn < n:
        cardType = random.randint(0, 10)

        if cardType <= normal_card_chance[0] and cardType >= normal_card_chance[1]:
            hands[p].append(f"{cards.get('Colors')[random.randint(0, len(cards.get('Colors')) - 1)]} {random.randint(1, 9)}")
        elif cardType <= special_card_chance[0] and cardType >= special_card_chance[1]:
            hands[p].append(cards.get('Specials')[random.randint(0, len(cards.get('Specials')) - 1)])
        elif cardType <= specialc_card_chance[0] and cardType >= specialc_card_chance[1]:
            hands[p].append(f"{cards.get('Colors')[random.randint(0, len(cards.get('Colors')) - 1)]} {cards.get('SpecialsC')[random.randint(0, len(cards.get('SpecialsC')) - 1)]}")
        
        drawn += 1

def play_card(p, conf, dtt):
   
    global players
    global table
    global table_wc_val
    global direction

    os.system('cls')
    nextConf = False
    if conf:
        input(f"Player {p}'s turn, other players, look away.\n")
    os.system('cls')

    nextp = None
    if direction == "cw":
        nextp = p + 1
        if nextp > players:
            nextp = 1
    elif direction == "ccw":
        nextp = p - 1
        if nextp < 1:
            nextp = players

    hasToPass = False
    canDraw = True

    tableSplit = table.split()
    
    if tableSplit[0] == "+4":
        if len(tableSplit) < 3:
            draw_card(p, 4)
            table = f"{table} (Used)"
            hasToPass = True
    elif tableSplit[1] == "+2":
        if len(tableSplit) < 3:
            draw_card(p, 2)
            table = f"{table} (Used)"
            hasToPass = True

    drawThisTurn = dtt
    if drawThisTurn >= maxDrawnCards:
        canDraw = False

    if p <= humans:
        print(f"Card on table: {table}\n")
        print(f"Player {p}:\n\nCards:")
        for card in hands[p]:
            print(card)

    if hasToPass:
        if p <= humans:
            input("\nPress enter to continue\n")
            os.system('cls')
            play_card(nextp, False, 0)
        else:
            input(f"Player {p} (AI):\n\nPassed\n")
            play_card(nextp, False, 0)

    if p <= humans:
        print()
        for i in range(1, players + 1):
            if i <= humans:
                print(f"Player {i} (Human) has {len(hands[i])} cards left.")
            else:
                print(f"Player {i} (AI) has {len(hands[i])} cards left.")
    
    if p <= humans:
        selectedCard = input("\nWhat card do you want to place?\nType \"draw\" to draw 1 card\nType \"pass\" to pass your turn\n")
    else:
        selectedCard = None
        for card in hands[p]:
            cardSplit = card.split(" ")
            os.system("cls")
            if len(cardSplit) == 1:
                selectedCard = card
                break
            elif cardSplit[0] == tableSplit[0] or cardSplit[1] == tableSplit[1]:
                selectedCard = card
                break
            if tableSplit[0] == "+4" and cardSplit[0] == tableSplit[1].replace("(", "").replace(")", ""):
                selectedCard = card
                break
            elif tableSplit[0] == "Wildcard" and cardSplit[0] == tableSplit[1].replace("(", "").replace(")", ""):
                selectedCard = card
                break
        if selectedCard == None:
            if canDraw:
                drawThisTurn += 1
                draw_card(p, 1)
                play_card(p, False, drawThisTurn)
            else:
                input(f"Player {p} (AI):\n\nPassed\n")
                play_card(nextp, nextConf, 0)

    placedCard = None
    for card in hands[p]:
        if selectedCard.lower() == card.lower():
            placedCard = card
            break

    cheats = True

    if cheats:
        if selectedCard == "Codes":
            os.system('cls')
            input("o?ma!sp! - cards\ns?em? - win\ns!ee!v - give\n")
            play_card(p, False, drawThisTurn)
        if selectedCard == "Cards":
            os.system('cls')
            plr = 1
            while plr <= players:
                print(f"----Player {plr}----")
                for card in hands[plr]:
                    print(card)
                plr += 1
                print("----------------\n")
            input()
            play_card(p, False, drawThisTurn)
        if selectedCard == "Win":
            hands[p] = ["+4"]
            play_card(p, False, drawThisTurn)
        if selectedCard == "Give":
            os.system('cls')
            give = input("Which card do you want?\n")
            giveSplit = give.split()

            if len(giveSplit) == 2:
                if giveSplit[0] in cards["Colors"]:
                    inrange = False
                    for i in range(1,9):
                        inrange = True
                    if inrange or giveSplit[1] in cards["SpecialsC"]:
                        hands[p].append(give)
                        play_card(p, False, drawThisTurn)
                        return
            elif give in cards["Specials"]:
                hands[p].append(give)
                play_card(p, False, drawThisTurn)
                return
            else: 
                input("Invalid Card!")
                play_card(p, False, drawThisTurn)
                return

    if selectedCard == "exit":
        confirmation = input("Are you sure you want to exit? Your progress will not be saved. ( Y / N )\n")
        if confirmation.lower() == "y":
            exit()
        elif confirmation.lower() == "n":
            play_card(p, False, drawThisTurn)
        else:
            input("Please select: Y / N\n")
            play_card(p, False, drawThisTurn)
    if selectedCard == "draw":
        if canDraw:
            drawThisTurn += 1
            draw_card(p, 1)
            play_card(p, False, drawThisTurn)
        else:
            input(f"You can not draw more than {maxDrawnCards} cards per turn.")
            play_card(p, False, drawThisTurn)
    if selectedCard == "pass":
        if drawThisTurn == maxDrawnCards:
            os.system('cls')
            input(f"Player {p} (Human) has passed.\n")
            play_card(nextp, nextConf, 0)
        else:
            os.system('cls')
            input(f"You need to draw {maxDrawnCards} cards to be able to pass.\n")
            play_card(p, conf, dtt)

    if placedCard == None:
        os.system('cls')
        input("Invalid card!\n")
        play_card(p, False, drawThisTurn)
        return

    placedCardSplit = placedCard.split()

    isSpecial = False
    if placedCard in cards.get("Specials"):
        isSpecial = True
    isCSpecial = False
    if len(placedCardSplit) > 1 and placedCardSplit[1] in cards.get("SpecialsC"):
        isCSpecial = True

    successful = None

    if len(tableSplit) != 1:
        if not isSpecial:
            if isCSpecial:
                if placedCardSplit[1] == "Skip":
                    if players == 2:
                        nextp = p
                        nextConf = False
                    elif nextp >= players:
                        nextp = 1
                    else:
                        if direction == "cw":
                            nextp += 1
                        elif direction == "ccw":
                            nextp -= 1
                    if nextp == 0: nextp = players
                    successful = True
                elif placedCardSplit[1] == "Reverse":
                    if direction == "cw":
                        direction = "ccw"
                        nextp = p - 1
                        if players == 2:
                            nextp = p
                            nextConf = False
                        if nextp < 1:
                            nextp = players
                    elif direction == "ccw":
                        direction = "cw"
                        nextp = p + 1
                        if players == 2:
                            nextp = p
                            nextConf = False
                        if nextp > players:
                            nextp = 1
                    successful = True
                elif placedCardSplit[0] == tableSplit[0]:
                    successful = True
                elif placedCardSplit[1] == tableSplit[1]:
                    successful = True
                elif placedCardSplit[0] == table_wc_val:
                    successful = True
                else:
                    successful = False
            else:
                if tableSplit[0] == "Wildcard":
                    if placedCardSplit[0] == table_wc_val or placedCardSplit[0] == tableSplit[0]:
                        successful = True
                elif tableSplit[0] == "+4":
                    if placedCardSplit[0] == table_wc_val or placedCardSplit[0] == tableSplit[0]:
                        successful = True
                else:
                    if placedCardSplit[1] == tableSplit[1] or placedCardSplit[0] == tableSplit[0]:
                        successful = True
                    else:
                        successful = False
        else:
            if placedCard == "Wildcard" or placedCard == "+4":
                if p <= humans:
                    os.system("cls")
                    print(f"Card on table: {table}\n")
                    print(f"Player {p}:\n\nCards:")
                    for card in hands[p]:
                        print(card)
                    color = input("\nSelect your color: Red / Green / Blue / Yellow\n").lower()
                else:

                    for card in hands[p]:
                        r=g=b=y = 0

                        cardSplit = card.split(" ")

                        if cardSplit[0] == "Red":
                            r += 1
                        elif cardSplit[0] == "Green":
                            g += 1
                        elif cardSplit[0] == "Blue":
                            b += 1
                        elif cardSplit[0] == "Yellow":
                            y += 1

                        if r >= g and r >= b and r >= y: color = "red"
                        elif g >= r and g >= b and g >= y: color = "green"
                        elif b >= r and b >= g and b >= y: color = "blue"
                        elif y >= r and y >= g and y >= b: color = "yellow"

                if color == "red":
                    placedCard = f"{placedCard} (Red)"
                    table_wc_val = "Red"
                elif color == "green":
                    placedCard = f"{placedCard} (Green)"
                    table_wc_val = "Green"
                elif color == "blue":
                    placedCard = f"{placedCard} (Blue)"
                    table_wc_val = "Blue"
                elif color == "yellow":
                    placedCard = f"{placedCard} (Yellow)"
                    table_wc_val = "Yellow"
                else:
                    input("Please select a color")
                    play_card(p, False, drawThisTurn)

                successful = True
    else:
        successful = True

    if successful:
        if p <= humans:
            os.system('cls')
            table = placedCard
            print(f"\nYou placed a {placedCard}\n")
            if (placedCardSplit[0] == "Wildcard" or placedCardSplit[0] == "+4"):
                hands[p].remove(placedCardSplit[0])
            else:
                hands[p].remove(placedCard)
            if len(hands[p]) == 0:
                input(f"Player {p} (Human) won!\n")
                exit()
        else:
            table = placedCard
            if (placedCardSplit[0] == "Wildcard" or placedCardSplit[0] == "+4"):
                hands[p].remove(placedCardSplit[0])
            else:
                hands[p].remove(placedCard)
            print(f"Player {p} (AI):\n")
            if drawThisTurn > 0:
                print (f"Drew {drawThisTurn} cards")
            input(f"Placed: {table}\n")
            if len(hands[p]) == 0:
                input(f"Player {p} (AI) won!\n")
                exit()
        
        if nextp <= humans:
            nextConf = True
        play_card(nextp, nextConf, 0)
    else:
        os.system('cls')
        input(f"\nCan not place a {placedCard} on a {table}\n")
        play_card(p, False, drawThisTurn)

def match_start(p):
   
    global hands
    global cards
    global players

    if players < minPlayers:
        raise Exception(f'You can not have less than {minPlayers} players')
    if players > maxPlayers:
        raise Exception(f'You can not have more than {maxPlayers} players')

    if p > players:
        play_card(1, False, 0)
        return

    hands[p] = ["null"]
    draw_card(p, 7)
    del(hands.get(p)[0])

    match_start(p+1)
    
if len(sys.argv) >= 2:
    if sys.argv[1] == "-h":
        print("Usage: py \"UNO AI.py\" -a (Number of AIs) -p (Number of Human Players)")
        sys.exit()
    if len(sys.argv) > 3 and sys.argv[3] == "-p":
        humans = int(sys.argv[4])
    if sys.argv[1] == "-a":
        ais = int(sys.argv[2])
    players = ais + humans

match_start(1)
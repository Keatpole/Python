import random, os, argparse

board = []

dimensions = [9, 9] # 9x9

argparser = argparse.ArgumentParser()

argparser.add_argument("-m", "--mines", type=int, default=10)
argparser.add_argument("-d", "--dimensions", type=int, nargs=2, default=dimensions, metavar=("X", "Y"))

args = argparser.parse_args()

dimensions = args.dimensions

if (dimensions[0] * dimensions[1]) - 9 < args.mines:
    print("Too many mines / too small board")
    exit()

board = [["" for _ in range(dimensions[0])] for _ in range(dimensions[1])]
shown_board = [["O" for _ in range(dimensions[0])] for _ in range(dimensions[1])]
flags = {}
reserved = {}

def generate_mines(board, amount):
    '''
    Generates mines on the board
    
    Arguments:
        board {list} -- The board
        amount {int} -- The amount of mines to generate
    '''

    amount_placed = 0
    board_to_return = board

    while amount_placed < amount:
        for j, i in enumerate(board):
            for k, v in enumerate(i):
                if amount_placed < amount and v != "M" and not (j, k) in reserved and random.randint(0, amount) == 0:
                    board_to_return[j][k] = "M"
                    amount_placed += 1

    return board_to_return

def generate_numbers(board):
    '''
    Generates numbers on the board

    Arguments:
        board {list} -- The board
    '''

    for j, i in enumerate(board):
        for k, v in enumerate(i):
            if v == "M":
                continue

            num = 0

            for x in range(j - 1, j + 2):
                for y in range(k - 1, k + 2):
                    if x < 0 or y < 0 or x >= dimensions[0] or y >= dimensions[1]:
                        continue

                    if board[x][y] == "M":
                        num += 1
                        
            board[j][k] = str(num)

    return board
            
def generate_board(board, mines):
    '''
    Generates the board

    Arguments:
        board {list} -- The board
        mines {int} -- The amount of mines to generate
    '''

    global reserved

    board = generate_mines(board, mines)
    board = generate_numbers(board)

    for i in reserved:
        shown_board[i[0]][i[1]] = board[i[0]][i[1]]
    
    reserved = {}

    return board

def print_board(board):
    '''
    Prints the board

    Arguments:
        board {list} -- The board
    '''

    x = "   MINESWEEPER   "
    print("|" + "-" * len(x) + "|")
    print("|" + x + "|")
    print("|" + "-" * len(x) + "|")
    print()

    for i in board:
        for v in i:
            if v == "" or v == "0":
                v = " "

            print(f"[{v}]", end='')
        print()

def interact(board, real_board, x, y):
    '''
    Interacts with the board

    Arguments:
        board {list} -- The board
        real_board {list} -- The real board
        x {int} -- The x coordinate
        y {int} -- The y coordinate
    '''

    val = board[x][y]
    real_val = real_board[x][y]

    if val != "O":
        return [board, False, "Neutral"]
                
    board[x][y] = real_board[x][y]

    if real_val == "M":
        board = real_board
        return [board, True, "Lost"]

    won = True

    for i in shown_board:
        for v in i:
            if v == "O":
                won = False

    if won:
        return [board, True, "Won"]

    return [board, True, "Neutral"]

def place(board, x, y):
    '''
    Places a mine on the board
    
    Arguments:
        board {list} -- The board
        x {int} -- The x coordinate
        y {int} -- The y coordinate
    '''

    board[x][y] = "M"

    return board

def flag(board, x, y):
    '''
    Flags a mine on the board

    Arguments:
        board {list} -- The board
        x {int} -- The x coordinate
        y {int} -- The y coordinate
    '''

    global flags

    v = board[x][y]

    if v == "F":
        board[x][y] = flags[(x, y)]
        flags.pop((x, y))
    else:
        board[x][y] = "F"
        flags[(x, y)] = v

    return board

def first_click():
    '''
    Make the first click cause an explosion
    '''
    global shown_board

    x = input().lower()

    os.system("cls")

    if x.startswith("f"):
        [_, x, y] = x.split(" ")
        shown_board = flag(shown_board, x, y)
        print_board(shown_board)
        return False
    
    [x, y] = x.split(" ")

    x = int(x) - 1
    y = int(y) - 1

    # Add the clicked square and its surrounding squares to the reserved list
    for i in range(int(x)-1, int(x)+2):
        for j in range(int(y)-1, int(y)+2):
            if i >= 0 and j >= 0 and i < dimensions[0] and j < dimensions[1]:
                reserved[(i, j)] = True

    #   shown_board = board
    print_board(shown_board)

    return True

def main():
    '''
    Main function
    '''

    global board, shown_board, flags

    x = input().lower()

    os.system("cls")

    if x.startswith("f"):
        [_, x, y] = x.split(" ")
        shown_board = flag(shown_board, int(x) - 1, int(y) - 1)
        print_board(shown_board)

        won = True

        for i in shown_board:
            for v in i:
                if v == "O":
                    won = False

        if won:
            print("You Won!")
            exit()
        return

    if x.startswith("/"):
        if x == "/place":
            board = [["" for _ in range(dimensions[0])] for _ in range(dimensions[1])]
            shown_board = [["O" for _ in range(dimensions[0])] for _ in range(dimensions[1])]
            reserved = {}
            _reserved = {}

            placing = True

            while placing:

                os.system("cls")
                print_board(board)

                x = input().lower()

                if x == "done":
                    placing = False
                    for i in _reserved:
                        board[i[0]][i[1]] = ""
                    break
                elif x.startswith("r"):
                    continue # This has not been implemented yet

                    [_, x, y] = x.split(" ")

                    if (int(x), int(y)) in _reserved:
                        board[int(x) - 1][int(y) - 1] = ""
                        reserved.pop((int(x), int(y)))
                        _reserved.pop((int(x), int(y)))
                    else:
                        board[int(x) - 1][int(y) - 1] = "R"
                        reserved[(int(x), int(y))] = True
                        _reserved[(int(x), int(y))] = True
                    continue

                [x, y] = x.split()

                if board[int(x) - 1][int(y) - 1] == "M":
                    board[int(x) - 1][int(y) - 1] = ""
                else:
                    board[int(x) - 1][int(y) - 1] = "M"

            os.system("cls")
            print_board(shown_board)

            #while not first_click():
            #    pass

            board = generate_numbers(board)

            for i in reserved:
                shown_board[i[0]][i[1]] = board[i[0]][i[1]]

            os.system("cls")
            print_board(shown_board)
        
        return

    [x, y] = x.split(" ")

    [_board, success, state] = interact(shown_board, board, int(x) - 1, int(y) - 1)

    shown_board = _board
    print_board(shown_board)

    if not success:
        print("ERROR!")
    if state == "Lost":
        print("You Lost!")
        exit()
    if state == "Won":
        print("You Won!")
        exit()

if __name__ == "__main__":
    os.system("cls")
    print_board(shown_board)

    while not first_click():
        pass

    board = generate_board(board, args.mines)

    os.system("cls")

    print_board(shown_board)

    while True:
        main()

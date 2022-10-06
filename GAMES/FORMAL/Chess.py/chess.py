# Make a chess clone using pygame
import pygame
from numpy import flip, ndarray
from math import floor
from sys import exit

# Define some constants
BOARD = 1
PAWN = 2
KNIGHT = 4
BISHOP = 8
ROOK = 16
QUEEN = 32
KING = 64

BLACK = 128
WHITE = 256

# Images
IMAGES = {
    BOARD  | WHITE: pygame.image.load("images/white_board.png"),
    PAWN   | WHITE: pygame.image.load("images/wp.png"),
    KNIGHT | WHITE: pygame.image.load("images/wn.png"),
    BISHOP | WHITE: pygame.image.load("images/wb.png"),
    ROOK   | WHITE: pygame.image.load("images/wr.png"),
    QUEEN  | WHITE: pygame.image.load("images/wq.png"),
    KING   | WHITE: pygame.image.load("images/wk.png"),
    BOARD  | BLACK: pygame.image.load("images/black_board.png"),
    PAWN   | BLACK: pygame.image.load("images/bp.png"),
    KNIGHT | BLACK: pygame.image.load("images/bn.png"),
    BISHOP | BLACK: pygame.image.load("images/bb.png"),
    ROOK   | BLACK: pygame.image.load("images/br.png"),
    QUEEN  | BLACK: pygame.image.load("images/bq.png"),
    KING   | BLACK: pygame.image.load("images/bk.png"),
    "SELECTED BOARD": pygame.image.load("images/selected_board.png")
}

pygame.mixer.init()

SOUNDS = {
    "check": pygame.mixer.Sound("sounds/check.ogg"),
    "move": pygame.mixer.Sound("sounds/move.mp3"),
    "capture": pygame.mixer.Sound("sounds/capture.mp3"),
    "notify": pygame.mixer.Sound("sounds/notify.mp3"),
}

board = [[0 for _ in range(8)] for _ in range(8)]
turn = WHITE

selected = None
attacker = None

move_count = 0

flags = {
    "castling": {
        "white": [False, False],
        "black": [False, False]
    },
    "en_passant": None,
    "half_move": 0,
}

def load_board_from_fen(fen):
    """Load a board from a FEN string"""
    global board, turn, flags, move_count

    pieceTypeFromSymbol = {
        "p": PAWN,
        "n": KNIGHT,
        "b": BISHOP,
        "r": ROOK,
        "q": QUEEN,
        "k": KING
    }

    rank = 7
    file = 0

    fen = fen.split(" ")

    for i in fen[0]:
        if i == "/":
            file = 0
            rank -= 1
        elif i.isdigit():
            file += int(i)
        else:
            pieceColor = WHITE if i.isupper() else BLACK
            pieceType = pieceTypeFromSymbol[i.lower()]
            board[rank][file] = pieceType | pieceColor
            file += 1

    if fen[1] == "w":
        turn = WHITE
    else:
        turn = BLACK

    for i in fen[2]:
        if i == "K":
            flags["castling"]["white"][1] = True
        elif i == "Q":
            flags["castling"]["white"][0] = True
        elif i == "k":
            flags["castling"]["black"][1] = True
        elif i == "q":
            flags["castling"]["black"][0] = True

    flags["en_passant"] = fen[3]
    flags["half_move"] = int(fen[4])
   
    move_count = int(fen[5])

    board = ndarray.tolist(flip(board, 0))

def is_valid_fen(fen):
    """Check if a FEN string is valid"""
    fen = fen.split(" ")

    if len(fen) != 6:
        return False

    if fen[1] not in ["w", "b"]:
        return False

    if fen[2] not in ["KQkq", "Kkq", "Qkq", "kq", "KQ", "Kk", "Qk", "K", "Q"]:
        return False

    if not fen[4].isdigit():
        return False

    if not fen[5].isdigit():
        return False

    return True

def is_valid_move(x1, y1, x2, y2):
    """Check if a move is valid"""
    global board

    piece = board[x1][y1]
    pieceType = piece & ~(BLACK | WHITE)
    pieceColor = piece & (BLACK | WHITE)

    if pieceType == PAWN:
        if pieceColor == WHITE:
            if x2 == x1 - 1 and y2 == y1 + 1 and board[x2][y2] & BLACK == BLACK:
                return True
            elif x2 == x1 - 1 and y2 == y1 - 1 and board[x2][y2] & BLACK == BLACK:
                return True
            elif x2 == x1 - 2 and y2 == y1 and x1 == 1 and y1 == 6 and not flags["en_passant"] and board[x2][y2] == 0:
                return True
            elif x2 == x1 - 1 and y2 == y1 and board[x1 - 1][y1] == 0 and board[x2][y2] == 0:
                return True
            elif x2 == x1 - 1 and y2 == y1 and board[x1 - 1][y1] & BLACK == BLACK and board[x2][y2] == 0:
                return True
            elif x2 == x1 - 1 and y2 == y1 + 1 and board[x1 - 1][y1 + 1] & BLACK == BLACK:
                return True
            elif x2 == x1 - 1 and y2 == y1 - 1 and board[x1 - 1][y1 - 1] & BLACK == BLACK:
                return True
        else:
            if x2 == x1 + 1 and y2 == y1 + 1 and board[x2][y2] & WHITE == WHITE:
                return True
            elif x2 == x1 + 1 and y2 == y1 - 1 and board[x2][y2] & WHITE == WHITE:
                return True
            elif x2 == x1 + 2 and y2 == y1 and x1 == 6 and y1 == 1 and not flags["en_passant"] and board[x2][y2] == 0:
                return True
            elif x2 == x1 + 1 and y2 == y1 and board[x1 + 1][y1] == 0 and board[x2][y2] == 0:
                return True
            elif x2 == x1 + 1 and y2 == y1 and board[x1 + 1][y1] & WHITE == WHITE and board[x2][y2] == 0:
                return True
            elif x2 == x1 + 1 and y2 == y1 + 1 and board[x1 + 1][y1 + 1] & WHITE == WHITE:
                return True
            elif x2 == x1 + 1 and y2 == y1 - 1 and board[x1 + 1][y1 - 1] & WHITE == WHITE:
                return True
    elif pieceType == ROOK:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                if board[x1][i] != 0:
                    return False
            return True
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                if board[i][y1] != 0:
                    return False
            return True
        else:
            return False
    elif pieceType == KNIGHT:
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
            return True
        elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
            return True
        else:
            return False
    elif pieceType == BISHOP:
        if abs(x1 - x2) == abs(y1 - y2):
            for i in range(1, abs(x1 - x2)):
                if board[min(x1, x2) + i][min(y1, y2) + i] != 0:
                    return False
            return True
        else:
            return False
    elif pieceType == QUEEN:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                if board[x1][i] != 0:
                    return True
            return True
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                if board[i][y1] != 0:
                    return True
            return True
        elif abs(x1 - x2) == abs(y1 - y2):
            for i in range(1, abs(x1 - x2)):
                if board[min(x1, x2) + i][min(y1, y2) + i] != 0:
                    return True
            return True
        else:
            return False
    elif pieceType == KING:
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            return True
        else:
            return False
    else:
        return False

def is_in_check(color):
    """Check if a color is in check"""
    global board, attacker

    king_pos = None

    for i in range(8):
        for j in range(8):
            if board[i][j] & color == color and board[i][j] & KING == KING:
                king_pos = (i, j)
                break

    if king_pos is None:
        return False

    for i in range(8):
        for j in range(8):
            if board[i][j] & color != color:
                if is_valid_move(i, j, king_pos[0], king_pos[1]):
                    attacker = (i, j)
                    return True

    return False

def calc_legal_move(piece, x, y):
    """
    piece: the piece to move
    x: tuple(current x, new x)
    y: tuple(current y, new y)
    """
    global board, turn, flags, move_count

    if piece & PAWN:
        if is_in_check(turn):
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False

        thing = board[y[1]][x[1]]
        board[y[1]][x[1]] = piece
        board[y[0]][x[0]] = 0
        if is_in_check(turn):
            board[y[1]][x[1]] = thing
            board[y[0]][x[0]] = piece
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False
        board[y[1]][x[1]] = thing
        board[y[0]][x[0]] = piece

        if piece & WHITE:
            if x[1] == x[0] and y[1] == y[0] - 1 and board[y[1]][x[1]] == 0:
                if y[1] == 0:
                    board[y[1]][x[1]] = QUEEN | WHITE
                    board[y[0]][x[0]] = 0

                    pygame.mixer.Sound.play(SOUNDS["move"])

                    turn = BLACK

                    if is_in_check(BLACK):
                        pygame.mixer.Sound.play(SOUNDS["check"])

                    return False

                return True
            elif x[1] == x[0] and y[1] == y[0] - 2 and y[0] == 6 and flags["half_move"] == 0 and board[y[1]][x[1]] == 0:
                return True
            elif x[1] == x[0] + 1 and y[1] == y[0] - 1 and board[y[1]][x[1]] & BLACK:
                if board[y[1]][x[1]] != 0:
                    pygame.mixer.Sound.play(SOUNDS["capture"])
                    if board[y[1]][x[1]] & KING:
                        return "checkmate"
                if y[1] == 0:
                    board[y[1]][x[1]] = QUEEN | WHITE
                    board[y[0]][x[0]] = 0

                    pygame.mixer.Sound.play(SOUNDS["move"])

                    turn = BLACK

                    if is_in_check(BLACK):
                        pygame.mixer.Sound.play(SOUNDS["check"])

                    return False
                return True
            elif x[1] == x[0] - 1 and y[1] == y[0] - 1 and board[y[1]][x[1]] & BLACK:
                if board[y[1]][x[1]] != 0:
                    pygame.mixer.Sound.play(SOUNDS["capture"])
                    if board[y[1]][x[1]] & KING:
                        return "checkmate"
                if y[1] == 0:
                    board[y[1]][x[1]] = QUEEN | WHITE
                    board[y[0]][x[0]] = 0

                    pygame.mixer.Sound.play(SOUNDS["move"])

                    turn = BLACK

                    if is_in_check(BLACK):
                        pygame.mixer.Sound.play(SOUNDS["check"])

                    return False
                return True
            else:
                return False
        else:
            if x[1] == x[0] and y[1] == y[0] + 1:
                if y[1] == 7:
                    board[y[1]][x[1]] = QUEEN | BLACK
                    board[y[0]][x[0]] = 0

                    pygame.mixer.Sound.play(SOUNDS["move"])

                    turn = WHITE

                    if is_in_check(WHITE):
                        pygame.mixer.Sound.play(SOUNDS["check"])
                    return False
                return True
            elif x[1] == x[0] and y[1] == y[0] + 2 and y[0] == 1 and flags["half_move"] == 0:
                return True
            elif x[1] == x[0] + 1 and y[1] == y[0] + 1 and board[y[1]][x[1]] & WHITE:
                if board[y[1]][x[1]] != 0:
                    pygame.mixer.Sound.play(SOUNDS["capture"])
                    if board[y[1]][x[1]] & KING:
                        return "checkmate"
                if y[1] == 7:
                    board[y[1]][x[1]] = QUEEN | BLACK
                    board[y[0]][x[0]] = 0

                    pygame.mixer.Sound.play(SOUNDS["move"])

                    turn = WHITE

                    if is_in_check(WHITE):
                        pygame.mixer.Sound.play(SOUNDS["check"])
                    return False
                return True
            elif x[1] == x[0] - 1 and y[1] == y[0] + 1 and board[y[1]][x[1]] & WHITE:
                if board[y[1]][x[1]] != 0:
                    pygame.mixer.Sound.play(SOUNDS["capture"])
                    if board[y[1]][x[1]] & KING:
                        return "checkmate"
                if y[1] == 7:
                    board[y[1]][x[1]] = QUEEN | BLACK
                    board[y[0]][x[0]] = 0

                    pygame.mixer.Sound.play(SOUNDS["move"])

                    turn = WHITE

                    if is_in_check(WHITE):
                        pygame.mixer.Sound.play(SOUNDS["check"])
                    return False
                return True
            else:
                return False
    elif piece & KNIGHT:
        if is_in_check(turn):
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False

        thing = board[y[1]][x[1]]
        board[y[1]][x[1]] = piece
        board[y[0]][x[0]] = 0
        if is_in_check(turn):
            board[y[1]][x[1]] = thing
            board[y[0]][x[0]] = piece
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False
        board[y[1]][x[1]] = thing
        board[y[0]][x[0]] = piece

        if abs(x[0] - x[1]) == 2 and abs(y[0] - y[1]) == 1 or abs(x[0] - x[1]) == 1 and abs(y[0] - y[1]) == 2:
            if board[y[1]][x[1]] != 0:
                pygame.mixer.Sound.play(SOUNDS["capture"])
                if board[y[1]][x[1]] & KING:
                    return "checkmate"
            
            return True

        return False
    elif piece & BISHOP:
        if is_in_check(turn):
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False

        thing = board[y[1]][x[1]]
        board[y[1]][x[1]] = piece
        board[y[0]][x[0]] = 0
        if is_in_check(turn):
            board[y[1]][x[1]] = thing
            board[y[0]][x[0]] = piece
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False
        board[y[1]][x[1]] = thing
        board[y[0]][x[0]] = piece

        # Stop the move if the bishop is blocked
        if x[0] != x[1] and y[0] != y[1]:
            if x[0] > x[1]:
                x_inc = -1
            else:
                x_inc = 1

            if y[0] > y[1]:
                y_inc = -1
            else:
                y_inc = 1

            for i in range(1, abs(x[0] - x[1])):
                if board[y[0] + y_inc * i][x[0] + x_inc * i] != 0:
                    return False            

        if x[0] != x[1] and y[0] != y[1]:
            if abs(x[0] - x[1]) == abs(y[0] - y[1]):
                if board[y[1]][x[1]] != 0:
                    pygame.mixer.Sound.play(SOUNDS["capture"])
                    if board[y[1]][x[1]] & KING:
                        return "checkmate"
                return True
        return False
    elif piece & ROOK:
        if is_in_check(turn):
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False

        thing = board[y[1]][x[1]]
        board[y[1]][x[1]] = piece
        board[y[0]][x[0]] = 0
        if is_in_check(turn):
            board[y[1]][x[1]] = thing
            board[y[0]][x[0]] = piece
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False
        board[y[1]][x[1]] = thing
        board[y[0]][x[0]] = piece

        # Stop the move if the rook is blocked

        if x[0] == x[1]:
            if y[0] > y[1]:
                y_inc = -1
            else:
                y_inc = 1

            for i in range(1, abs(y[0] - y[1])):
                if board[y[0] + y_inc * i][x[0]] != 0:
                    return False
        elif y[0] == y[1]:
            if x[0] > x[1]:
                x_inc = -1
            else:
                x_inc = 1

            for i in range(1, abs(x[0] - x[1])):
                if board[y[0]][x[0] + x_inc * i] != 0:
                    return False

        if x[0] == x[1] or y[0] == y[1]:
            if board[y[1]][x[1]] != 0:
                pygame.mixer.Sound.play(SOUNDS["capture"])
                if board[y[1]][x[1]] & KING:
                    return "checkmate"
            return True
        return False
    elif piece & QUEEN:
        if is_in_check(turn):
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False

        thing = board[y[1]][x[1]]
        board[y[1]][x[1]] = piece
        board[y[0]][x[0]] = 0
        if is_in_check(turn):
            board[y[1]][x[1]] = thing
            board[y[0]][x[0]] = piece
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False
        board[y[1]][x[1]] = thing
        board[y[0]][x[0]] = piece

        # Stop the move if the queen is blocked
        if x[0] == x[1]:
            if y[0] > y[1]:
                y_inc = -1
            else:
                y_inc = 1

            for i in range(1, abs(y[0] - y[1])):
                if board[y[0] + y_inc * i][x[0]] != 0:
                    return False
        elif y[0] == y[1]:
            if x[0] > x[1]:
                x_inc = -1
            else:
                x_inc = 1

            for i in range(1, abs(x[0] - x[1])):
                if board[y[0]][x[0] + x_inc * i] != 0:
                    return False

        if x[0] != x[1] and y[0] != y[1]:
            if x[0] > x[1]:
                x_inc = -1
            else:
                x_inc = 1

            if y[0] > y[1]:
                y_inc = -1
            else:
                y_inc = 1

            for i in range(1, abs(x[0] - x[1])):
                if board[y[0] + y_inc * i][x[0] + x_inc * i] != 0:
                    return False

        if x[0] == x[1] or y[0] == y[1] or abs(x[0] - x[1]) == abs(y[0] - y[1]):
            if board[y[1]][x[1]] != 0:
                pygame.mixer.Sound.play(SOUNDS["capture"])
                if board[y[1]][x[1]] & KING:
                    return "checkmate"
            return True
        return False
    elif piece & KING:
        # Check if the new move will put the king in check
        thing = board[y[1]][x[1]]
        board[y[1]][x[1]] = piece
        board[y[0]][x[0]] = 0
        if is_in_check(turn):
            board[y[1]][x[1]] = thing
            board[y[0]][x[0]] = piece
            pygame.mixer.Sound.play(SOUNDS["check"])
            return False
        board[y[1]][x[1]] = thing
        board[y[0]][x[0]] = piece

        if abs(x[0] - x[1]) <= 1 and abs(y[0] - y[1]) <= 1:
            if board[y[1]][x[1]] != 0:
                pygame.mixer.Sound.play(SOUNDS["capture"])
                if board[y[1]][x[1]] & KING:
                    return "checkmate"
            return True

        return False

def is_in_checkmate(turn):
    # Find the king
    king_x, king_y = None, None

    for y in range(8):
        for x in range(8):
            if board[y][x] & KING and board[y][x] & turn:
                king_x = x
                king_y = y
                break

    if king_x is None:
        return True

    if king_y + 1 < 8 and king_x + 1 < 8:
        if board[king_y + 1][king_x + 1] & turn == 0:
            piece = board[king_y + 1][king_x + 1]
            board[king_y + 1][king_x + 1] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y + 1][king_x + 1] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y + 1][king_x + 1] = piece
            board[king_y][king_x] = KING | turn
    
    if king_y + 1 < 8 and king_x - 1 >= 0:
        if board[king_y + 1][king_x - 1] & turn == 0:
            piece = board[king_y + 1][king_x - 1]
            board[king_y + 1][king_x - 1] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y + 1][king_x - 1] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y + 1][king_x - 1] = piece
            board[king_y][king_x] = KING | turn

    if king_y - 1 >= 0 and king_x + 1 < 8:
        if board[king_y - 1][king_x + 1] & turn == 0:
            piece = board[king_y - 1][king_x + 1]
            board[king_y - 1][king_x + 1] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y - 1][king_x + 1] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y - 1][king_x + 1] = piece
            board[king_y][king_x] = KING | turn

    if king_y - 1 >= 0 and king_x - 1 >= 0:
        if board[king_y - 1][king_x - 1] & turn == 0:
            piece = board[king_y - 1][king_x - 1]
            board[king_y - 1][king_x - 1] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y - 1][king_x - 1] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y - 1][king_x - 1] = piece
            board[king_y][king_x] = KING | turn

    if king_y + 1 < 8:
        if board[king_y + 1][king_x] & turn == 0:
            piece = board[king_y + 1][king_x]
            board[king_y + 1][king_x] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y + 1][king_x] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y + 1][king_x] = piece
            board[king_y][king_x] = KING | turn

    if king_y - 1 >= 0:
        if board[king_y - 1][king_x] & turn == 0:
            piece = board[king_y - 1][king_x]
            board[king_y - 1][king_x] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y - 1][king_x] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y - 1][king_x] = piece
            board[king_y][king_x] = KING | turn

    if king_x + 1 < 8:
        if board[king_y][king_x + 1] & turn == 0:
            piece = board[king_y][king_x + 1]
            board[king_y][king_x + 1] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y][king_x + 1] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y][king_x + 1] = piece
            board[king_y][king_x] = KING | turn

    if king_x - 1 >= 0:
        if board[king_y][king_x - 1] & turn == 0:
            piece = board[king_y][king_x - 1]
            board[king_y][king_x - 1] = KING | turn
            board[king_y][king_x] = 0
            if not is_in_check(turn):
                board[king_y][king_x - 1] = piece
                board[king_y][king_x] = KING | turn
                return False
            board[king_y][king_x - 1] = piece
            board[king_y][king_x] = KING | turn

    if is_in_check(turn):
        return "checkmate"
    else:
        # Check if the player can move another piece
        for y in range(8):
            for x in range(8):
                if board[y][x] & turn:
                    for i in range(8):
                        for j in range(8):
                            if is_valid_move(x, y, i, j):
                                return False
        return "stalemate"



    

load_board_from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
#load_board_from_fen("7k/8/1P6/8/2K5/8/8/8 w KQkq - 0 1")

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (480, 480)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Chess")

# Loop until the user clicks the close button.
done = False

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    pygame.time.delay(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                board = [[0 for _ in range(8)] for _ in range(8)]
                load_board_from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
            if event.key == pygame.K_LSHIFT:
                
                fen = input("Enter FEN: ")

                if fen == "":
                    continue
                if is_valid_fen(fen):
                    board = [[0 for _ in range(8)] for _ in range(8)]
                    load_board_from_fen(fen)
                else:
                    print("Invalid FEN")
        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            x = floor(pos[0]) // 60
            y = floor(pos[1]) // 60

            pos = (y, x)

            piece = board[y][x]

            if pygame.mouse.get_pressed()[0]:
                if selected is None and piece != 0 and piece & turn != 0 or selected is not None and piece != 0 and piece & turn != 0:
                    selected = (pos, piece)

                elif selected is not None and piece & turn == 0:
                    result = calc_legal_move(selected[1], (selected[0][1], pos[1]), (selected[0][0], pos[0]))

                    if not result:
                        continue
                        
                    elif result == "checkmate":
                        pygame.mixer.Sound.play(SOUNDS["notify"])
                        print(f"Checkmate! {'White' if turn == WHITE else 'Black'} wins!")
                        done = True


                    pygame.mixer.Sound.play(SOUNDS["move"])
                        
                    board[y][x] = selected[1]
                    board[selected[0][0]][selected[0][1]] = 0
                    selected = None

                    turn = WHITE if turn == BLACK else BLACK

                    if is_in_check(turn):
                        pygame.mixer.Sound.play(SOUNDS["check"])

                    thing = is_in_checkmate(turn)

                    # Check for checkmate
                    if thing == "checkmate":
                        pygame.mixer.Sound.play(SOUNDS["notify"])
                        print(f"Checkmate! {'White' if turn == BLACK else 'Black'} wins!")
                        done = True
                    elif thing == "stalemate":
                        pygame.mixer.Sound.play(SOUNDS["notify"])
                        print("Stalemate!")
                        done = True
                    

    # Draw the pieces
    for file in range(8):
        for rank in range(8):
            pos = (rank * 60, file * 60)

            if selected is not None and selected[0] == (file, rank):
                screen.blit(IMAGES["SELECTED BOARD"], pos)
            else:
                if (file + rank) % 2 == 0:
                    screen.blit(IMAGES[BOARD | WHITE], pos)
                else:
                    screen.blit(IMAGES[BOARD | BLACK], pos)

            if board[file][rank] != 0:
                screen.blit(IMAGES[board[file][rank]], pos)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

while True:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()
            exit(0)

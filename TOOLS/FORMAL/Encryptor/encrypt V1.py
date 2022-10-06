import base64
import random
import string
import sys as sus

enc = [
    {"0": "Z", "1": "J", "2": "b", "3": "q", "4": "W", "5": "e", "6": "I", "7": "2", "8": "s", "9": "N", "a": "K", "b": "O", "c": "c", "d": "L", "e": "X", "f": "n", "g": "l", "h": "d", "i": "A", "j": "D", "k": "w", "l": "p", "m": "r", "n": "G", "o": "S", "p": "E", "q": "t", "r": "m", "s": "y", "t": "v", "u": "u", "v": "x", "w": "i", "y": "z", "x": "o", "z": "a", "A": "f", "B": "g", "C": "k", "D": "Q", "E": "R", "F": "h", "G": "j", "H": "P", "I": "B", "J": "H", "K": "F", "L": "C", "M": "_", "N": "V", "O": "T", "P": "Y", "Q": "U", "R": "5", "S": "3", "T": "6", "U": "1", "V": "4", "W": "7", "Y": "8", "X": "0", "Z": "=", "_": "M", "=": "9"},
    {'n': 'U', 'A': 'F', 'e': 'c', 't': 'X', 'z': 'R', 'D': 'T', '3': 'Q', 'P': 's', 'g': '_', 'V': 'f', '8': 'P', 'i': 'y', 's': '3', 'x': 'z', 'N': 'n', '0': 'I', 'w': '5', 'l': 'q', 'o': 'i', 'c': 'a', 'a': 'G', 'S': '1', 'h': 'm', 'C': 'k', 'J': '9', '1': 'h', 'b': 'A', 'I': 'E', 'G': 'J', 'f': 'j', 'm': 'S', 'W': 'Z', 'r': '4', '5': 'H', '4': 'C', 'q': '6', 'E': 'p', 'B': '=', 'Z': 'D', 'Q': 'Y', 'j': 'l', '=': 'N', 'd': 'x', '7': 'V', 'O': 'b', 'v': 'v', "k": "w", '_': 'M', 'y': '7', 'p': 'L', 'X': '0', 'u': 'K', 'H': 'u', 'U': 'B', 'K': 'o', '9': '8', 'L': '2', '2': 'r', 'Y': 'g', 'F': 'd', '6': 'O', 'M': 'e', 'R': 'W', 'T': 't'},
    {'o': 'u', 'R': 'b', 'I': '_', 'J': 'O', 'b': 'R', 'F': 'Z', "O": "Y", '_': 'N', 'G': 'l', 'N': 'v', '2': 'C', 'z': 'I', 'W': 'r', 'u': 'o', 'Q': '1', 'h': 'B', 'E': 'm', 'w': 'K', 'n': 'k', '5': 'D', 'c': '=', 'S': 't', 'g': '6', 'X': '2', 'x': '4', '6': 'L', 'j': 'n', 'Y': 'F', '9': 's', 'l': 'i', 'Z': '9', 'd': 'P', 'D': '0', '8': 'V', 'V': 'w', 'i': 'W', 'H': '7', 'L': 'Q', 'a': '5', 'U': 'E', '0': 'M', 'r': '8', 'A': 'U', 'q': 'p', '4': '3', 'f': 'd', "s": "f", 'y': 'q', 'C': 'e', "m": "G", '1': 'H', 'B': 'S', 'e': 'g', '3': 'c', 'M': 'J', 't': 'y', 'k': 'X', 'T': 'z', 'v': 'T', 'p': 'A', 'K': 'x', '7': 'a', '=': 'h', 'P': 'j'},
    {'s': '8', 'l': 'u', '=': 'I', 'R': 'H', 'u': 'S', 'a': 'U', 'c': 's', 'W': 'R', 'A': 'Z', 'M': 'l', 't': 'C', 'O': 'J', 'Q': 'T', 'U': 'F', 'S': '3', '7': 'P', 'I': '2', 'h': 'w', '5': 'e', 'z': 'y', '4': 'j', 'k': 'q', '_': '7', 'x': 'x', 'F': 'N', '2': '4', 'K': 'm', 'o': '9', 'Z': '0', 'G': '1', 'X': 'a', 'p': 'f', 'E': 'i', '9': 'g', 'Y': 'b', 'f': 'V', 'n': 'O', 'B': 't', 'H': '=', 'J': 'v', 'N': 'M', 'w': 'h', 'V': 'G', 'D': 'z', 'i': 'd', 'P': 'Q', 'v': 'B', 'd': '6', 'b': 'p', '1': 'k', 'q': 'X', '6': 'E', "C": "Y", 'g': 'n', 'T': 'W', '3': '5', '0': 'K', 'r': 'A', 'm': '_', '8': 'r', 'L': 'o', 'j': 'L', 'e': 'D', 'y': 'c'},
    {'P': '5', 'l': 'S', 'x': 'Z', 'b': 'B', 'H': 'i', '4': 'E', 'V': 'V', 'J': 'o', 'D': '7', 'Q': 'q', '_': '=', 'c': 'U', 'e': '_', 'i': 'T', 'B': 'C', 'n': 'n', 'u': 'f', '1': 'F', '2': 'y', 'h': 's', 'Y': '1', 'L': 'j', 'U': 'v', "E": "u", 'p': 'H', '0': 'R', 'G': 'a', 'q': 'A', '3': 'G', '8': 'p', 'O': 'I', 'v': 'X', 'F': 'c', 'X': 'r', 'K': '6', 'a': 'J', 'C': 'k', 'W': 'W', '=': 'z', 'S': 'P', 'k': '4', 'o': 'Y', 'j': 'Q', '9': 'N', 'I': 'b', 'r': 'm', 'R': 'h', '6': '8', 'f': 'M', 'Z': 'w', '7': 'L', 'y': '9', 'T': '3', 'm': 'g', '5': '0', 'g': 'O', 'w': '2', 'N': 'l', 'A': 'K', 's': 'x', 't': 'd', 'z': 'D', 'd': 'e', 'M': 't'},
    {'_': 'E', 'y': 'd', '0': 'Z', 'e': 'c', 'L': 'Q', '5': 'J', '7': 's', 'C': 'm', 'a': 'T', 'c': 'g', 'j': 'e', 'b': 'B', 'z': 'M', '=': 'Y', 'f': 'X', 'i': 'I', 'p': 'h', 'V': '_', 'P': 'w', 'W': 'K', 'k': 't', 'B': '0', 'J': '9', '6': '3', 'n': 'P', 'O': 'q', 's': 'z', 'T': 'y', 'h': 'S', 'H': '=', 'R': '7', 'g': 'C', 'I': '2', 'q': 'L', 'w': 'j', '3': 'n', 'm': 'N', 'G': 'D', 'N': 'v', '2': '1', 'D': 'x', 'M': 'r', '1': 'p', '4': 'l', 'v': 'k', 'd': 'b', 'x': '5', 'r': 'V', "U": "R", 'Y': 'i', 'u': '8', '8': 'U', 't': 'O', 'K': 'F', '9': 'G', 'F': 'H', 'l': 'a', 'X': 'o', 'o': '6', 'Z': 'W', 'Q': '4', 'A': 'f', 'E': 'A', 'S': 'u'}
]

EDIT_FILE = False
VERBOSE = False
ENC_VALUE = 0

def increment_enc():
    global ENC_VALUE

    ENC_VALUE += 1
    if ENC_VALUE >= len(enc):
        ENC_VALUE = 0

def decrement_enc():
    global ENC_VALUE

    ENC_VALUE -= 1
    if ENC_VALUE < 0:
        ENC_VALUE = len(enc) - 1

def encode(line):
    global ENC_VALUE

    fin = ""

    for l in line:
        if l in f"{string.ascii_letters}{string.digits}_=":
            fin += enc[ENC_VALUE][l]
        else:
            fin += l

    increment_enc()

    return fin


def decode(line):
    global ENC_VALUE

    fin = ""

    decrement_enc()

    for l in line:
        if l in f"{string.ascii_letters}{string.digits}_=":
            fin += list(enc[ENC_VALUE].keys())[list(enc[ENC_VALUE].values()).index(l)]
        else:
            fin += l

    return fin


def encrypt(file):
    '''
    docstring
    '''

    try:
        with open(file, "r+") as f:

            res = ""

            for line in f.readlines():

                decrement_enc()

                if VERBOSE:
                    print(f"VERBOSE: Start - {line}\n")

                line = encode(line)

                if VERBOSE:
                    print(f"VERBOSE: Encoded - {line}")

                line = encode(line)

                if VERBOSE:
                    print(f"VERBOSE: Encoded - {line}")

                line = encode(line)

                if VERBOSE:
                    print(f"VERBOSE: Encoded - {line}")

                line = base64.b64encode(line.encode("utf-8"))[::-1]

                if VERBOSE:
                    print(f"VERBOSE: b64 encode & rev - {line.decode('utf-8')}")

                line = base64.b64encode(line).decode("utf-8")[::-1]

                if VERBOSE:
                    print(f"VERBOSE: b64 encode & rev - {line}\n")

                len_line = len(line)

                line += base64.b64encode(line.encode('utf-8')[::-1]).decode('utf-8')

                if VERBOSE:
                    print(f"VERBOSE: Added garbage values - {line}\n")

                _line = ""

                index = 0
                for chr in line:
                    rnd = random.choice(string.ascii_letters)
                    _line += f"{chr}{rnd}"
                    if VERBOSE:
                        print(f"VERBOSE: Added garbage value at {index} - {rnd}")
                    index += 2

                line = f"{len(str(len_line))}_{len_line}{_line}\n"

                if VERBOSE:
                    print(f"\nVERBOSE: Added info - {line}")

                line = encode(line)

                if VERBOSE:
                    print(f"VERBOSE: Encoded - {line}\n")

                line = encode(line)

                if VERBOSE:
                    print(f"VERBOSE: Encoded - {line}")

                line = encode(line)

                if VERBOSE:
                    print(f"VERBOSE: Encoded - {line}")
                    print(f"VERBOSE: Finished! - {line}\n")

                res += line

            if EDIT_FILE:
                f.truncate(0)
                f.seek(0)
                f.write(res)
                print(f"`{file}` has been encrypted.")
            else:
                print(f"\nRESULT:\n{res}")
    except FileNotFoundError:
        input(f"ERROR: `{file}` does not exist!\n")
        sus.exit(1)


def decrypt(file):
    '''
    docstring
    '''

    try:
        with open(file, "r+") as f:

            res = ""

            for line in f.readlines():

                decrement_enc()

                if VERBOSE:
                    print(f"VERBOSE: Start - {line}")

                line = decode(line)

                if VERBOSE:
                    print(f"VERBOSE: Decoded - {line}")

                line = decode(line)

                if VERBOSE:
                    print(f"VERBOSE: Decoded - {line}")

                line = decode(line)

                if VERBOSE:
                    print(f"VERBOSE: Decoded - {line}")

                try:
                    len_of_len = int(line.split("_")[0])
                except ValueError:
                    input("ERROR: Invalid format!\n")
                    sus.exit(1)

                len_of_encoded = int(line[2:2 + len_of_len])

                line = line[2 + len_of_len:]

                if VERBOSE:
                    print(f"VERBOSE: Removed now useless details - {line}")

                line = line[:len_of_encoded * 2]

                if VERBOSE:
                    print(f"VERBOSE: Remove garbage values - {line}\n")

                line = line[::2]

                if VERBOSE:
                    print(f"VERBOSE: Done - {line}")

                line = base64.b64decode(line[::-1]).decode('utf-8')

                if VERBOSE:
                    print(f"VERBOSE: rev & b64 decode - {line}")

                line = base64.b64decode(line[::-1]).decode("utf-8")

                if VERBOSE:
                    print(f"VERBOSE: rev & b64 decode - {line}")

                line = decode(line)

                if VERBOSE:
                    print(f"VERBOSE: Decoded - {line}")

                line = decode(line)

                if VERBOSE:
                    print(f"VERBOSE: Decoded - {line}")

                line = decode(line)

                if VERBOSE:
                    print(f"VERBOSE: Decoded - {line}")
                    print(f"VERBOSE: Finished! - {line}\n")

                res += line

            if EDIT_FILE:
                f.truncate(0)
                f.seek(0)
                f.write(res)
                print(f"`{file}` has been decrypted.")
            else:
                print(f"RESULT:\n{res}")

    except FileNotFoundError:
        input(f"ERROR: `{file}` does not exist!\n")
        sus.exit(1)


if __name__ == "__main__":

    argv = sus.argv

    if len(argv) <= 1:
        e_or_d = input("Do you want to encrypt or decrypt a file?\n").lower()

        VERBOSE = True if input(
            "Do you want to enable verbose mode?\n(When verbose mode is enabled you can see everything that happens. Keep in mind this will clog up your console.)\n[Y / N]\n").lower().startswith(
            "y") else False
        EDIT_FILE = True if input(
            "Do you want to automatically edit the file to be encrypted or do you want the result to be printed to the console.\n[Y: edit / N: print]\n").lower().startswith(
            "y") else False

        if e_or_d.startswith("e"):
            encrypt(input("Enter a file you want to encrypt.\nExamples:\n    foo.txt\n    passwords/google.txt\n\n"))
        elif e_or_d.startswith("d"):
            decrypt(input(
                "Enter a file you want to decrypt.\nExamples:\n    foo_encrypted.txt\n    passwords/google_encrypted.txt\n\n"))
        else:
            input("ERROR: Please type `encrypt` or `decrypt`.")
            sus.exit(1)

    else:
        encryption = None

        file = argv[len(argv) - 1]

        for i in range(len(argv)):
            if not VERBOSE:
                VERBOSE = argv[i] == "-v" or argv[i] == "--verbose"
            if not EDIT_FILE:
                EDIT_FILE = argv[i] == "-c" or argv[i] == "--change"
            if argv[i] == "-e" or argv[i] == "--encrypt":
                if encryption is None:
                    encryption = True
            elif argv[i] == "-d" or argv[i] == "--decrypt":
                if encryption is None:
                    encryption = False
            elif not argv[i].startswith("-"):
                file = argv[i]

        if encryption is not None:
            if encryption:
                encrypt(file)
            else:
                decrypt(file)
        else:
            print("Usage:\n\npy encrypt.py (-d | -e) [-v] [-c] (File Name)\n-e: Encrypt\n-d: Decrypt\n-v: Verbose\n-c: Change file automatically")

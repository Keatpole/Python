import FILE_ENC as enc
import sys, os

def clear():
    if sys.platform == "win32": os.system("cls")
    else: os.system("clear")

def start():
    clear()
    fort = input("Do you want to input a file or paste in text?\nInput (F)ile / Paste in (T)ext\n")
    if fort.lower() == "f" or fort.lower == "file" or fort.lower() == "input file": file()
    elif fort.lower() == "t" or fort.lower == "text" or fort.lower() == "paste in text": text()
    else: start()
    
def file():
    clear()
    eord = input("Do you want to encrypt or decrypt a file?\n(E)ncrypt / (D)ecrypt\n")

    if eord.lower() == "e" or eord.lower() == "encrypt": fe()
    elif eord.lower() == "d" or eord.lower() == "decrypt": fd()
    else: start()

def text():
    clear()
    eord = input("Do you want to encrypt or decrypt the text?\n(E)ncrypt / (D)ecrypt\n")

    if eord.lower() == "e" or eord.lower() == "encrypt": te()
    elif eord.lower() == "d" or eord.lower() == "decrypt": td()
    else: start()

def fe():
    clear()
    reqf = input("What file do you want to encrypt? ")
    clear()
    with open(reqf, "r") as f:
        print(enc.encrypt(f.read()))

def fd():
    clear()
    reqf = input("What file do you want to decrypt? ")
    clear()
    with open(reqf, "r") as f:
        print(enc.decrypt(f.read()))

def te():
    clear()
    reqt = input("What text do you want to encrypt?\n\n").replace("§*","\\n")
    clear()
    print(enc.encrypt(reqt))

def td():
    clear()
    reqt = input("What text do you want to decrypt?\n\n").replace("\\n", "\n")
    clear()
    print(enc.decrypt(reqt))

start()
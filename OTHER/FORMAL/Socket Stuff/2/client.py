import socket as s

socket = s.socket()
port = 42069

socket.connect(("DESKTOP-LFHNNJ0", port))
print("Connected to @DESKTOP-LFHNNJ0")


def handleArgs(cmdf):
    cmdf = cmdf.split(" ")
    del cmdf[0]
    return cmdf


def command(cmdf, value):
    if cmdf.lower().startswith(value, 0, len(value)):
        return True
    else:
        return False

def send(value):
    socket.send(value.encode())


while True:
    cmd = socket.recv(1024).decode()

    if command(cmd, "msg"):
        args = handleArgs(cmd)
        print(" ".join(args))
        send(f"Sent \"{' '.join(args)}\" to the client")
    elif command(cmd, "listenclient"):
        msg = input("You can now say one sentence to the server: ")
        send(msg)
        print(f"You sent \"{msg}\" to the server")
    else:
        send("Could not find command")


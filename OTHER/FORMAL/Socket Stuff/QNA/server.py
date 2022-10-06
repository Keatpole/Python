import socket as s
import os

socket = s.socket(s.AF_INET, s.SOCK_STREAM)

options = []
running = False
ip = None
conn = None
addr = None

try:
    with open("IPV4.txt", "r") as i:
        ip = i.read()
        socket.bind((ip, 42069))
except:
    input("Put your local ipv4 address in \"IPV4.txt\"\n")
    exit()

def handleArgs(cmdf):
    cmdf = cmdf.split(" ")
    del cmdf[0]
    return cmdf

def command(cmdf, values):
    returning = False

    for value in values:
        if cmdf.lower().startswith("/" + value):
            returning = True

    return returning

def question(cmd, f):

    options = []
    msg = " ".join(handleArgs(cmd))
    print("Write \"done\" to complete or write \"return\" to go back\n")
    c = True

    while True:
        option = input("Add an option: ")

        if option.lower() == "done":
            break

        if option.lower() == "return":
            c=False
            break

        options.append(option)

    if c:

        print(f"Sent the question to the client")
        conn.send(f"options {' '.join(options)}".encode())

        if f:
            conn.send(f"fq {msg}".encode())
        else:
            conn.send(f"question {msg}".encode())

    while c:

        msg = conn.recv(1024).decode()
        test = False

        if not msg:
            print(f"WARNING: The client's code may have been edited. The client did not respond.")

        for o in options:
            if msg.lower() == o.lower():
                test = True
                print(f"The client answered: \"{msg}\"")
                conn.send("1".encode())
                c = False

        if not test:
            conn.send("0".encode())

def start():
    global conn, addr, running

    os.system("cls")

    print(f"\nServer is running at {ip}")
    print(f"\nWaiting for a connection...")

    socket.listen(1)
    conn, addr = socket.accept()

    print(f"\n{addr[0]} has successfully connected to the server.\n")

    running = True

    with open("bans.txt", "r") as f:
        for v in f.readlines():
            if v == addr[0]:
                conn.send("ban".encode())
                conn.close()
                start()
                running = False

    while running:

        cmd = input("\nCommand: ")

        os.system("cls")

        if command(cmd, ["cmds", "commands", "help"]):
            print(",\n".join(["cmds / commands / help", "ask / q / question", "fask / fq / fquestion", "say / tell / msg", "fsay / ftell / fmsg", "cls / clear", "kill / stop / close / end", "talk / listen / lc / l / speech", "ban"]))
        
        elif command(cmd, ["q", "question", "ask"]):
            question(cmd, False)
        
        elif command(cmd, ["fq", "fquestion", "fask"]):
            question(cmd, True)
        
        elif command(cmd, ["fsay", "ftell", "fmsg"]):
            msg = " ".join(handleArgs(cmd))
            conn.send(f"fsay {msg}".encode())
            print(f"Sent:\"{msg}\" to the client")

        elif command(cmd, ["cls", "clear"]):
            conn.send(f"cls".encode())
            print(f"Clearing the client's screen")

        elif command(cmd, ["kill", "stop", "close", "end"]):
            conn.send("kill".encode())
            running = False
            conn.close()
            start()

        elif command(cmd, ["ban"]):
            conn.send("ban".encode())
            running = False
            with open("bans.txt", "a") as f:
                f.write(addr[0])

            conn.close()
            start()

        elif command(cmd, ["listen", "lc", "l", "speech", "talk"]):
            conn.send("talk".encode())
            print(f"Waiting for the client to speak\n")
            msg = conn.recv(1024).decode()
            print(f"The client said:\"{msg}\"")

        elif cmd.startswith("/"):
            print(f"Could not find command")

        else:
            conn.send(f"say {cmd}".encode())
            print(f"Sent:\"{cmd}\" to the client")

start()
import socket as s

socket = s.socket()
port = 42069

cmds = ["cmds", "msg", "listenclient"]

socket.bind((s.gethostname(), port))

print(f"\nServer is running at: @{s.gethostname()}")
print(f"\nWaiting for a connection...")

socket.listen(1)
conn, addr = socket.accept();

print(f"{addr} has successfully connected to the server.")

def command(cmdf, values):
    returning = False
    for value in values:
        if cmdf.lower().startswith(value, 0, len(value)):
            returning = True
    return returning

while True:
    cmd = input("Command: ")

    if command(cmd, ["cmds", "commands", "help"]):
        print(", ".join(cmds))
    elif command(cmd, ["listenclient", "lc", "listen", "lcs"]):
        conn.send("listenclient".encode())
        msg = conn.recv(1024).decode()
        print(f"The client said: \"{msg}\"")
    else:
        conn.send(cmd.encode())
        callback = conn.recv(1024).decode()
        print(f"Command returned: {callback}")
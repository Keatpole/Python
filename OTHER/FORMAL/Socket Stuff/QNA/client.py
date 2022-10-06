import socket as s;import sys,time,os;socket = s.socket();options = []
try:socket.connect((input("Put in a valid IPV4 Address here: "), 42069))
except:input("Put in a valid IPV4 address\n");exit()
def handleArgs(cmdf):cmdf = cmdf.split(" ");del cmdf[0];return cmdf
def slowText(string):
    for c in string:sys.stdout.write(c);sys.stdout.flush();time.sleep(0.05)
def command(cmdf, value):
    if cmdf.lower().startswith(value):return True
def send(value):socket.send(value.encode())
def question(cmd,st):
    if st:slowText(" ".join(handleArgs(cmd))+"\n");slowText("("+" / ".join(options)+")\n")
    else:print(" ".join(handleArgs(cmd)));print("("+" / ".join(options)+")")
    send(input())
    if socket.recv(1024).decode() == "0":print("\nIncorrect option!\n");question(cmd, False)
os.system("cls");slowText("Please wait for the test to begin...\n")
while True:
    cmd = socket.recv(1024).decode();os.system("cls")
    if command(cmd, "say"):slowText(" ".join(handleArgs(cmd))+"\n")
    elif command(cmd, "fsay"):print(" ".join(handleArgs(cmd))+"\n")
    elif command(cmd, "cls"):os.system("cls")
    elif command(cmd, "question"):question(cmd, True)
    elif command(cmd, "fq"):question(cmd, False)
    elif command(cmd, "options"):options = handleArgs(cmd)
    elif command(cmd, "kill"):print("The test has ended...");exit()
    elif command(cmd, "ban"):print("You have been banned.");exit()
    elif command(cmd, "talk"):send(input("You can now talk: "))
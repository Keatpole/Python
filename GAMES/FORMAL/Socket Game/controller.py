import socket
import threading
import sys

HOST = "192.168.10.138"
PORT = 26556

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

def recv_msg():
    while True:
        try:
            data = s.recv(1024)
            if not data:
                continue
            print(data.decode("utf-8"))
        except:
            pass

# Create a thread to receive messages
t = threading.Thread(target=recv_msg)
t.daemon = True
t.start()

def send_msg(msg):
    s.send(("G678hjasd/hkj!342Huu78+132#/%&das | " + msg).encode("utf-8"))

while True:
    send_msg(input(">> "))
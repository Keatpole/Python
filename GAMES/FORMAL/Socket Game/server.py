# Create a socket server
import socket
import threading

HOST = "192.168.10.138"
PORT = 26556

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

def recv_msg(conn1, conn):
    while True:
        #try:
        data = conn.recv(1024).decode()

        controller_key = "G678hjasd/hkj!342Huu78+132#/%&das | "
        if data.startswith(controller_key):
            data = data.split(controller_key)[1]

            if data == "kill":
                send_msg(conn1, "die")

        print(data)
        #except:
        #    print("dhusia")
        #    pass

def send_msg(sock, msg):
    try:
        sock.send(msg.encode("utf-8"))
    except:
        return False


s.listen(5)
conn, addr = s.accept()

print("Connected by", addr)
send_msg(conn, "Welcome to the server!")
print("Waiting for controller...")

s.listen(5)
conn2, addr2 = s.accept()

print("Connected by", addr2)
send_msg(conn2, "Welcome to the server!")

t = threading.Thread(target=recv_msg, args=(conn,conn))
#t.daemon = True
t.start()
t = threading.Thread(target=recv_msg, args=(conn,conn2))
#t.daemon = True
t.start()
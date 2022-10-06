# Create a platforming game using pygame and use sockets
import pygame
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
            data = s.recv(1024).decode("utf-8")
            if not data:
                continue
            print(data)
            
            if data == "die":
                player.x = 0
                player.y = 0

        except:
            pass

# Create a thread to receive messages
t = threading.Thread(target=recv_msg)
t.daemon = True
t.start()

def send_msg(msg):
    s.send(msg.encode("utf-8"))


sprites = {
    "player": pygame.image.load("sprites/player.png"),
    "enemy": pygame.image.load("sprites/enemy.png"),
    "platform01": pygame.image.load("sprites/platform01.png")
}

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((480, 480))

# Main loop
running = True

player = screen.blit(sprites["player"], (0, 0))




while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            dir = 0

            # Send the key pressed
            if event.key == pygame.K_UP:
                dir = 1
            elif event.key == pygame.K_DOWN:
                dir = 2
            elif event.key == pygame.K_LEFT:
                dir = 3
            elif event.key == pygame.K_RIGHT:
                dir = 4
        else:
            dir = 0

    # Move the player
    if dir == 1:
        player.move_ip(0, -1)
    elif dir == 2:
        player.move_ip(0, 1)
    elif dir == 3:
        player.move_ip(-1, 0)
    elif dir == 4:
        player.move_ip(1, 0)
    else:
        continue

    send_msg(f"{dir} | {player.x} {player.y}")

    # Draw the screen
    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(sprites["player"], (player.x, player.y))

    # Update the screen
    pygame.display.flip()

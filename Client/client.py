import socket
import pygame
import sys
from player import Player
from functions import drawwindow
import pickle
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
SERVER = "192.168.68.132"
ADDRESS = (SERVER, PORT)

# sending server stuff
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(message):
    encodedmessage = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(encodedmessage)

# Pygame window setup


pygame.init()
windowsize = 800, 800
pygame.display.set_caption("MultiplayerGame")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(windowsize)
refreshrate = 60


# game variables
player = Player("P1", 400, 400, 80, 80)
while 1:
    # event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Shutting down game")
            client.close()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Shutting down game")
                client.close()
                sys.exit()
    drawwindow(screen, player)
    player.handlemovement()

    # screen update
    clock.tick(refreshrate)
    pygame.display.update()

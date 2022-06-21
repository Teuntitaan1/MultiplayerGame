# import statements
import socket
import pygame
import sys
from player import Player
from functions import drawwindow
import pickle

# pygame initializer
pygame.init()


# server variables
HEADER = 4096
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
def sendplayer(player):
    playerinbytes = pickle.dumps(player)
    message_length = len(playerinbytes)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(playerinbytes)

def recieveplayerlist():


    message_length = client.recv(HEADER).decode(FORMAT)
    if message_length:
        message_length = int(message_length)
        print(message_length)
        data = b""
        while True:
            packet = client.recv(message_length)
            data += packet
            if len(data) == message_length:
                break
        playerlist = pickle.loads(data)
        return playerlist

# Pygame window setup
windowsize = 800, 800
pygame.display.set_caption("MultiplayerGame")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(windowsize)
getTicksLastFrame = 0
# game variables
player = Player(str(input("What do you want your name to be?")), 400, 400, 80, 80)
Running = True
refreshrate = 60

while Running:
    # event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Shutting down game")
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Shutting down game")
                Running = False
    drawwindow(screen)



    player.handlemovement()
    playerinfo = {
        "playername": player.name,
        "x": player.x,
        "y": player.y,
        "width": player.width,
        "height": player.height,
        "color": player.color
    }
    sendplayer(playerinfo)
    playerlist = recieveplayerlist()
    for i in playerlist:
        rect = pygame.Rect([i["x"], i["y"]], [i["width"], i["height"]])
        pygame.draw.rect(screen, i["color"], rect)

    # screen update
    clock.tick(refreshrate)
    pygame.display.update()

# noinspection PyUnreachableCode
pygame.quit()
send("!DISCONNECT")
sys.exit()
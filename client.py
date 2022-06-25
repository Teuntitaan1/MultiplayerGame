# import statements
import pygame
import sys
from player import Player
from functions import drawwindow
from network import Network

# pygame initializer
pygame.init()


# server variables
PORT = int(input("What is the port of the server?"))
FORMAT = "utf-8"
SERVER = input("What is the ip of the server?")
ADDRESS = (SERVER, PORT)

# sending server stuff
network = Network()
def main(Player):
    # game variables
    player = Player
    Running = True
    refreshrate = 60

    while Running:
        # event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    Running = False
        drawwindow(screen)
        player.handlemovement()
        playerlist = network.send(player)
        for i in playerlist:
            i.draw(screen)
            name = font.render(i.name, True, (0, 0, 0))
            screen.blit(name, (i.x, i.y - 25))
            health = font.render(str(i.health), True, i.handlehealthcolor())
            screen.blit(health, (i.x, i.y - 50))


        # screen update
        clock.tick(refreshrate)
        pygame.display.update()

# Windowsize for the player
windowsize = 800, 800
# player init
player = Player(str(input("What do you want your name to be?")), 400, 400, 80, 80, windowsize[0], windowsize[1])
# pygame setup
pygame.display.set_caption("MultiplayerGame")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(windowsize)
font = pygame.font.SysFont("Vera", 40)

# main functiom
main(player)
# triggers when main ends
print("Shutting down game")
pygame.quit()
sys.exit()
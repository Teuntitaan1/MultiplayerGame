# import statements
import pygame
import sys
from player import Player
from functions import drawwindow
from network import Network

# pygame initializer
pygame.init()


# server variables
PORT = 5050
FORMAT = "utf-8"
SERVER = "192.168.68.132"
ADDRESS = (SERVER, PORT)

# sending server stuff
network = Network()
# Pygame window setup
windowsize = 800, 800
pygame.display.set_caption("MultiplayerGame")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(windowsize)
font = pygame.font.SysFont("Vera", 40)

def main():
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
        playerlist = network.send(player)
        for i in playerlist:
            i.draw(screen)
            name = font.render(i.name, True, (0, 0, 0))
            screen.blit(name, (i.x, i.y - i.height / 2))


        # screen update
        clock.tick(refreshrate)
        pygame.display.update()


main()
pygame.quit()
sys.exit()
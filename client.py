# import statements
import random

import pygame
import sys
from player import Player
from network import Network
from clientstates import maingame, mainmenu
# pygame initializer
pygame.init()

# Windowsize for the player
width, height = 800, 800
# player init
# pygame setup
pygame.display.set_caption(f"MultiplayerGame: Main menu")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Vera", 40)

# after the main menu ends(when the join button is pressed) it collects the port, server and name and passes them on to the rest of the progra
PORT, SERVER, NAME = mainmenu(clock, screen, font)
# player setup after the main menu is initialized
player = Player(NAME, random.randint(0, width-80), random.randint(0, height-80), 80, 80, width, height)
# connects to the server
network = Network(SERVER, PORT)

# changes the screen caption
pygame.display.set_caption(f"MultiplayerGame: {NAME}")
# switch the scene
maingame(player, screen, font, network, clock)
# triggers when main ends
print("Shutting down game")
pygame.quit()
sys.exit()

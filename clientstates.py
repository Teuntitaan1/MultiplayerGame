import random

import pygame
from functions import drawwindow
from Button import button
from TextInput import InputBox
def maingame(player, screen, font, network, clock):
    # game variables
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
        entitylist = network.send(player)
        for i in entitylist:
            i.draw(screen)
            name = font.render(i.name, True, (0, 0, 0))
            screen.blit(name, (i.x, i.y - 25))
            health = font.render(str(i.health), True, i.handlehealthcolor())
            screen.blit(health, (i.x, i.y - 50))

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()

def mainmenu(clock, screen, font):
    # game variables
    Running = True
    refreshrate = 60
    nameinput = InputBox(330, 100, 140, 50, font, "Enter your name")
    portinput = InputBox(330, 150, 140, 50, font, "Enter the server's port")
    ipinput = InputBox(330, 200, 140, 50, font, "Enter the server's ip address")
    buttoncolor = (random.randint(0,255), random.randint(0,255), (random.randint(0,255)))
    joinbutton = button(buttoncolor, 400, 600, 80, 40, "Join")
    inputboxlist = [portinput, ipinput, nameinput]

    while Running:
        # event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            # updates the text in a textinput
            for i in inputboxlist:
                i.handle_event(event)
        # clears the window
        drawwindow(screen)
        joinbutton.draw(screen, 10)
        # checks if the mouse and the button collide
        if joinbutton.ismouseover(pygame.mouse.get_pos()):
            # checks if the left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                # returns all the values neccesary for joining the server
                return int(portinput.text), str(ipinput.text), str(nameinput.text)
        # update and draws the inputs
        for i in inputboxlist:
            i.update()
            i.draw(screen)

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
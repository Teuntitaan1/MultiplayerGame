import random

import pygame


# player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, width, height, screenwidth, screenheight):

        super().__init__()
        # kind of useless right now
        self.name = name
        # color
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        # x and y
        self.x = x
        self.y = y
        # width and height variables
        self.width = width
        self.height = height
        # movementspeed
        self.movementspeed = 5
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        self.health = 150
        self.healthbegin = 150
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        # type
        self.type = "Player"


    def handlemovement(self):

        key = pygame.key.get_pressed()

        # movement script with screen border checking
        if key[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.movementspeed
        elif key[pygame.K_RIGHT]:
            if self.x < self.screenwidth - self.width:
                self.x += self.movementspeed
        elif key[pygame.K_UP]:
            if self.y > 0:
                self.y -= self.movementspeed
        elif key[pygame.K_DOWN]:
            if self.y < self.screenwidth - self.height:
                self.y += self.movementspeed

        # DEBUGGING
        # health changer

        if key[pygame.K_e]:
            if self.health < 150:
                self.health += 1
        elif key[pygame.K_q]:
            if self.health > 1:
                self.health -= 1

        # size changer

        if key[pygame.K_w]:
            if self.height > 1:
                self.height -= 1
        elif key[pygame.K_s]:
            if self.height < 200:
                self.height += 1
        if key[pygame.K_a]:
            if self.width > 1:
                self.width -= 1
        elif key[pygame.K_d]:
            if self.width < 200:
                self.width += 1


        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    # simple gradiant producer from green to red to indicate how close the player is to dying
    def handlehealthcolor(self):
        return self.healthbegin - self.health, 0 + self.health, 0

# simple enemy
# player sprite
class Simplefollowenemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, width, height, screenwidth, screenheight):

        super().__init__()
        # kind of useless right now
        self.name = name
        # color
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        # x and y
        self.x = x
        self.y = y
        # width and height variables
        self.width = width
        self.height = height
        # movementspeed
        self.movementspeed = 5
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        self.health = 150
        self.healthbegin = 150
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        # type
        self.type = "Simplefollowenemy"


    def handlemovement(self):
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    # simple gradiant producer from green to red to indicate how close the enemy is to dying
    def handlehealthcolor(self):
        return self.healthbegin - self.health, 0 + self.health, 0


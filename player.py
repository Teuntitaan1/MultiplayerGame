import random

import pygame


# player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, width, height):

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


    def handlemovement(self):

        key = pygame.key.get_pressed()

        # movement script
        if key[pygame.K_LEFT]:
            self.x -= self.movementspeed
        elif key[pygame.K_RIGHT]:
            self.x += self.movementspeed
        elif key[pygame.K_UP]:
            self.y -= self.movementspeed
        elif key[pygame.K_DOWN]:
            self.y += self.movementspeed
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)



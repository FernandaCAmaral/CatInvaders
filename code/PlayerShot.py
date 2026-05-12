import pygame

from code.Entity import Entity

class PlayerShot(Entity):

    def __init__(self, name , position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += self.speed
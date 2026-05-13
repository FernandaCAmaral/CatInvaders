import pygame

from code.Entity import Entity

class PlayerShot(Entity):

    def __init__(self, name , position):
        super().__init__(name, position)
        self.speed = 6

        if name == 'PlayerShot':
            self.surface = pygame.transform.scale(self.surface, (30, 20))
            self.rect = self.surface.get_rect(center=position)

    def move(self):
        self.rect.x += self.speed
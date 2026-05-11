from abc import ABC, abstractmethod
import pygame.image

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Carrega a imagem
        self.surface = pygame.image.load('./assets/' + name + '.png')
        self.rect = self.surface.get_rect(topleft = position)
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
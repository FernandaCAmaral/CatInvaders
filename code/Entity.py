from abc import ABC, abstractmethod
import pygame.image

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Carrega a imagem
        full_image = pygame.image.load('./assets/' + name + '.png')
        # Redimensiona a imagem para caber na janela
        window_size = pygame.display.get_surface().get_size()
        self.surface = pygame.transform.scale(full_image, window_size)

        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, x, y):
        pass
import pygame
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name ,position):
        super().__init__(name, position)
        print(f"Camada: {self.name} | Tamanho do Rect: {self.rect.size}")

    def move(self, x, y):
        pass
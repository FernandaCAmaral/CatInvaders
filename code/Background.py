import pygame
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name ,position):
        super().__init__(name, position)
        # Redimensiona as imagens para a janela
        window_size = pygame.display.get_surface().get_size()
        self.surface = pygame.transform.scale(self.surface, window_size)
        self.rect = self.surface.get_rect(topleft=position)
        print(f"Camada: {self.name} | Tamanho do Rect: {self.rect.size}")

    def move(self):
        pass
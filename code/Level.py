import sys
import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list [Entity] = []
        #O extend(), 'aloca' os 5 elementos da lista da EntityFactory diretamente para dentro da self.entity_list
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity('Player')  # Retorna o objeto Player
        self.entity_list.append(self.player)

        self.font_level = pygame.font.SysFont("Comic Sans MS", 16)
        self.window_height = self.window.get_height() # Pega a altura da janela para alocar dinamicamente os textos

    def run(self, ):
        pygame.mixer_music.load('./assets/LevelsMusic.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        print(self.entity_list)
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                entity.move()

            for entity in self.entity_list:
                self.window.blit(entity.surface, entity.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(self.font_level, f'fps: {clock.get_fps():.0f}', (255, 255, 255),(10, self.window_height - 10))
            pygame.display.flip()

    def level_text(self, font, text: str, text_color: tuple, text_pos: tuple):
        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(bottomleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        return text_rect
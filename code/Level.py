import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list [Entity] = []
        #O extend(), 'aloca' os 5 elementos da lista da EntityFactory diretamente para dentro da self.entity_list
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while True:
            for entity in self.entity_list:
                self.window.blit(entity.surface, entity.rect)
            pygame.display.flip()
        pass
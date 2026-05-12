import sys
import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list [Entity] = []

        # Carregamento Inicial
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity('Player')  # Retorna o objeto Player
        self.entity_list.append(self.player)

        # Coinfiguração do Spawn dos inimigos
        self.spawn_limit = 10  # Número total de inimigos na fase
        self.spawn_count = 0  # Contador de quantos já nasceram
        self.enemies_list = []  # Lista específica para facilitar colisões
        self.level_finished = False  # Para saber se a fase acabou
        self.SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_ENEMY_EVENT, 3000) # Dispara o evento a cada 2000ms (2 segundos)
        self.shots_list = []
        self.mediator = EntityMediator(self.player, self.entity_list, self.enemies_list, self.shots_list)

        self.font_level = pygame.font.SysFont("Comic Sans MS", 16)
        self.window_height = self.window.get_height() # Pega a altura da janela para alocar dinamicamente os textos

    def run(self, ):
        pygame.mixer_music.load('./assets/LevelsMusic.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == self.SPAWN_ENEMY_EVENT:
                    if self.spawn_count < self.spawn_limit:
                        new_enemy = EntityFactory.get_entity('Enemy1')
                        self.enemies_list.append(new_enemy)
                        self.entity_list.append(new_enemy)
                        self.spawn_count += 1
                    else:
                        # Para o timer para economizar processamento
                        pygame.time.set_timer(self.SPAWN_ENEMY_EVENT, 0)

            for entity in self.entity_list:
                entity.move()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.player.shoot(self.entity_list, self.shots_list)

            self.mediator.update()

            for entity in self.entity_list:
                # Se for o Player, vamos checar se ele deve piscar
                if entity == self.player:
                    current_time = pygame.time.get_ticks()
                    # Se estiver no período de invencibilidade pisca a cada 100ms
                    if current_time - self.player.last_hit_time < self.player.invincibility_duration:
                        if (current_time // 100) % 2 == 0:
                            continue
                self.window.blit(entity.surface, entity.rect)

            self.level_text(self.font_level, f'fps: {clock.get_fps():.0f}', (255, 255, 255),(10, self.window_height - 10))
            pygame.display.flip()

    def level_text(self, font, text: str, text_color: tuple, text_pos: tuple):
        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(bottomleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        return text_rect


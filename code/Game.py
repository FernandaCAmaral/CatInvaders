from code.EntityFactory import EntityFactory
from code.Level import Level
from code.Menu import Menu

import pygame

from code.Tutorial import Tutorial


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 500))


    def run(self):
        while True:
            menu = Menu(self.window)
            resultado = menu.run()

            if resultado == "JOGAR":
                player = EntityFactory.get_entity('Player')
                # Lista de fases para percorrer
                fases = ['Level1', 'Level2', 'Level3']

                for i,nome_fase in enumerate(fases):
                    level = Level(self.window, nome_fase, player)
                    resultado_level = level.run()

                    if resultado_level == "VITÓRIA":
                        # Checa se é a última fase da lista
                        if i == len(fases) - 1:
                            level.show_victory_screen() # Se for o último level, chama a tela final de vitória
                        else:
                            continue # Se não, o loop continua para a próxima fase
                    else:
                        break # Se perdeu ou saiu, interrompe o loop de fases

            elif resultado == "TUTORIAL":
                tutorial = Tutorial(self.window)
                tutorial.run()

            elif resultado == "SAIR":
                pygame.quit()
                exit()

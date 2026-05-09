from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 500))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            #Checagem de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Fecha a janela
                    quit() # Encerra o pygame
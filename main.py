import pygame

pygame.init()
window = pygame.display.set_mode((700, 500))

while True:
    #Checagem de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha a janela
            quit() # Encerra o pygame
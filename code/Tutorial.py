import pygame
import sys

class Tutorial:
    def __init__(self, window):
        self.window = window
        self.font_title = pygame.font.SysFont("Comic Sans MS", 40)
        self.font_text = pygame.font.SysFont("Comic Sans MS", 20)

    def run(self):
        while True:
            self.window.fill((30, 30, 30))

            # Título
            title_surf = self.font_title.render("COMO JOGAR", True, (255, 215, 0))
            self.window.blit(title_surf, (400 - title_surf.get_width()//2, 50))

            # Instruções
            instructions = [
                "SETAS: Movimentar o Gatinho",
                "ESPAÇO: Atirar nos Inimigos",
                "OBJETIVO: Sobreviver às 3 fases!",
                "",
                "Pressione ESC ou M para voltar ao Menu"
            ]

            for i, line in enumerate(instructions):
                text_surf = self.font_text.render(line, True, (255, 255, 255))
                self.window.blit(text_surf, (400 - text_surf.get_width()//2, 150 + i * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                        return # Volta para o loop do Game.py
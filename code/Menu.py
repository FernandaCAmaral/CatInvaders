import pygame
from pygame import Rect
from pygame.surface import Surface


class Menu:
    def __init__(self, window):
        self.window = window
        # Carrega a imagem original
        original_surface = pygame.image.load("./assets/MenuBg.png")
        # Redimensiona a imagem para o tamanho da janela
        self.surface = pygame.transform.scale(original_surface, self.window.get_size())

        # Define uma área (retângulo) para a imagem, permitindo manipular
        self.rect = self.surface.get_rect()

        #Define a fonte
        self.font_titulo = pygame.font.SysFont("Comic Sans MS", 50)
        self.font_botoes = pygame.font.SysFont("Comic Sans MS", 30)

    def run(self):
        # Carrega e toca a música do Menu
        pygame.mixer.music.load('assets/menu.mp3')
        pygame.mixer.music.play(-1)

        # Define o centro do Eixo X e Y
        center_x, center_y = self.window.get_rect().center

        # Define as posições das opçoes do Menu em relação ao centro
        pos_titulo = (center_x, center_y - 80)
        pos_iniciar = (center_x, center_y)
        pos_como_jogar = (center_x, center_y + 40)
        pos_sair = (center_x, center_y + 80)

        while True:

            # Enquadra a imagem definida no retângulo
            self.window.blit(self.surface, self.rect)

            # Exibe a caixa para englobar o Menu
            self.draw_menu_box()

            # Exibe as opçoes do menu
            self.menu_text (self.font_titulo,"Cat Invaders",(0, 102, 51),pos_titulo)
            rect_iniciar = self.menu_text(self.font_botoes, "Iniciar", (0, 0, 0), pos_iniciar, True)
            rect_tutorial = self.menu_text(self.font_botoes, "Como Jogar", (0, 0, 0), pos_como_jogar, True)
            rect_sair = self.menu_text(self.font_botoes, "Sair", (0, 0, 0), pos_sair, True)
            pygame.display.flip()  # Atualiza na tela

            # Checagem de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Fecha a janela
                    quit() # Encerra o pygame

                # Pega a posição do Mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botão esquerdo do mouse
                        mouse_pos = event.pos

                        # Checagem de cliques
                        if rect_iniciar.collidepoint(mouse_pos):
                            return "JOGAR"
                        elif rect_tutorial.collidepoint(mouse_pos):
                            return "TUTORIAL"
                        elif rect_sair.collidepoint(mouse_pos):
                            return "SAIR"


    def menu_text(self, font, text: str, text_color: tuple, text_center_pos: tuple, is_button: bool = False):

        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Verifica se o mouse está colidindo com o retângulo do texto
        if is_button and text_rect.collidepoint(pygame.mouse.get_pos()):
            # Muda a cor se o mouse estiver em cima (ex: fica cinza)
            text_surf = font.render(text, True, (64, 64, 64))

        self.window.blit(source=text_surf, dest=text_rect)
        return text_rect


    # Cria uma caixa para englobar as opções do menu
    def draw_menu_box(self):
        # Define o tamanho da caixa
        box_width = 350
        box_height = 310

        # Centraliza a caixa na tela
        center_x, center_y = self.window.get_rect().center
        # Cria o Rect da caixa
        box_rect = pygame.Rect(0, 0, box_width, box_height)
        box_rect.center = (center_x, center_y)

        # Cria uma superfície com transparência, permitindo que o background apareça atrás
        overlay = pygame.Surface((box_width, box_height), pygame.SRCALPHA)

        # Desenha o fundo da caixa (com 150 de opacidade)
        pygame.draw.rect(overlay, (192, 192, 192, 150), (0, 0, box_width, box_height), border_radius=20)

        # Aplica na janela
        self.window.blit(overlay, box_rect)
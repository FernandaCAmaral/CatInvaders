import pygame
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 4
        self.last_hit_time = 0
        self.invincibility_duration = 1500
        self.health = 100
        self.max_health = 100
        # Configuração para o métdo shoot
        self.shot_cooldown = 500  # Meio segundo entre tiros
        self.last_shot_time = 0

        # Define o ponto inicial fora da tela, à esquerda para a entrada
        self.rect.x = -80
        self.rect.y = 340  # Posição inicial no gramado
        self.entering = True  # Variável para controlar a animação inicial

        # Lida com o Sprite Sheet do personagem
        self.sprite_sheet = self.surface
        self.frame_width = 64
        self.frame_height = 64

        self.surface = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)

        # Ajusta o rect para o tamanho correto do personagem (64x64)
        self.rect = self.surface.get_rect()

        # Configuração de Animação
        self.frames = []
        self.load_frames()  # Métdo para recortar os frames

        self.current_frame = 0
        self.animation_speed = 0.15
        self.frame_index = 0.0

    def load_frames(self):
        line_y = 192

        for i in range(8):
            temp_surface = pygame.Surface((64, 64), pygame.SRCALPHA)
            temp_surface.blit(self.sprite_sheet, (0, 0), (i * 64, line_y, 64, 64))

            # Usando a dica de limpar as bordas vazias:
            real_area = temp_surface.get_bounding_rect()
            cropped_frame = temp_surface.subsurface(real_area)

            # Redimensionando para o gatinho não ficar minúsculo
            final_frame = pygame.transform.scale(cropped_frame, (90, 90))
            self.frames.append(final_frame)

        # Define a imagem inicial
        self.surface = self.frames[0]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.surface = self.frames[int(self.frame_index)]

    def shoot(self, entity_list, shots_list):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shot_cooldown:
            # O tiro sai da frente do gatinho (meio da altura dele)
            shot_x = self.rect.right + 15
            shot_y = self.rect.centery + 18
            new_shot = PlayerShot('PlayerShot', (shot_x, shot_y))

            entity_list.append(new_shot)
            shots_list.append(new_shot)

            self.last_shot_time = current_time

    def move(self):
        is_moving = False

        # Lógica de entrada automática
        if self.entering:
            is_moving = True
            self.rect.x += 2  # Ele caminha sozinho até a posição 50
            if self.rect.x >= 50:
                self.entering = False

        # Controles normais
        else:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
                is_moving = True
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
                is_moving = True
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                is_moving = True
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                is_moving = True

        # LIMITAÇÃO DE MOVIMENTO
        if self.rect.top < 100: self.rect.top = 100
        if self.rect.bottom > 400: self.rect.bottom = 400
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > 900: self.rect.right = 900

        # ANIMAÇÃO
        if is_moving:
            self.animate()  # Só troca o frame se estiver andando
        else:
            # Se parado, volta para o frame 0 (posição de repouso)
            self.current_frame = 0
            self.surface = self.frames[0]
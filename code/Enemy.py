import pygame

from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name, position, speed, damage):
        # Chama o construtor da Entity (carrega a imagem base)
        super().__init__(name, position)

        self.speed = speed
        self.damage = damage

        # Configuração do SpriteSheet (seguindo a lógica que usamos no Player)
        self.sprite_sheet = self.surface
        self.frame_width = 64
        self.frame_height = 64

        self.frames = []
        self.load_enemy_frames()

        self.frame_index = 0.0
        self.animation_speed = 0.2
        self.surface = self.frames[0]
        self.rect = self.surface.get_rect(topleft=position)

    def load_enemy_frames(self):
        line_y = 128
        for i in range(8):
            temp_surface = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
            temp_surface.blit(self.sprite_sheet, (0, 0),(i * self.frame_width, line_y, self.frame_width, self.frame_height))

            # Limpa as bordas e redimensiona
            real_area = temp_surface.get_bounding_rect()
            if real_area.width > 0 and real_area.height > 0:
                cropped = temp_surface.subsurface(real_area)
                final_frame = pygame.transform.scale(cropped, (50, 50))
                self.frames.append(final_frame)

    def animate(self):
        if self.frames:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            self.surface = self.frames[int(self.frame_index)]

    def move(self):
        # Move para a esquerda
        self.rect.x -= self.speed
        self.animate()
import pygame

class EntityMediator:
    def __init__(self, player, entity_list, enemies_list):
        self.player = player
        self.entity_list = entity_list
        self.enemies_list = enemies_list

    def update(self):
        self.__check_collisions()
        self.__check_bounds()
        if self.player.health <= 0:
            print("Game Over!")

    def __check_collisions(self):
        current_time = pygame.time.get_ticks()
        # Usamos a lista auxiliar para colisão do Player com o Enemy
        for enemy in self.enemies_list[:]:
            if self.player.rect.colliderect(enemy.rect):
                # Lógica de Invencibilidade do Player
                if current_time - self.player.last_hit_time > self.player.invincibility_duration:
                    self.player.health -= enemy.damage
                    self.player.last_hit_time = current_time # Reseta o timer de proteção
                    print(f"Gatinho atingido! Vida: {self.player.health}")

    def __check_bounds(self):
        # Limpeza de inimigos que saem da tela
        for entity in self.entity_list[:]:
            if 'Enemy' in entity.name and entity.rect.right < 0:
                self.entity_list.remove(entity)
                if entity in self.enemies_list:
                    self.enemies_list.remove(entity)
                print("DEBUG: Mediator removeu inimigo fora da tela.")

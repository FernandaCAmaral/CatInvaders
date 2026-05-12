import pygame

class EntityMediator:
    def __init__(self, player, entity_list, enemies_list, shots_list):
        self.player = player
        self.entity_list = entity_list
        self.enemies_list = enemies_list
        self.shots_list = shots_list

    def update(self):
        self.__check_collisions()
        self.__check_bounds()
        self.__check_shot_impacts()
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

    def __check_shot_impacts(self):
        for shot in self.shots_list[:]:
            for enemy in self.enemies_list[:]:
                if shot.rect.colliderect(enemy.rect):
                    # Se o tiro bater no inimigo:
                    if shot in self.shots_list: self.shots_list.remove(shot)
                    if shot in self.entity_list: self.entity_list.remove(shot)

                    if enemy in self.enemies_list: self.enemies_list.remove(enemy)
                    if enemy in self.entity_list: self.entity_list.remove(enemy)

                    break

    def __check_bounds(self):
        # Limpeza de inimigos que saem da tela
        for entity in self.entity_list[:]:
            if 'Enemy' in entity.name and entity.rect.right < 0:
                self.entity_list.remove(entity)
                if entity in self.enemies_list:
                    self.enemies_list.remove(entity)

        for shot in self.shots_list[:]:
            if shot.rect.left > 900:
                self.shots_list.remove(shot)
                self.entity_list.remove(shot)

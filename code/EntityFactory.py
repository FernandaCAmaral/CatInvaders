import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                # Cria: Level1Bg0, Level1Bg1, Level1Bg2,
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                return list_bg
            case 'Player':
                return Player('Player', (0,0))
            case 'Enemy1':
                return Enemy('Enemy1walk', (920, random.randint(110,390)), speed=1.5, damage=10)
            case 'Enemy2':
                return Enemy('Enemy2walk', position, speed=2, damage=20)
            case 'Enemy3':
                return Enemy('Enemy3walk', position, speed=3, damage=25)


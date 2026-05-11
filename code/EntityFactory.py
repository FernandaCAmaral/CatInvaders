from code.Background import Background
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

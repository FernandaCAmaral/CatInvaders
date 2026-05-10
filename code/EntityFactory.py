from code.Background import Background
class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                # Cria: Level1Bg0, Level1Bg1, Level1Bg2,
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    print(f'imagem {i} carregada com sucesso')
                return list_bg

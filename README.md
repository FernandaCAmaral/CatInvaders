# 🐱 CatInvader - Demo de Jogo 2D

Este projeto foi desenvolvido como requisito avaliativo para a faculdade **Uninter**, especificamente para a disciplina de **Linguagem de Programação Aplicada**. O objetivo é aplicar conceitos práticos de desenvolvimento de software, arquitetura de sistemas e lógica de jogos.

---

## 🛠️ Tecnologias e Ferramentas
O jogo foi construído inteiramente em **Python**, utilizando a biblioteca **Pygame** para o gerenciamento de gráficos, sons e colisões. 

### Principais conceitos aplicados:
*   **Programação Orientada a Objetos (POO):** Classes para entidades, níveis e gerenciadores.
*   **Design Pattern Factory:** Utilizado na `EntityFactory` para criação dinâmica de objetos.
*   **Design Pattern Mediator:** Utilizado no `EntityMediator` para centralizar a lógica de colisão e interação entre entidades.


## 🎮 Como Iniciar o Jogo

### 1. Pré-requisitos
Você precisa ter o Python instalado. Além disso, instale a biblioteca Pygame via terminal:
```bash
pip install pygame
```
### 2. Execução
Execute o arquivo principal:

```bash
python main.py
```

## 🕹️ Comandos e Objetivo
*   SETAS DIRECONAIS: Movimentam o gatinho pela tela.
*   BARRA DE ESPAÇO: Dispara o ataque contra os inimigos.
*   TECLA M / ESC: Retorna ao menu principal.
*   OBJETIVO: Sobreviver às 3 fases progressivas. Atenção: a vida do gatinho não se regenera entre os níveis, exigindo cautela do jogador!

## 🎨 Créditos de Recursos
Agradecimentos aos criadores dos recursos visuais utilizados neste projeto:

*   Gatinho (Player): [dogchicken](https://opengameart.org/content/cat-fighter-addon2-assault-rifle-kit)
*   Inimigos (Enemies): [craftpix](https://craftpix.net/freebies/free-slime-mobs-pixel-art-top-down-sprite-pack/?num=1&count=105&sq=cat&pos=8)
*   Cenários (Backgrounds): [craftpix](https://craftpix.net/freebies/free-forest-battle-backgrounds/?num=1&count=57&sq=battle&pos=15)

## 🚀 To-Do (Melhorias Futuras)
Estas são as funcionalidades planejadas para evoluir esta demonstração, fique à vontade para implementá-las:

*   [ ] Sistema de Score: Implementação de um contador de pontos acumulativo por inimigo derrotado.

*   [ ] Animação de Morte: Inclusão de sprites de morte para os inimigos atingidos.

*   [ ] Efeitos Sonoros: Adição de sons individuais para tiro, impacto de dano e vitória.

## 📸 Screenshots das Fases

Abaixo, os registros das três etapas progressivas do jogo:

<img width="800" height="495" alt="Image" src="https://github.com/user-attachments/assets/6720a8df-8ebb-4b12-807d-8d723a0b7efb" />
<img width="800" height="495" alt="Image" src="https://github.com/user-attachments/assets/ad633e0d-15cb-4031-a884-80c6f0d74a6c" />
<img width="800" height="495" alt="Image" src="https://github.com/user-attachments/assets/59e7d9e5-4d22-48a9-bb91-e877da82f514" />

## 📄 Autor
Fernanda Amaral

Instituição: Centro Universitário Internacional Uninter

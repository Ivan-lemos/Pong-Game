from turtle import Turtle


class Scoreboard(Turtle):
    """Gerencia a pontuação dos jogadores no jogo de Pong.

    Herda de Turtle para exibir as pontuações na tela.
    """

    def __init__(self):
        """Inicializa um novo objeto Scoreboard.

        Define a cor, levanta a caneta, esconde a tartaruga e inicializa as pontuações
        dos jogadores esquerdo (l_score) e direito (r_score) como zero.
        Em seguida, atualiza o placar na tela.
        """
        super().__init__()
        self.color("white") # Define a cor do texto do placar como branco
        self.penup() # Levanta a caneta para não desenhar ao mover
        self.hideturtle() # Esconde a tartaruga que representa o placar
        self.l_score = 0 # Pontuação do jogador esquerdo
        self.r_score = 0 # Pontuação do jogador direito
        self.update_scoreboard() # Exibe as pontuações iniciais na tela

    def update_scoreboard(self) -> None:
        """Atualiza a exibição do placar na tela.

        Limpa o placar anterior e escreve as pontuações atuais dos jogadores
        nas posições designadas na tela.
        """
        self.clear() # Limpa o que estava escrito anteriormente na tela
        self.goto(-100, 200) # Move a tartaruga para a posição da pontuação do jogador esquerdo
        self.write(self.l_score, align="center", font=("Courier", 80, "normal")) # Escreve a pontuação do jogador esquerdo
        self.goto(100, 200) # Move a tartaruga para a posição da pontuação do jogador direito
        self.write(self.r_score, align="center", font=("Courier", 80, "normal")) # Escreve a pontuação do jogador direito

    def l_point(self) -> None:
        """Incrementa a pontuação do jogador esquerdo em 1 e atualiza o placar.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self) -> None:
        """Incrementa a pontuação do jogador direito em 1 e atualiza o placar.
        """
        self.r_score += 1
        self.update_scoreboard()



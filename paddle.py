from turtle import Turtle


class Paddle(Turtle):
    """Representa uma raquete no jogo de Pong, herdando de Turtle para capacidades gráficas.

    Cada raquete é um objeto Turtle que pode se mover para cima e para baixo na tela.
    """

    def __init__(self, position: tuple):
        """Inicializa uma nova raquete.

        Args:
            position: Uma tupla (x, y) que define a posição inicial da raquete na tela.
        """
        super().__init__()
        self.shape("square") # Define a forma da raquete como um quadrado
        self.color("white") # Define a cor da raquete como branca
        self.shapesize(stretch_wid=5, stretch_len=1) # Estica o quadrado para formar uma raquete retangular
        self.penup() # Levanta a caneta para que a raquete não desenhe ao se mover
        self.goto(position) # Move a raquete para a posição inicial especificada

    def go_up(self) -> None:
        """Move a raquete para cima.

        A raquete se move 20 unidades para cima no eixo Y.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self) -> None:
        """Move a raquete para baixo.

        A raquete se move 20 unidades para baixo no eixo Y.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



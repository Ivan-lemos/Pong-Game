from turtle import Turtle

STEP_DISTANCE = 20  # Distância de movimento da raquete

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

        A raquete se move para cima pela distância definida em STEP_DISTANCE,
        desde que não ultrapasse o limite superior da tela.
        """
        new_y = self.ycor() + STEP_DISTANCE
        # Verifica se a nova posição Y está dentro dos limites da tela
        # O limite de 250 e -250 é uma estimativa baseada no tamanho da raquete e da tela
        if new_y < 250:
            self.sety(new_y)

    def go_down(self) -> None:
        """Move a raquete para baixo.

        A raquete se move para baixo pela distância definida em STEP_DISTANCE,
        desde que não ultrapasse o limite inferior da tela.
        """
        new_y = self.ycor() - STEP_DISTANCE
        # Verifica se a nova posição Y está dentro dos limites da tela
        if new_y > -250:
            self.sety(new_y)




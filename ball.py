from turtle import Turtle


class Ball(Turtle):
    """Representa a bola no jogo de Pong, herdando de Turtle para capacidades gráficas.

    A bola se move pela tela, ricocheteia nas paredes e nas raquetes, e sua velocidade
    aumenta a cada vez que ricocheteia em uma raquete.
    """

    def __init__(self):
        """Inicializa um novo objeto Ball.

        Define a cor, forma, levanta a caneta e inicializa os vetores de movimento
        e a velocidade da bola.
        """
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3  # Componente X do movimento da bola
        self.y_move = 3  # Componente Y do movimento da bola
        self.move_speed = 0.1  # Velocidade inicial da bola

    def move(self) -> None:
        """Move a bola para sua próxima posição com base nos vetores de movimento.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        """Inverte a direção vertical da bola (ricochete na parede superior/inferior).
        """
        self.y_move *= -1

    def bounce_x(self) -> None:
        """Inverte a direção horizontal da bola (ricochete na raquete ou parede lateral).

        Também aumenta a velocidade da bola após o ricochete.
        """
        self.x_move *= -1
        self.move_speed *= 0.9  # Aumenta a velocidade da bola

    def reset_position(self) -> None:
        """Reinicia a posição da bola para o centro da tela e inverte sua direção horizontal.

        Redefine a velocidade da bola para o valor inicial.
        """
        self.goto(0, 0)
        self.move_speed = 0.1  # Reseta a velocidade
        self.bounce_x()  # Inverte a direção para o próximo saque



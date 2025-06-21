from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Configuração da tela do jogo
screen = Screen()
screen.bgcolor("black") # Define a cor de fundo da tela como preto
screen.setup(width=800, height=600) # Define as dimensões da tela
screen.title("Pong") # Define o título da janela
screen.tracer(0) # Desliga a atualização automática da tela para controle manual

# Cria as raquetes para os jogadores e a bola
r_paddle = Paddle((350, 0)) # Raquete do jogador da direita
l_paddle = Paddle((-350, 0)) # Raquete do jogador da esquerda
ball = Ball() # A bola do jogo
scoreboard = Scoreboard() # O placar do jogo

# Configura os ouvintes de teclado para controlar as raquetes
screen.listen() # Começa a escutar eventos do teclado
screen.onkey(r_paddle.go_up, "Up") # Seta para cima move a raquete direita para cima
screen.onkey(r_paddle.go_down, "Down") # Seta para baixo move a raquete direita para baixo
screen.onkey(l_paddle.go_up, "w") # Tecla 'w' move a raquete esquerda para cima
screen.onkey(l_paddle.go_down, "s") # Tecla 's' move a raquete esquerda para baixo

# Loop principal do jogo
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # Controla a velocidade do jogo
    screen.update() # Atualiza a tela para mostrar os movimentos
    ball.move() # Move a bola

    # Detecta colisão da bola com as paredes superior e inferior
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() # Inverte a direção vertical da bola

    # Detecta colisão da bola com as raquetes
    # Verifica a distância da bola para cada raquete e se a bola está na área de colisão horizontal
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x() # Inverte a direção horizontal da bola e aumenta a velocidade

    # Detecta quando a raquete da direita perde a bola
    if ball.xcor() > 380:
        ball.reset_position() # Reinicia a posição da bola
        scoreboard.l_point() # Adiciona ponto para o jogador da esquerda

    # Detecta quando a raquete da esquerda perde a bola
    if ball.xcor() < -380:
        ball.reset_position() # Reinicia a posição da bola
        scoreboard.r_point() # Adiciona ponto para o jogador da direita

# Mantém a janela aberta até ser clicada
screen.exitonclick()



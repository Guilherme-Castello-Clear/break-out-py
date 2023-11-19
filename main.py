from turtle import Screen
from paddle import Paddle
from block import Block
from ball import Ball

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
BLOCKS = []
SCORE = 0

# SCREEN
screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


# PADDLE
paddle = Paddle((0, -200))


# BLOCKS
def render_blocks():
    block_x = -550
    block_y = 330

    for i in range(1):
        for j in range(11):
            block = Block((block_x, block_y))
            BLOCKS.append(block)
            block_x += 105
        block_x = -550
        block_y -= 45


screen.listen()
render_blocks()
ball = Ball((0, 0))

game_on = True

while True:
    screen.onkey(paddle.move_left, "Left")
    screen.onkey(paddle.move_right, "Right")
    ball.move()
    if ball.ycor() > 350 or ball.distance(paddle) < 60:
        ball.bounce('y')
    if ball.xcor() > 550 or ball.xcor() < -550:
        ball.bounce('x')
    if ball.ycor() < -300:
        game_on = False
        print('-= Game Over =-')
        break
    if BLOCKS == []:
        game_on = False
        print(f'You win! | Score: {SCORE}')
        break
    for block in BLOCKS:
        if ball.distance(block) < 40:
            ball.bounce('y')
            ball.bounce('x')
            block.hideturtle()
            BLOCKS.remove(block)
            SCORE += 1
            print(f'Current score: {SCORE}')

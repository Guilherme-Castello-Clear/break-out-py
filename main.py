from turtle import Screen
from paddle import Paddle
from block import Block

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
BLOCKS = []


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

    for i in range(4):
        for j in range(11):
            block = Block((block_x, block_y))
            BLOCKS.append(block)
            block_x += 105
        block_x = -550
        block_y -= 45


screen.listen()
render_blocks()

screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

screen.exitonclick()

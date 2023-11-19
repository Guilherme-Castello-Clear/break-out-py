from turtle import Screen
from paddle import Paddle

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# SCREEN
screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


# PADDLE
paddle = Paddle((0, -200))

screen.listen()

screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

screen.exitonclick()

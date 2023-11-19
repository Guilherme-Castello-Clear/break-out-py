from turtle import Turtle


class Ball(Turtle):
	def __init__(self, xy):
		super().__init__()
		self.color('white')
		self.penup()
		self.shape('circle')
		self.x_direction = 5
		self.y_direction = 5

	def move(self):
		x = self.xcor() + self.x_direction
		y = self.ycor() + self.y_direction
		self.goto((x, y))

	def bounce(self, axis):
		if axis == 'x': self.x_direction *= -1
		elif axis == 'y': self.y_direction *= -1

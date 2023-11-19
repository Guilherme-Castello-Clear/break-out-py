from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, xy):
		super().__init__()
		self.shape('square')
		self.penup()
		self.color('white')
		self.shapesize(stretch_wid=0.5, stretch_len=5)
		self.goto(xy)

	def move_right(self):
		if self.xcor() < 550:
			x = self.xcor() + 50
			self.goto((x, self.ycor()))

	def move_left(self):
		if self.xcor() > -550:
			x = self.xcor() - 50
			self.goto((x, self.ycor()))

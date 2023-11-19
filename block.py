from turtle import Turtle


class Block(Turtle):
	def __init__(self, xy):
		super().__init__()
		self.shape('square')

		self.penup()
		self.color('white')
		self.goto(xy)
		self.shapesize(stretch_wid=2, stretch_len=5)

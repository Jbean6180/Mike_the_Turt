import turtle

def drawSquare(Myturtle):
	Myturtle.color("green")
	for i in range(4):
		Myturtle.forward(100)
		Myturtle.right(90)

def drawTriangle(Myturtle):
	Myturtle.color("red")
	for i in range(4):
		Myturtle.forward(100)
		Myturtle.right(120)

def drawSomethingCool(Myturtle):
	Myturtle.color("yellow")
	for i in range(100):
		Myturtle.forward(2 * 2 * i)
		Myturtle.right(90)
		Myturtle.right(45)

def drawSomethingCooler(my_turtle):
	my_turtle.color("blue")
	for i in range (36):
		drawSquare(my_turtle)
		my_turtle.right(10)

# create the turtle's play pen
canvas = turtle.Screen()
canvas.bgcolor("black")

# create a turtle named mike
mike = turtle.Turtle()
mike.shapesize(2, 2, 2)
mike.color("yellow")
mike.shape("turtle")
mike.speed(10)

# drawSquare(mike)
# drawSomethingCool(mike)
drawSomethingCooler(mike)

# exits the screen when clicked
canvas.exitonclick()

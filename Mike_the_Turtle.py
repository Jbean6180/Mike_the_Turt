import turtle

def drawSquare(Myturtle):
	Myturtle.color("gold")
	for i in range(4):
		Myturtle.forward(100)
		Myturtle.right(90)

def drawTriangle(Myturtle):
	Myturtle.color("red")
	for i in range(4):
		Myturtle.forward(100)
		Myturtle.right(120)

def drawSomethingCool(Myturtle):
	Myturtle.color("purple")
	for i in range(100):
		Myturtle.forward(2 * 2 * i)
		Myturtle.right(90)
		Myturtle.right(45)

def drawSomethingSpicyFlu(Myturtle):
	Myturtle.color("pink")
	for i in range(720):
		Myturtle.forward(1.5 * i)
		Myturtle.left(i*2)

def drawSomethingSpiky(Myturtle):
	Myturtle.color("orange")
	for i in range(720):
		Myturtle.forward(i)
		Myturtle.left(30)

def drawSomethingCooler(my_turtle):
	my_turtle.color("blue")
	for i in range (36):
		drawSomethingSpiky(my_turtle)
		my_turtle.right(10)

def drawSomethingAwesome(my_turtle, my_turtle2,my_turtle3,my_turtle4):
	my_turtle.color("cyan")
	for i in range (720):
		my_turtle.right(30)
		my_turtle2.left(40)
		my_turtle2.forward(i)
		my_turtle.forward(i)
		my_turtle3.right(50)
		my_turtle4.left(60)
		my_turtle4.forward(i)
		my_turtle3.forward(i)


# create the turtle's play pen
canvas = turtle.Screen()
canvas.bgcolor("black")

# create a turtle named mike
mike = turtle.Turtle()
mike.shapesize(2, 2, 2)
mike.color("green")
mike.shape("turtle")
mike.speed(25)

# create a turtle named terry
terry = turtle.Turtle()
terry.shapesize(2, 2, 2)
terry.color("brown")
terry.shape("turtle")
terry.speed(25)

# create a turtle named sara
sara = turtle.Turtle()
sara.shapesize(2, 2, 2)
sara.color("pink")
sara.shape("duck")
sara.speed(25)

# create a turtle named pablo
pablo = turtle.Turtle()
pablo.shapesize(2, 2, 2)
pablo.color("yellow")
pablo.shape("turtle")
pablo.speed(25)


drawSomethingAwesome(mike,terry,sara,pablo)

# exits the screen when clicked
canvas.exitonclick()

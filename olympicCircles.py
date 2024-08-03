import turtle

turtle.shape('turtle')
screen = turtle.Screen()

for i in range(360):
    turtle.color("blue")
    turtle.forward(1)
    turtle.left(1)
    turtle.width(7)
    turtle.tracer(50)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()

for i in range(360):
    turtle.color("black")
    turtle.forward(1)
    turtle.left(1)
    turtle.width(7)
    turtle.tracer(50)

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

for i in range(360):
    turtle.color("red")
    turtle.forward(1)
    turtle.left(1)
    turtle.width(7)
    turtle.tracer(50)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()

for i in range(360):
    turtle.color("yellow")
    turtle.forward(1)
    turtle.left(1)
    turtle.width(7)
    turtle.tracer(50)

turtle.penup()
turtle.goto(150, -50)
turtle.pendown()

for i in range(360):
    turtle.color("green")
    turtle.forward(1)
    turtle.left(1)
    turtle.width(7)
    turtle.tracer(50)

screen.exitonclick()
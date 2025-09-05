import turtle
turtle.Screen().bgcolor("Aqua")
turtle.Screen().setup(200,100)
star = turtle.Turtle()

star.forward(100)
star.left(120)
star.forward(100)
star.left(120)
star.forward(100)

star.penup()
star.right(150)
star.forward(90)

star.pendown()
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()
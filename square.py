# Making a square using turtle
import turtle
turtle.Screen().bgcolor("Aqua")
turtle.Screen().setup(400,500)
square = turtle.Turtle()

num_sides = 4
angles = 360/num_sides
side_length = 100
for i in range(num_sides):
    square.forward(side_length)
    square.right(angles)
turtle.done()
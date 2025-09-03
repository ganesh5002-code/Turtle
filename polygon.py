import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(700,600)
polygon = turtle.Turtle()

num_sides = 9
side_length = 90
angle = 360/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
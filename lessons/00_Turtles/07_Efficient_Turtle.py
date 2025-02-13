
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)  
colors = ["red", "orange", "green", "blue", "purple"]

def draw_polygon(sides):

    angle = 360/sides #angle according to number of sides

    for i in range(sides):    # loop according to number of sides
        tina.forward(10)                 # move tina forward
        tina.left(angle)                                # turn tin left by angle
for i in range(3, 1000):
    draw_polygon(i)

turtle.exitonclick()

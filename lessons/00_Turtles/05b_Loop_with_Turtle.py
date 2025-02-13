
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)         
                  # Make the turtle move as fast, but not too fast. 
tina.pencolor('brown')
tina.speed(0)

def draw_polygon(sides):


    angle = 10000/sides
    for i in range(sides):
        tina.backward(4)
    tina.left(angle)
for i in range(1, 1000):

    draw_polygon(i)

                         # Turn tina left by the left turn




turtle.exitonclick()                    # Close the window when we click on it

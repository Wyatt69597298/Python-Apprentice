"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle() 
tina.shape('turtle')                 # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
tina.color('yellow')
tina.pencolor('green')
tina.begin_fill()
tina.speed(2)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.penup()
tina.forward(30)
tina.write("hellooooooooooooooooo")
tina.end_fill()
tina.goto(-210,0)
tina.pendown()
tina.color('blue')
tina.begin_fill()
tina.circle(101, steps=55)
tina.end_fill()
tina.penup()
tina.goto(50,0)


sides = 10
angles = 40
for i in range(90):
    tina.left(sides)
    tina.forward(angles) 


turtle.exitonclick()                    # Close the window when we click on it


# Dont forget to check in your code!
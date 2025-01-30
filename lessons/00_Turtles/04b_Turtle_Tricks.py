"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here

tina.shape('turtle')
tina.speed(10)
tina.penup()
tina.goto(-150,0)
tina.color('red')
tina.begin_fill()
tina.pendown()
tina.circle(101, steps=50)
tina.end_fill()
tina.penup()
tina.goto(150,0)
tina.begin_fill()
tina.pendown()
tina.color('blue')
tina.circle(101, steps=50)
tina.end_fill()
tina.penup()
tina.goto(-100,-50)
tina.color('purple')
tina.pendown()
tina.begin_fill()
tina.forward(200)
tina.right(90)
tina.forward(100)
tina.right(90)
tina.forward(200)
tina.right(90)
tina.forward(100)
tina.end_fill()
tina.penup()
tina.goto(-79,12)
tina.right(180)
tina.write('GET DOWN MR. PRESIDIENT')


tina.speed(0)
tina.right(59)
tina.forward(200)
tina.left(59)
tina.forward(100)
tina.left(89)
tina.forward(500)
tina.left(90)
tina.forward(469)
tina.left(90)
tina.forward(515)
tina.left(90)
tina.forward(500)
for i in range(24):
    tina.left(90)
    tina.forward(500)
tina.write('AAAAAAAAHHHHHHHH')



for i in range(99):
    tina.left(90)
    tina.forward(500)
tina.write('...')
for i in range(102):
    tina.left(90)
    tina.forward(500)



turtle.exitonclick()                    # Close the window when we click on it

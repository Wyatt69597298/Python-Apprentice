
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle
turtle.setup (width=600, height=600)
tina = turtle.Turtle()
tina.shape('turtle')
for i in range(4):
    tina.forward(90)
    tina.right(90)

tina.left(45)
tina.forward(65)
tina.right(91)
tina.forward(62)
tina.penup()
tina.forward(1000)

turtle.exitonclick()



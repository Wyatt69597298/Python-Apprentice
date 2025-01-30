
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
tina.speed(0)
tina.color('blue')
tina.begin_fill()
for i in range(60):
    tina.left(30)
    tina.forward(60)
tina.end_fill()


turtle.exitonclick()



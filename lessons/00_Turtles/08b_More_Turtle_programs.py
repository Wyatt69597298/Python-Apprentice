"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle
turtle.setup (width=600, length=600)
tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(0)

for i in range(1000):
    tina.left(45)
    tina.forward(360)



 


















turtle.extoniclick()
# The following program displays the word Python with different alignments.

import turtle
import time

t = turtle.Turtle()
t.hideturtle()
t.up()
time.sleep(0.5)
t.goto(0, 60)
t.dot()
t.write("Python")
time.sleep(0.5)
t.goto(0, 30)
t.dot()
t.write("Python", align="right")
time.sleep(0.5)
t.goto(0, 0)
t.dot()
t.write("Python", align="center")
time.sleep(0.5)
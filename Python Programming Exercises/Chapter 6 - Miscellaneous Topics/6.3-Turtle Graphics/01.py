# The following program draws a rectangle having a red border and a yellow interior

import turtle

def main():
  t = turtle.Turtle()
  t.hideturtle()
  drawFilledRectangle(t, 0, 0, 100, 150, "red", "yellow")

def drawFilledRectangle(t, x, y, w, h, colorP="black", colorF="white"):
  ## Draw a filled rectangle with bottom-left corner (x, y),
  ## width w, height h, pen color colorP, and fill color colorF.
  t.pencolor(colorP)
  t.fillcolor(colorF)
  t.up()
  t.goto(x, y) # start at bottom-left corner of rectangle
  t.down()
  t.begin_fill()
  t.goto(x + w, y) # draw line to bottom-right corner
  t.goto(x + w, y + h) # draw line to top-right corner
  t.goto(x, y + h) # draw line to top-left corner
  t.goto(x, y) # draw line to bottom-left corner
  t.end_fill()

main()
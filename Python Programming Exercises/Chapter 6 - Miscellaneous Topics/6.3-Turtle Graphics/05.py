# The following program creates the bar chart on the next page. The x- coordinates of the bottom- left corners of the rectangles begin at -200 and successively increase by 76 pixels. The y- coordinates of the points are given by the list heights, with each value divided by 4. (The divisor is needed in order for the bar chart to fit in the canvas.) In the displayText function, the numbers -162, -10, -25, and -45 were obtained by trial-and-error.

import turtle

heights = [856, 420, 360, 260, 205] # number of speakers for each language

def main():
  t = turtle.Turtle()
  t.hideturtle()
  for i in range(5):
    drawFilledRectangle(t, -200 + (76 * i), 0, 76, heights[i] / 4, "black", "light blue")
  displayText(t)

def drawFilledRectangle(t, x, y, w, h, colorP="black", colorF="white"):
  ## Draw a filled rectangle with bottom-left corner (x, y), width w,
  ## height h, pen color colorP, and fill color colorF.
  t.pencolor(colorP)
  t.fillcolor(colorF)
  t.up()
  t.goto(x, y) # bottom-left corner of rectangle
  t.down()
  t.begin_fill()
  t.goto(x + w, y) # bottom-right corner of rectangle
  t.goto(x + w, y + h) # top-right corner of rectangle
  t.goto(x, y + h) # top-left corner of rectangle
  t.goto(x, y) # bottom-left corner of rectangle
  t.end_fill()

def displayText(t):
  languages = ["Mandarin", "Spanish", "English", "Hindi", "Bengali"]
  t.pencolor("blue")
  t.up()
  for i in range(5):
    # Display number at top of rectangle.
    t.goto(-162 + (76 * i), heights[i] / 4)
    t.write(str(heights[i]), align="center", font=("Arial", 10, "normal"))
    # Display language.
    t.goto(-162 + (76 * i), 10)
    t.write(languages[i], align="center", font=("Arial", 10, "normal"))
    # Display title of bar chart.
    t.goto(-200, -25)
    t.write("Principal Languages of the World", font=("Arial", 10, "normal"))
    t.goto(-200, -45)
    t.write('(in millions of "first language" speakers)', font=("Arial", 10, "normal"))

main()
# The following program uses the data in Table 6.3 to create the line chart on the right. The x-coordinates of the points begin at 40 and successively increase by 40. The y- coordinates of the points are given by the list yValues, with each value multiplied by 15. (The multiplier improves the readability of the graph.)In the displayText function, the numbers -3, -10, -20, and -50 were obtained by trial-and-error.

import turtle

yValues = [10.0, 7.4, 6.4, 5.3, 4.4, 3.7, 2.6] # percent for each year

def main():
  t = turtle.Turtle()
  t.hideturtle()
  drawLine(t, 0, 0, 300, 0) # Draw x-axis.
  drawLine(t, 0, 0, 0, 175) # Draw y-axis.
  for i in range(6):
      drawLineWithDots(t, 40 + (40 * i), 15 * yValues[i], 40 + (40 * (i + 1)), 15 * yValues[i + 1], "blue")
  drawTickMarks(t)
  displayText(t)

def drawLine(t, x1, y1, x2, y2, colorP="black"):
 ## Draw line segment from (x1, y1) to (x2, y2) having color colorP.
  t.up()
  t.goto(x1, y1)
  t.down()
  t.pencolor(colorP)
  t.goto(x2, y2)

def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):
  ## Draw line segment from (x1, y1) to (x2, y2) having color
  ## colorP and insert dots at both ends of the line segment.
  t.pencolor(colorP)
  t.up()
  t.goto(x1, y1) # beginning of line segment
  t.dot(5)
  t.down()
  t.goto(x2, y2) # end of line segment
  t.dot(5)

def drawTickMarks(t):
  ## Draw tick marks along x-axis.
  for i in range(1, 8):
    drawLine(t, 40 * i, 0, 40 * i , 10)
    # Draw tick mark on y-axis to indicate greatest value.
    drawLine(t, 0, 15 * max(yValues), 10, 15 * max(yValues))
    # Draw tick mark on y-axis to indicate least value.
    drawLine(t, 0, 15 * min(yValues), 10, 15 * min(yValues)) 

def displayText(t):
  t.pencolor("blue")
  t.up()
  # Display greatest y-value next to upper tick mark on y-axis.
  t.goto(-3, (15 * max(yValues)) - 10)
  t.write(max(yValues), align="right")
  # Display least y-value next to lower tick mark on y-axis.
  t.goto(-3, (15 * min(yValues)) - 10)
  t.write(min(yValues), align="right")
  # Display the years below the tick marks on x-axis.
  x = 40
  for i in range(2000, 2013, 2): 
    t.goto(x, -20)
    t.write(str(i), align="center")
    x += 40
  # Display title of graph.
  t.goto(0, -50)
  t.write("Percentage of College Freshmen Who Smoke")

main()
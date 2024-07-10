# Five- Pointed Star Figure 6.15(a) shows the star that appears on the American flag. In Fig. 6.15(b), L is the length of each side of the star, and the lower- left point of the star is at (0, 0). The coordinates of the center of the star are given, but are not needed in order to draw the star. However, the coordinates are useful if you want to draw a five- pointed star having a specified center rather than a specified lower- left point. The following program draws the five- pointed star in Fig. 6.15(b). The drawing of the entire American flag is given as a programming project.

import turtle

def main():
  t = turtle.Turtle()
  t.hideturtle()
  lengthOfSide = 200
  drawFivePointStar(t, 0, 0, lengthOfSide)

def drawFivePointStar(t, x, y, lengthOfSide):
  # Drawing begins at (x, y) and moves in a north-east direction.
  t.up()
  t.goto(x, y)
  t.left(36)
  t.down()
  for i in range(5):
    t.forward(lengthOfSide)
    t.left(144) # 144 = 180 – 36

main()
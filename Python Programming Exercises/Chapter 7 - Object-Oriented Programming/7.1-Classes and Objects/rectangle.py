class Rectangle:
  def __init__(self, width=1, height=1):
    self.width = width
    self.height = height

  def setWidth(self, width):
    self.width = width

  def setHeight(self, height):
    self.height = height

  def getWidth(self):
    return self.width
  
  def getHeight(self):
    return self.height
  
  def area(self):
    return self.height * self.width
  
  def perimeter(self):
    return 2 * (self.width + self.height)
  
  def __str__(self):
    return (f'Width: {self.width}\nHeight: {self.height}')
  
# rect1 = Rectangle(20, 30)

# print(rect1)
# print(rect1.getWidth())
# print(rect1.getHeight())
# print(rect1.area())
# print(rect1.perimeter())
# print()

# rect2 = Rectangle()

# rect2.setHeight(10)
# rect2.setWidth(15)
# print(rect2)
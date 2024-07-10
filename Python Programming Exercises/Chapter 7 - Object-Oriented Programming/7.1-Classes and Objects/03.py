import rectangle

# Create a rectangle with the default values for width and height
r = rectangle.Rectangle()

# Use the mutators to assign values to the instance variables.
r.setWidth(4)
r.setHeight(5)

print("The rectangle has the following measurements:")

# Use the accessor methods to retrieve the values of the instance variables.
print("Width is", r.getWidth())
print("Height is", r.getHeight())

# Use methods to calculate the area and perimeter of the rectangle.
print("Area is", r.area())
print("Perimeter is", r.perimeter())

# OUTPUT
# The rectangle has the following measurements:
# Width is 4
# Height is 5
# Area is 20
# Perimeter is 18
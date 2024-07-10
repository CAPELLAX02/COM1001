# The following program calculates the population density of a state. The parameterless function describeTask explains the purpose of the program.

def describeTask():
  print("This program displays the population")
  print("density of the last state to become")
  print("part of the United States.\n")

def calculateDensity(state, population, landArea):
  density = population / landArea
  print("The density of", state, "is", end=' ')
  print("{0:,.2f} people per square mile.".format(density))

def main():
  describeTask()
  calculateDensity('Hawaii', 1375000, 6423)

main()
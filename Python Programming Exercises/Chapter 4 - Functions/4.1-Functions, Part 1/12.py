# The following program contains a global variable.

x = 0 # Declare a global variable

def main():
  # Demonstrate the scope of a global variable.
  print(str(x) + ': function main')
  trivial()
  print(str(x) + ': function main')

def trivial():
  global x #
  x += 7
  print(str(x) + ': function trivial')

main()
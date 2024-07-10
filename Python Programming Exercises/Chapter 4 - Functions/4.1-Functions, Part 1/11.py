def main():
  # Demonstrate the scope of local variables.

  x = 5
  trivial()

def trivial():
  print(x)

main() # NameError: name 'x' is not defined
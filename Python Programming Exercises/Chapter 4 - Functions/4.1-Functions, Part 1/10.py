def main():
  # Demonstrate the scope of variables.
  x = 2
  print(str(x) + ': function main')
  trivial()
  print(str(x) + ': function main')

def trivial():
  x = 3
  print(str(x) + ': function trivial')

main()
def main():
  # Display the names of the first three presidents
  file = 'FirstPresidents.txt'
  displayWithForLoop(file)
  print()
  displayWithListComprehension(file)
  
def displayWithForLoop(file):
  infile = open(file, 'r')
  for line in infile:
    print(line, end='')
  infile.close()

def displayWithListComprehension(file):
  infile = open(file, 'r')
  listPres = [line.strip() for line in infile]
  infile.close()
  print(listPres)

main()

# George Washington
# John Adams
# Thomas Jefferson

# ['George Washington', 'John Adams', 'Thomas Jefferson']
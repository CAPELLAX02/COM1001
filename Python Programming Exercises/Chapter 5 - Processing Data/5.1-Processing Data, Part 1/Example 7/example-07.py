# The following program demostrates the use of three set-theoretic operations with two simple text files.

def main():
  # Use the two files to create two sets:
  infile = open('File1.txt', 'r')
  firstSet = {line.rstrip() + '\n' for line in infile}
  infile.close()

  infile = open('File2.txt', 'r')
  secondSet = {line.rstrip() + '\n' for line in infile}
  infile.close()

  # Createt files containing the union, intersection and difference of the original two files:
  outfile = open('Union.txt', 'w')
  outfile.writelines(firstSet.union(secondSet))
  outfile.close()

  outfile = open('Intersection.txt', 'w')
  outfile.writelines(firstSet.intersection(secondSet))
  outfile.close()

  outfile = open('Difference.txt', 'w')
  outfile.writelines(firstSet.difference(secondSet))
  outfile.close()

main()
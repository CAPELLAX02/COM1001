# The following rewrite of Example 4 uses set methods to create a file containing the names of users1 who are also written in users2.

def main():
  # Create a file of the presidents who also served as vice-presidents:
  users1set = createSetFromFile('users1.txt')
  users2set = createSetFromFile('users2.txt')
  bothUsers1andUsers2 = createIntersection(users1set,users2set)
  writeNamesToFile(bothUsers1andUsers2, 'both.txt')

def createSetFromFile(fileName):
  # Assume that the last line of the files ends with a newline ('\n') character.
  infile = open(fileName, 'r')
  namesSet = {name for name in infile}
  infile.close()
  return namesSet

def createIntersection(set1, set2):
  return set1.intersection(set2)

def writeNamesToFile(setName, fileName):
  outfile = open(fileName, 'w')
  outfile.writelines(setName)
  outfile.close()

main()
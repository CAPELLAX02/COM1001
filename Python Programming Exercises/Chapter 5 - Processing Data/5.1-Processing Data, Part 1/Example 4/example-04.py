def main():
  # Create a file of the users1's who are also in users2.
  secondUsers = createListFromFile('users2.txt')
  createNewFile(secondUsers, 'users1.txt', 'both.txt ')
  
def createListFromFile(fileName):
  infile = open(fileName, 'r')
  desiredList = [line.strip() for line in infile]
  infile.close()
  return desiredList

def createNewFile(listName, oldFileName, newFileName):
  infile = open(oldFileName, 'r')
  outfile = open(newFileName, 'w')
  for person in infile:
    if person.rstrip() in listName:
      outfile.write(person)
  infile.close()
  outfile.close()

main()
def main():
  # Create a text file containing the 20 states in alphabetical order.
  statesList = createListFromFile('States.txt')
  createSortedFile(statesList, 'StatesAlpha.txt')

def createListFromFile(fileName):
  infile = open(fileName, 'r')
  desiredList = [line.strip() for line in infile]
  infile.close()
  return desiredList

def createSortedFile(listName, fileName):
  listName.sort()

  for i in range(len(listName)):
    listName[i] = listName[i] + '\n'
  
  outfile = open(fileName, 'w')
  outfile.writelines(listName)
  outfile.close()
  
main()

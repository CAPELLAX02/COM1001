# The file USpresStatesDict.dat holds a dictionary giving the names of the presidents and their home states. Each key is a tuple of the form (last name, first name(s)). Two of the items in the dictionary are ('Kennedy', 'John'):'Massachusetts' and ('Reagan', 'Ronald'):'California'.

# The following program requests the name of a state and then displays the presidents from that state ordered alphabetically by their last names. The use of tuples to store the names simplifies alphabetizing the names. Although the items of a dictionary canned be ordered, they can be displayed in a specified order with statements such as 'print(sorted(dictName))'.

import pickle

def main():
  presidentDict = createDictionaryFromBinaryFile('USpresStatesDict.dat')
  state = getState(presidentDict)
  displayOutput(state, presidentDict)

def createDictionaryFromBinaryFile(fileName):
  infile = open(fileName, 'rb')
  dictionaryName = pickle.load(infile)
  infile.close()
  return dictionaryName

def getState(dictName):
  state = input('Enter the name of a state: ')
  if state in dictName.values():
    return state
  else:
    return f'There are no presidents from {state}.'
  
def displayOutput(state, dictName):
  if state.startswith('There'):
    print(state)
  else:
    print(f'Presidents from {state} is listed below:')
    for president in sorted(dictName):
      if dictName[president] == state:
        print(f'\t{president[1]} {president[0]}')

main()
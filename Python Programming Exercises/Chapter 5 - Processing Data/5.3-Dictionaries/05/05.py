# The following program displays the data for a requested nation from a text file called countries.dat

import pickle

def main():
  # Display the data for an individual country
  nations = getDictionary('countries.dat')
  nation = inputNameOfNation(nations)
  displayData(nations, nation)

def getDictionary(fileName):
  infile = open(fileName, 'rb') # rb: read binary
  nations = pickle.load(infile)
  infile.close()
  return nations

def inputNameOfNation(nations):
  nation = input('Enter the name of the country: ')
  while nation not in nations:
    print('Does not exist in countries.dat file.')
    nation = input('Enter the name of another country: ')
  return nation

def displayData(nations, nation):
  print(f'Continent: {nations[nation]['cont']}')
  print(f'Popultion: {nations[nation]['popl']} million people')
  print(f'Area: {nations[nation]['area']} square miles')

main()
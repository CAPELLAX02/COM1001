# The following program displays the countries and their population from a specified continent. The countries will be ordered by their populations.

import pickle

def main():
  # Display countries and their population from a specified continent.
  nations = getDictionary('countries.dat')
  continent = input('Enter the name of a continent other than Antarctica: ')
  continentDict = constructContinentNations(nations, continent)
  displaySortedResults(continentDict)

def getDictionary(fileName):
  infile = open(fileName, 'rb')
  nations = pickle.load(infile)
  infile.close()
  return nations

def constructContinentNations(nations, continent):
  # Reduce the dictionary to a dictionary consisting solely of the countries in the specified continent.
  continentDict = {}
  for i in nations:
    if nations[i]['cont'] == continent:
      continentDict[i] = nations[i]
  return continentDict

def displaySortedResults(dictionaryName):
  # Display coountries in descending order by population.
  continentList = sorted(dictionaryName.items(), key=lambda x : x[1]['popl'], reverse=True)
  for i in continentList:
    print('\t{0}: {1:,.2f}'.format(i[0], i[1]['popl']))

main()
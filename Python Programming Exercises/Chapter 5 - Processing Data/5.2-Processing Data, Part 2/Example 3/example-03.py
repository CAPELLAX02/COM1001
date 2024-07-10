# BU KODUN TAMAMINI DÜZGÜN BİR CSV DOSYASI İLE TEKRAR GÖZDEN GEÇİR!!!!

def main():
  # Do statistical analysis of country's areas.
  areasAsStrings = extractField('countries.txt', 4) # Place areas into a list
  areas = [eval(num) for num in areasAsStrings]
  displaySomeStatistics(areas)

def extractField(fileName, n):
  # Extract the nth field from each record of a CSV file and replace the data into a list.
  infile = open(fileName, 'r')
  return [line.rstrip().split(',')[n - 1] for line in infile]

def displaySomeStatistics(listOfNumbers):
  # Display the average, median, and standart deviation of the areas.
  average = sum(listOfNumbers) / len(listOfNumbers)
  median = calculateMedian(listOfNumbers)
  standartDeviation = calculateStandartDeviation(listOfNumbers, average)
  print('Average Area: {0:,.2f} square miles.'.format(average))
  print('Median Area: {0:,.1f} square miles.'.format(median))
  print('Standart Deviation: {0:,.2f} square miles.'.format(standartDeviation))

def calculateMedian(listOfNumbers):
  listOfNumbers.sort()
  if len(listOfNumbers) % 2 == 1:
    median = listOfNumbers[int(len(listOfNumbers) / 2)] # middle number
  else:
    # median will be the average of the two middle numbers
    m = int(len(listOfNumbers) / 2) # kalan önemli değil, tam kısım lazım. burada "m", bize ortadaki iki elemandan soldakinin indeksini verir.
    median = (listOfNumbers[m] + listOfNumbers[m + 1]) / 2
  return median

def calculateStandartDeviation(listOfNumbers, average):
  m = average
  n = len(listOfNumbers)
  listOfSquaresOfDeviations = [0] * n
  for i in range(n):
    listOfSquaresOfDeviations[i] = (listOfNumbers[i] - m) ** 2
  standartDeviation = (sum(listOfSquaresOfDeviations) / n) ** (0.5)
  return standartDeviation

main()

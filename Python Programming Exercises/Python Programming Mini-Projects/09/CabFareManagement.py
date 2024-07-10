def main():
  listOfDrives = createListOfDrives()
  displayResults(listOfDrives)


class Cab:
  def __init__(self, cabType='', numberOfKilometers=0.0):
    self.cabType = cabType
    self.numberOfKilometers = numberOfKilometers

  def setName(self, cabType):
    self.cabType = cabType

  def getName(self):
    return self.cabType
  
  def setKilometers(self, numberOfKilometers):
    self.numberOfKilometers = numberOfKilometers

  def getKilometers(self):
    return self.numberOfKilometers
  

class Sedan(Cab):
  def calculate(self):
    rate = 2.0
    return float(self.getKilometers()) * rate
  

class Hatchback(Cab):
  def calculate(self):
    rate = 1.5
    return float(self.getKilometers()) * rate
  

def createListOfDrives():
  listOfDrives = []
  carryOn = 'Y'

  while carryOn == 'Y':
    name = input('Enter cab type (Hatchback/Sedan): ').capitalize()

    if name != 'Sedan' and name != 'Hatchback':
      print('Please enter either Sedan or Hatchback.')
      continue

    kilometerTravelled = input('Enter the number of kilometers travelled: ')

    if name == 'Sedan':
      cab = Sedan(name, kilometerTravelled)
    elif name == 'Hatchback':
      cab = Hatchback(name, kilometerTravelled)

    listOfDrives.append(cab)
    
    carryOn = input('Do you want to continue (Y/N)? : ')
    carryOn = carryOn.upper()

  return listOfDrives


def displayResults(listOfDrives):
  print()
  
  totalFare = 0.0
  totalKilometers = 0.0

  print('----- List of Drives -----')

  for drive in listOfDrives:
    print(str(drive.getName())+ ' : ' +str(drive.getKilometers()) + ' kilometers')
  print('---------------------------')

  for drive in listOfDrives:
    totalKilometers += float(drive.getKilometers())

    if drive.getName() == 'Sedan':
      totalFare += drive.calculate()
    elif drive.getName() == 'Hatchback':
      totalFare += drive.calculate()

  print('Total number of kilometers drived by all Cabs: {0:,.2f}'.format(totalKilometers))
  print('Total Fare earned from al cabs ($): {0:,.2f}'.format(totalFare))


main()
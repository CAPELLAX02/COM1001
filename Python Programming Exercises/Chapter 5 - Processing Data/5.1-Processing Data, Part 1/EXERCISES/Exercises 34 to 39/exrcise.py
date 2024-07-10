def main():
  numberOfNumbers('Numbers.txt')
  findLargestAndSmallestNumbers('Numbers.txt')
  findTheLastNumber('Numbers.txt')
  Average('Numbers.txt')

def numberOfNumbers(fileName):
  infile = open(fileName, 'r')
  counter = 0
  for _ in infile:
    counter += 1
  infile.close()
  print('Number of numbers in Numbers.txt: ', counter)

def findLargestAndSmallestNumbers(fileName):
  infile = open(fileName, 'r')
  strNumbers = [line.rstrip() for line in infile]
  intNumbers = [int(number) for number in strNumbers]
  infile.close()
  print('Maximum number of the Numbers.txt: ', max(intNumbers))
  print('Minimum number of the Numbers.txt: ', min(intNumbers))

def findTheLastNumber(fileName):
  infile = open(fileName, 'r')
  numbers = [int(line.rstrip()) for line in infile]
  infile.close()
  print('Last Number of the Numbers.txt: ', numbers[-1])

def Average(fileName):
  infile = open(fileName, 'r')
  numbers = [int(line.rstrip()) for line in infile]
  avg = float(sum(numbers) / len(numbers))
  infile.close()
  print('Average of the numbers in Numbers.txt: ', avg)

main()

# OUTPUTS OF THE PROGRAM ABOVE:

# Number of numbers in Numbers.txt:  7
# Maximum number of the Numbers.txt:  8
# Minimum number of the Numbers.txt:  2
# Last Number of the Numbers.txt:  5
# Average of the numbers in Numbers.txt:  4.857142857142857
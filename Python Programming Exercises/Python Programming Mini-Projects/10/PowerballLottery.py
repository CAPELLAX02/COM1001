# In Powerball Lottery, often the five selected white balls contain two or more balls with consecutive numbers. 

# The following program simulates 100,000 selections of white balls and displays the percentage of times the selection contains at least two consecutive numbers.

import random


def main():
  total = 0

  for trial in range(100000):
    numbers = random.sample(range(1, 60), 5)
    numbers.sort()

    if two_consecutive(numbers):
      total += 1

  sentence = ' of the time there were at least two consecutive numbers in the set of five numbers.'

  print(('{0:.0%}' + sentence).format(total / 100000))


def two_consecutive(x):
  for index in range(0, 4):
    if x[index] + 1 == x[index + 1]:
      return True
    
    
main()
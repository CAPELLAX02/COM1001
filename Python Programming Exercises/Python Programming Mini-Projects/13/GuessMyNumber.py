# The following program randomly selects a number from 1 through 100 and asks the user to guess the number. At each guess the user should be told if the guess is proper, and if so, whether it is too high or too low. The user should be told of the number of guesses when finally guessing the correct number.

import random

attempt = 1
n = random.randint(1, 100)
print("\nI've thought a number from 1 through 100.")

while True:
  try:
    guess = int(input('Guess the number: '))
    break
  except ValueError:
    attempt += 1
    print('You did not enter a number.')

while guess != n:
  attempt += 1
  if (guess > 100) or (guess < 1):
    print('Number must be from 1 through 100.')
  elif guess > n:
    print('Too high.')
  elif guess < n:
    print('Too low')

  while True:
    try:
      guess = int(input('Try again: '))
      break
    except ValueError:
      attempt += 1
      print('You did not enter a number.')

print('Correct!', end=' ')
if attempt == 1:
  print('You got it in one guess!')
else:
  print(f'You took {attempt} guesses.')
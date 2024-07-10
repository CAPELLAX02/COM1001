import random

def main():
  ## Play three games of rock, paper, scissors.
  # Get names of contestants and instantiate and object for each.
  nameOfHuman = input('Enter the name of human: ')
  h = Human(nameOfHuman)
  nameOfComputer = input('Enter the name of computer: ')
  c = Computer(nameOfComputer)
  print()

  # Plat three games and keep score.
  for i in range(3):
    humanChoice = h.makeChoice()
    computerChoice = c.makeChoice()
    print(f'{c.getName()} chooses {computerChoice}')

    # Determine whether human wins.
    if humanChoice == 'rock':
      if computerChoice == 'scissors':
        h.incrementScore()
      elif computerChoice == 'paper':
        c.incrementScore()
    
    elif humanChoice == 'paper':
      if computerChoice == 'rock':
        h.incrementScore()
      elif computerChoice == 'scissors':
        c.incrementScore()

    else: # humanChoice == 'scissors
      if computerChoice == 'paper':
        h.incrementScore()
      elif computerChoice == 'rock':
        c.incrementScore()

    print(h, end=' ')
    print(c)

  if h.getScore() > c.getScore():
    print(h.getName().upper(), 'WINS!')
  elif c.getScore() > h.getScore():
    print(c.getName().upper(), 'WINS!')
  else:
    print('TIE!')


class Contestant():
  def __init__(self, name='', score=0):
    self.name = name
    self.score = score

  def getName(self):
    return self.name
  
  def getScore(self):
    return self.score
  
  def incrementScore(self):
    self.score += 1

  def __str__(self):
    return f'{self.name}: {self.score}'
  

class Human(Contestant): # Basic Inheritance Demonstration
  def makeChoice(self):
    choices = ['rock', 'paper', 'scissors']
    while True:
      choice = input(self.name + ', enter your choice: ')
      if choice.lower() in choices:
        break
    return choice.lower()
  

class Computer(Contestant): # Basic Inheritance Demonstration
  def makeChoice(self):
    choices = ['rock', 'paper', 'scissors']
    selection = random.choice(choices)
    return selection
  
  
main()
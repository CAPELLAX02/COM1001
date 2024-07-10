# The following program uses a class containing no mutator or accessor methods.

import random

def main():
  # Select a cart at random.
  c = Card()          # Create an instance of a Card object.
  c.selectAtRandom()  # Invokes the selectAtRandom method on the object c.
  print(c)            # Calls the __str__ method that displays the returned value.

class Card:
  def __init__(self, rank='', suit=''):
    self.rank = rank
    self.suit = suit

  def selectAtRandom(self):
    # Randomly select a rank and a suit.
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', "10", "jack", "queen", "king", "ace"]
    
    self.rank = random.choice(ranks)
    self.suit = random.choice(['spades', 'hearts', 'clubs', 'diamonds'])

  def __str__(self):
    return f'{self.rank} of {self.suit}'
  
main()
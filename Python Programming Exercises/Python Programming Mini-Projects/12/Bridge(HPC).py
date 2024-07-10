# A bridge consist of 13 cards. One way to evaluate a hand is to calculate the total high point count (HPC) where:

  # an ace (A) is worth 4 points, 
  # a king (K) is worth 3 points,
  # a queen (Q) is worth 2 points, and
  # a jack (J) is worth 1 point.

# The following program randomly selects 13 cards from a deck of cards and calculates HPC (high point count) for the hand using the pickled binary file named 'DeckOfCardsList.dat'.

import random
import pickle

def main():
  # Calculate the High Point Count (HPC) for a bridge hand.
  bridgeHand = getHand()
  print(', '.join(bridgeHand)) # Display the bridge hand.
  HPC = calculateHighCardPointCount(bridgeHand)
  print(f'High Point Count (HPC): {HPC}')


def getHand():
  infile = open('DeckOfCardsList.dat', 'rb')
  deckOfCards = pickle.load(infile)
  infile.close()

  bridgeHand = random.sample(deckOfCards, 13)

  return bridgeHand


def calculateHighCardPointCount(bridgeHand):
  countDict = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
  HPC = 0

  for card in bridgeHand:
    # Check if the card is '10' or other single digit rank
    rank = card[:-1] if card[-1] in '♠♥♦♣' else card[:-2]

    if rank in countDict:
      HPC += countDict[rank]

  return HPC


main()
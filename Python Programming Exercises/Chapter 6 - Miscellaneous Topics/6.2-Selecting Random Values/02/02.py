# The file DeckOfCardsList.dat is a pickled binary file containing a list of the 52 cards in an ordinary deck of playing cards. The following program randomly selects five cards from the deck.

import random
import pickle

infile = open('DeckOfCardsList.dat', 'rb')

deckOfCards = pickle.load(infile) # we've got a dictionary now.

infile.close()

pokerHand = random.sample(deckOfCards, 5)

print(pokerHand)
# OUTPUT: ['7♠', 'Q♠', 'K♦', 'Q♣', '5♦']
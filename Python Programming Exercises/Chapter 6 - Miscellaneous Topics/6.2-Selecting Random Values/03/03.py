#  American roulette wheels have 38 numbers (1 through 36 plus 0 and 00). Many different types of bets are possible. We shall consider the “odd” bet. When you bet $1 on “odd”, you win $1 if an odd number appears and you lose $1 otherwise. In the following program, the user specifies an amount of money, called the bankroll, to risk at the roulette table. He decides to bet $1 on each spin of the wheel and to quit when he doubles his bankroll or goes broke. The program simulates his session at the roulette table.

import random

def main():
  bankroll = int(input('Enter the amount of the bankroll ($): '))
  (amount, timesPlayed) = playDoubleOrNothing(bankroll)
  print(f'Ending bankroll: ${amount}')
  print(f'Number of games played: {timesPlayed}')

def isOdd(n):
  if (1 <= n <= 36) and (n % 2):
    return True
  else:
    return False
  
def profit(n):
  if isOdd(n):
    return 1
  else:
    return -1
  
def playDoubleOrNothing(bankroll):
  amount = bankroll
  timesPlayed = 0
  
  while 0 < amount < 2 * bankroll:
    # let 37 represent 00:
    n = random.randint(0, 37)
    timesPlayed += 1
    amount += profit(n)
  return (amount, timesPlayed)

main()
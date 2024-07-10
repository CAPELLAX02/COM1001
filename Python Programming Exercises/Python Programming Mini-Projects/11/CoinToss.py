# The following program displays the result of tossing a coin 32 times. Then determines if there is a run of five consecutive Head or a run of five consecutive Tails.

import random

coin = ['T', 'H']

result = ''

for i in range(32):
  result += random.choice(coin)

print(result)

if ('TTTTT' in result) or ('HHHHH' in result):
  print('There was a run of five consecutive same outcomes.')
else:
  print('There was no run of five consecutive same outcomes.')
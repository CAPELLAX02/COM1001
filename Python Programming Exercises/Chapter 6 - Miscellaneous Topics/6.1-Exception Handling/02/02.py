# The following program uses exception handling to guarantee a proper response from the user.

def main():
  # Request that the user enter a proper response.
  phoneticAlphabet = { 'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta' }
  
  while True:
    try:
      letter = input('Enter a, b, c, or d: ')
      print(phoneticAlphabet[letter])
      break
    except KeyError:
      print('unacceptable letter was entered.')

main()
    
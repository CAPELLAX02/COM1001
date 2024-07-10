# The following program displays the vowels contained in a word input by the user. The program uses a list-valued function.

def occuringWovels(word):
  word = word.upper()
  vowels = ('A', 'E', 'I', 'O', 'U')
  includedVowels = []

  for i in vowels:
    if (i in word) and (i not in includedVowels):
      includedVowels.append(i)

  print('The following vowels occur in the word: ', end='')
  for i in includedVowels:
    print(i, end=' ')

word = input('Enter a word: ')

occuringWovels(word)
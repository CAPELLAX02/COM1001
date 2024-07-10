# The following program uses a Boolean-valued function to determine whether a word input by the user is a vowel word. 

def isVowel(word):

  word = word.upper()

  vowels = ['A', 'E', 'I', 'O', 'U']

  for i in vowels:
    if i not in word:
      return False
  return True

word = input('Enter a word: ')

if isVowel(word):
  print(word, 'contains every vowel.')
else:
  print(word, 'does not contain every vowel.')
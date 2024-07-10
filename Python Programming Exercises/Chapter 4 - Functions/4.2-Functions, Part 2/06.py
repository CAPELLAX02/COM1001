# The following program sorts a list of words using each of three properties cited above.

def main():
  # Custom sort a list of keywords.
  list1 = ['democratic', 'sequoia', 'equals', 'brrr', 'break', 'two']

  list1.sort(key=len)
  print('Sorted list by length in ascending order:')
  print(list1, '\n')

  list1.sort(key=lastCharacter)
  print('Sorted by the last character in ascending order:')
  print(list1, '\n')

  list1.sort(key=numberOfVowels, reverse=True)
  print('Sorted by number of vowels in descending order:')
  print(list1, '\n')

def lastCharacter(word):
  return word[-1]

def numberOfVowels(word):
  vowels = ('a', 'e', 'i', 'o', 'u')
  total = 0
  for i in vowels:
    total += word.count(i)
  return total

main()
# The following program uses a recursive structrue to create a permutaion funtion.

def main():
  word = input('Enter a word: ')
  print(' '.join(permuations(word)))


def permuations(word):
  if len(word) == 1:
    return word
  
  listOfPermutaions = []

  for i in range(len(word)):
    restOfWord = word[: i] + word[i + 1:]
    z = permuations(restOfWord) # Recursion

    for j in z:
      listOfPermutaions.append(word[i] + j)

  return listOfPermutaions


main()
# COUNTING WORDS

def main():
  # Analyze word frequencies in the text file.
  listOfWords = formListOfWords('myText.txt')
  freq = createFrequencyDictionary(listOfWords)
  displayWordCount(listOfWords, freq)
  displayMostCommon(freq)

def formListOfWords(fileName):
  infile = open(fileName)
  originalLine = infile.readline().lower()

  # Remove punctuation marks from the line.
  line = ''
  for char in originalLine:
    if ('a' <= char <= 'z') or (char == ' '):
      line += char

  # Place the individual words into a list.
  listOfWords = line.split()
  return listOfWords

def createFrequencyDictionary(listOfWords):
  # Create dictionary with each item having the form word:frequency.
  freq = {}
  for word in listOfWords:
    freq[word] = 0
  for word in listOfWords:
    freq[word] += 1
  return freq

def displayWordCount(listOfWords, freq):
  print(f'The text file contains {len(listOfWords)} words')
  print(f'The text file contains {len(freq)} different words')
  print()

def displayMostCommon(freq):
  print('The most common words and their frequencies are shown below:')
  listOfMostCommonWords = []
  for word in freq.keys():
    if freq[word] >= 6:
      listOfMostCommonWords.append((word, freq[word]))    
  # Sorting the dictionary according to values:
  listOfMostCommonWords.sort(key=lambda x : x[1], reverse=True)
  for item in listOfMostCommonWords:
    print(f'\t{item[0]}: {item[1]}')

main()
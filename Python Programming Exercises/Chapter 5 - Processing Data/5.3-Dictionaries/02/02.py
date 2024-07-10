# The following program translates simple sentences into textese.

# DÜZGÜN ÇALIŞMIYOR ?!

def main():
  # Translate and English sentence into textese.
  texteseDict = createDictionary('Textese.txt')
  sentence = input('Enter a simple sentence in lowercase withot any punctuation: ')
  translate(sentence, texteseDict)

def createDictionary(fileName):
  infile = open(fileName, 'r')
  textList = [line.rstrip() for line in infile]
  infile.close()

  return dict([x.split(',') for x in textList])

def translate(sentence, texteseDict):
  words = sentence.split()
  for word in words:
    print(texteseDict.get(word, word) + " ", end="")

main()

# INPUT:   
# OUTPUT:  
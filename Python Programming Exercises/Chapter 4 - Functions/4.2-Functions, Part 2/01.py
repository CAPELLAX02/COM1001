# In the following program, the function firstPart calls the function secondPart. After the statements in secondPart are executed, the execution continues with the remaining statements in the function firstPart before returning to the function main.

def main():
  # Demonstrate functions calling other functions.
  firstPart()
  print(str(4) + ': from function main')

def firstPart():
  print(str(1) + ': from function firstPart')
  secondPart()
  print(str(3) + ': from function firstPart')

def secondPart():
  print(str(2) + ': from function secondPart')

main()

# OUTPUT
# 1: from function firstPart
# 2: from function secondPart
# 3: from function firstPart
# 4: from function main
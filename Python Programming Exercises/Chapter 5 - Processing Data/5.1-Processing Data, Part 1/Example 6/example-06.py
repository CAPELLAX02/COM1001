# the following program illustrates several set operations

def main():
  words = ['apple', 'apple', 'banana', 'banana']

  terms = set(words)
  print(terms) # {'apple', 'banana'}

  words = list(terms)
  print(words) # ['apple', 'banana']

  # Demonstrate the effect of the "add" method:
  terms.add('apple') # has no effect since "apple" was already in the set.
  terms.add('orange')
  print(terms) # {'apple', 'banana', 'orange'}

  # Demonstrate the effect of the "discard" method:
  terms.discard('apple')
  print(terms) # {'banana', 'orange'}

  # Convert the set to a tuple:
  words = tuple(terms)
  print(words)  # ('banana', 'orange')

main()
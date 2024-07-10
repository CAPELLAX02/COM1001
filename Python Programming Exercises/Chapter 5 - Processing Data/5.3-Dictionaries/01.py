# The following program illustrates many of the functions and methods for dictionaries.

def main():
  # Illustrate dictionary functions and methods.
  d = {}

  d['spam'] = 3

  print(d) # {'spam': 3}

  d.update({'spam' : 1, 'eggs' : 2}) 

  print(f'd has {len(d)} items.') # d has 2 items.

  print('eggs' in d) # True

  print(f'keys: {list(d.keys())}') # keys: ['spam', 'eggs']

  print(f'values: {list(d.values())}') # values: [1, 2]

  
  index = 0
  for key in d:
    print(f'key-{index} = {key}', end=' ; ')
    index += 1
  # key-0 = spam ; key-1 = eggs ;
  
  print(d.get('toast', 'not in dictionary')) # not in dictionary

  del(d['eggs'])

  print(d) # {'spam': 1}

main()
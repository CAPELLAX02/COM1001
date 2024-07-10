# The following program displays three verses of a well-known children’s song. In this case, the function prevents having to write repetitive code.

def oldMcDonald(animal, sound):
  print("Old McDonald had a farm. Eyi eyi oh.")
  print("And on his farm he had a", animal + ".", "Eyi eyi oh.")
  print("With a", sound, sound, "here, and a", sound, sound, "there.")
  print("Here a", sound + ",", "there a", sound + ",", "everywhere a", sound, sound + ".")
  print("Old McDonald had a farm. Eyi eyi oh.")

oldMcDonald('LAMB', 'BEA')
print()
oldMcDonald('DUCK', 'QUACK')
print()
oldMcDonald('COW', 'MOO')
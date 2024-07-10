# The following program sorts names by their surnames. The second line sorts the list of names, and the last two lines display the contents of the sorted list.

names = ['Lebron James', 'Stephan Curry', 'Kobe Bryant', 'Micheal Jordan']

names.sort(key=lambda name : name.split()[-1])

nameString = ', '.join(names)

print(nameString)
# Kobe Bryant, Stephan Curry, Lebron James, Micheal Jordan
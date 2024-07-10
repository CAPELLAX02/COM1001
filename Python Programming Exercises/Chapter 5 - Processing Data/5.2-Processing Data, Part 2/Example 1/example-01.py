def main():
  # Display the countries in a specified continent
  continent = input('Enter a name of a continent: ')
  continent = continent.title()
  if continent != 'Antarctica':
    infile = open('countries.txt', 'r')
    for line in infile:
      data = line.split(',') # data = [country, continent, population, area] is constructed.
      if data[1] == continent:
        print(data[0])
  else:
    print('There are no countries in Antarctica.')

main()
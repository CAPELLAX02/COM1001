# We will run the following program with different assumptions.

def main():
  # Display the reciprocal of number in a file.
  try:
    fileName = input('Enter the name of a file: ')
    infile = open(fileName, 'r')
    num = float(infile.readline())
    print(1 / num)
  except FileNotFoundError:
    print(f'There is no file named {fileName}')
  except ValueError:
    print("Opps, ValueError! You're probaby trying to converting some string to integer or something.'")
  except ZeroDivisionError:
    print('You cannot divide a number by zero!')
  
main()
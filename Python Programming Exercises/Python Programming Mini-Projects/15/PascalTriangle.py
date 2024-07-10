# The following program prompts the user for a nonnegative integer number n and then displays the numbers in the n^th row of the triangle.

def main():
  ## Display the line of Pascal's triangle.
  n = int(input('Enter a nonnegative integer: '))
  line = [str(x) for x in pascal(n)]
  print(f'Row-{n}: ' + ' '.join(line))

def pascal(n):
  # Display the nth line of Pascal's triangle.
  if n == 0:
    return [1]
  else:
    line = [1]
    previousLine = pascal(n - 1)
    for i in range(len(previousLine) - 1):
      line.append(previousLine[i] + previousLine[i + 1])
    line += [1]
  return line

main()
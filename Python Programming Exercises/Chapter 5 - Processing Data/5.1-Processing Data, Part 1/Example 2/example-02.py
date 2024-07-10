def main():
  # Create two files containing the first three presedents
  outfile = open('FirstPresidents2.txt', 'w')
  createWithWritelines(outfile)
  outfile = open('FirstPresidents3.txt', 'w')
  createWithWrite(outfile)
  
def createWithWritelines(outfile):
  list1 = ['George Washington', 'John Adams', 'Thomas Jefferson']
  # Append endline characters to the list's items
  for i in range(len(list1)):
    list1[i] = list1[i] + '\n'
  # Write the list's items to the file
  outfile.writelines(list1)
  outfile.close()

def createWithWrite(outfile):
  outfile.write('George Washington\n')
  outfile.write('John Adams\n')
  outfile.write('Thomas Jefferson\n')
  outfile.close()

main()

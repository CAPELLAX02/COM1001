# The following function creates a list of both types of students and uses the list to display the names of the students and their semester grades, where the names are displayed in alphabetical order. Assume that the class definitions in Example 1 are contained in the file student.py.

import student

def main():
  listOfStudents = obtainListOfStudents()
  displayResults(listOfStudents)


def obtainListOfStudents():
  listOfStudents = []
  carryOn = 'Y'

  while carryOn == 'Y':
    name = input("Enter student's name: ")
    midterm = float(input("Enter student's grade on midterm exam: "))
    final = float(input("Enter student's grade on final exam: "))

    category = input("Enter the category (LG or PF): ")

    if category.upper() == 'LG':
      st = student.LGStudent(name, midterm, final)
    
    else:
      st = student.PFstudent(name, midterm, final)

    listOfStudents.append(st)
    
    carryOn = input('Do you want to continue (Y/N)? ')
    carryOn = carryOn.upper()

  return listOfStudents


def displayResults(listOfStudents):
  print('\nNAME\tGRADE')
  listOfStudents.sort(key=lambda x : x.getName()) # Sort students by name.

  for pupil in listOfStudents:
    print(pupil)


main()

# EXAMPLE INPUT
# Enter student's name: Bob
# Enter student's grade on midterm exam: 79
# Enter student's grade on final exam: 85
# Enter the category (LG or PF): LG
# Do you want to continue (Y/N)? Y
# Enter student's name: Alice
# Enter student's grade on midterm exam: 92
# Enter student's grade on final exam: 96
# Enter the category (LG or PF): pF
# Do you want to continue (Y/N)? y
# Enter student's name: Carol
# Enter student's grade on midterm exam: 75
# Enter student's grade on final exam: 76
# Enter the category (LG or PF): Lg
# Do you want to continue (Y/N)? N

# EXAMPLE OUTPUT
# NAME    GRADE
# Alice   Pass
# Bob     B
# Carol   C
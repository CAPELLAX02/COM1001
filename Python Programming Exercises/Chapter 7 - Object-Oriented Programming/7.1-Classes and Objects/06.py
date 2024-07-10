# In the following program, assume that the class LGstudent has been stored in the file lgStudent.py

import lgStudent

def main():
  # Calculate and display several students' semester letter grades.
  listOfStudents = []
  carryOn = 'Y'

  while carryOn == 'Y':
    # Obtain student's name, midterm grade and final grade.
    name = input("Enter student's name: ")
    midterm = float(input("Enter student's midterm grade: "))
    final = float(input("Enter student's final grade: "))

    # Create an instance of an LGstudent object.
    student1 = lgStudent.LGstudent(name, midterm, final)
    listOfStudents.append(student1)
    carryOn = input('Do you want to continue (Y/N)? ')
    carryOn = carryOn.upper()

  print('NAME\tGRADE')

  # Display students, names, and semester letter grades.
  for pupil in listOfStudents:
    print(pupil)

main()

# EXAMPLE INPUT:
# Enter student's name: John
# Enter student's midterm grade: 56
# Enter student's final grade: 74
# Do you want to continue (Y/N)? Y
# Enter student's name: Bruce
# Enter student's midterm grade: 72
# Enter student's final grade: 66
# Do you want to continue (Y/N)? y
# Enter student's name: Sue    
# Enter student's midterm grade: 66
# Enter student's final grade: 88
# Do you want to continue (Y/N)? n

# EXAMPLE OUTPUT
# NAME    GRADE
# John    D
# Bruce   D
# Sue     C
# The following program uses a class containing no accessor methods. The program requests a student’s name and two grades, and then calculates the letter grade for the semester. The “LG” at the beginning of the class name signifies that the student is registered to receive a letter grade at the end of the semester.

def main():
   # Calculate and display a student's semester letter grade,
   # and obtain student's name, grade on midterm exam, and grade on final.
  name = input("Enter student's name: ")
  midterm = float(input("Enter student's grade on midterm exam: "))
  final = float(input("Enter student's grade on final exam: "))
  
  # Create an instance of an LGstudent object.
  student1 = LGstudent(name, midterm, final)
  print('\nNAME\tGRADE')

  # Display student's name and semester letter grade.
  print(student1)


class LGstudent:
  def __init__(self, name='', midterm=0, final=0):
    self.name = name
    self.midterm = midterm
    self.final = final

  def setName(self, name):
    self.name = name

  def setMidterm(self, midterm):
    self.midterm = midterm

  def setFinal(self, final):
    self.final = final

  def calculateSemesterGrade(self):
    average = (self.midterm + self.final) / 2
    average = round(average, 2)

    if average >= 90:
      return 'A'
    elif average >= 80:
      return 'B'
    elif average >= 70:
      return 'C'
    elif average >= 60:
      return 'D'
    else:
      return 'F'
    
  def __str__(self):
    return f'{self.name}\t{self.calculateSemesterGrade()}'
  

main()

# OUTPUT EXAMPLE:
# NAME    GRADE
# Josh    C
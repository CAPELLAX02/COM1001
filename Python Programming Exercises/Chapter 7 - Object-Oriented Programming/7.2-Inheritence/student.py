# (This is the 01.py file actually.)

# Specify that LGstudent and PFstudent are subclasses of the superclass Student and inherit all the properties and methods of the class Student. Students in the class PFstudent receive either Pass or Fail as their semester grades.

class Student:
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

  def getName(self):
    return self.name
  
  def __str__(self):
    return self.name + "\t" + self.calcSemGrade()
  

class LGStudent(Student):
  def calcSemGrade(self):
    average = round((self.midterm + self.final) / 2)

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


class PFstudent(Student):
  def calcSemGrade(self):
    average = round((self.midterm + self.final) / 2)
    if average >= 60:
      return "Pass"
    else:
      return "Fail"
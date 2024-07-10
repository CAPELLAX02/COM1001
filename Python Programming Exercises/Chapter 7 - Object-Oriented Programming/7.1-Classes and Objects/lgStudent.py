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
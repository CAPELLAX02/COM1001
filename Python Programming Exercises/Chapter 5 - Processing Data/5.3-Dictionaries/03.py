# A program with a long if-elif statement can be simplified with the use of a dictionary. Consider the following program that calculates an admission fee.

def main():
  # Determine an admission fee based on age group.
  ageGroup = input("Enter the person's age group (child, minor, adult, or senior): ")
  print(f'The admission fee is ${determineAdmissionFee(ageGroup)}')

def determineAdmissionFee(ageGroup):
  if ageGroup == "child":
    return 0 
  elif ageGroup == "minor":
    return 5 
  elif ageGroup == "adult":
    return 10
  elif ageGroup == "senior":
    return 8
  
main()

# The rewrite of the determineAdmissionFee function below, replaces the if-elif statement with a dictionary

def determineAdmissionFeeWithDictionary(ageGroup):
  myDict = {'child': 0, 'minor': 5, 'adult': 10, 'senior': 8}
  return myDict[ageGroup]


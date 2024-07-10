def firstName(fullName):
  firstSpace = fullName.index(" ")
  givenName = fullName[:firstSpace]
  return givenName
## Extract the first name from a full name.
fullName = input("Enter a person's full name: ")
print("First name:", firstName(fullName))
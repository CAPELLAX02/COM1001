# The following function uses recursion to determine whether or not a word containing no punctuation is a palindrome.

def isPalindrome(word):
  word = word.lower()

  if len(word) <= 1:
    return True
  
  elif word[0] == word[-1]: # First and last letters match.
    word = word[1: -1] # Remove first and last letters.
    return isPalindrome(word) # Proceed with recursion.
  
  else:
    return False
  
myInput = input('Enter a word to check if it is palindrome: ')

print(isPalindrome(myInput))
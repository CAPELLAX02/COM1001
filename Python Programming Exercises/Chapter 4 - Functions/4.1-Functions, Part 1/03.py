def triple(num):
  num = 3 * num   # functional scope
  return num

num = 2   # global scope

print(num)
print(triple(num))
# Power Function structured with ITERATION

def power(r, n):
  # iterative definition of power function:
  value = 1
  for i in range(1, n + 1):
    value *= r
  return value

print(power(3, 4))  # 81
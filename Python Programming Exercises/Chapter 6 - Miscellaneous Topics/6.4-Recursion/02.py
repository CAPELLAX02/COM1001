# Power Function structured with RECURSION

def power(r, n):
  # recursive definition of power function:
  if n == 1:
    return r
  else:
    return r * power(r, n - 1)
  
print(power(3, 4))  # 81
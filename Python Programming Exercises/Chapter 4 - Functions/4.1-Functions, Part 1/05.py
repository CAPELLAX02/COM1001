def futureValue(p, r, m, t):
  # p principal, the amount deposited
  # r annual rate of interest in decimal form
  # m number of times interest is compounded per year
  # t number of years
  i = r / m # interest rate per period
  n = m * t # total number of times interest is compounded
  amount = p * ((1 + i) ** n)
  return amount

p = eval(input('Enter amount deposited: '))
r = eval(input("Enter annual rate of interest in decimal form: "))
m = eval(input("Enter number of times interest is compounded per year: "))
t = int(input("Enter number of years: "))

balance = futureValue(p, r, m, t)
print('Balance after {0} years: ${1:,.2f}'.format(t, balance))
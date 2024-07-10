# The balanceAndInterest function in the following program returns a tuple giving values associated with a deposit into a savings account.

INTEREST_RATE = 0.04 # annual rate of interest

def main():
  principal = eval(input('Enter the amount of the deposit: '))
  numberOfYears = eval(input('Enter the number of years: '))

  bal, intEarned = balanceAndInterest(principal, numberOfYears)

  print('Balance: ${0:,.2f}\nInterest Earned: ${1:,.2f}'
        .format(bal, intEarned))
  
def balanceAndInterest(prin, numYears):
  balance = prin * ((1 + INTEREST_RATE) ** numYears)
  interestEarned = balance - prin

  return balance, interestEarned

main()
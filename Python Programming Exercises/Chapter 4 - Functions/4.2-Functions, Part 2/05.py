# The following program shows several ways to pass values when calculating the balance in a savings account given the principal, number of years, and the annual rate of interest, with interest compounded annually. The formula used is as follows:

# BALANCE = PRINCIPAL * ((1 + INTEREST_RATE) ** NUMBER_OF_YEARS)

def main():
  # Demonstrate the passing of values.
  print('Balance:')
  print('${0:,.2f}'.format(balance(1000, 5)))
  print('${0:,.2f}'.format(balance(1000, 5, .04)))
  print('${0:,.2f}'.format(balance(1000, intRate=.04, numYears=5)))
  print('${0:,.2f}'.format(balance(numYears=5, principal=1000)))
  print()
  print('${0:,.2f}'.format(balance(1000, 5, .03)))
  print('${0:,.2f}'.format(balance(1000, intRate=.03, numYears=5)))
  print('${0:,.2f}'.format(balance(intRate=.03, numYears=5, principal=1000)))
  print('${0:,.2f}'.format(balance(numYears=5, intRate=.03, principal=1000)))


def balance(principal, numYears, intRate = .04):
  return principal * ((1 + intRate) ** numYears)

main()

# OUTPUT
# Balance:
# $1,216.65
# $1,216.65
# $1,216.65
# $1,216.65

# $1,159.27
# $1,159.27
# $1,159.27
# $1,159.27
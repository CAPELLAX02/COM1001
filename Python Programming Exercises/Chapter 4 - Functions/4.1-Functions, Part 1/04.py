def pay(wage, hours):

  # Calculate weekly pay with time-and-a-half for overtime
  if hours <= 40:
    amount = wage * hours
  else:
    amount = (wage * 40) + (1.5 * wage * (hours - 40))

  return amount

## Calculate a person's weekly pay.
hourlyWage = eval(input("Enter the hourly wage: "))
hoursWorked = eval(input("Enter the number of hours worked: "))
earnings = pay(hourlyWage, hoursWorked)
print("Earnings: ${0:,.2f}".format(earnings))
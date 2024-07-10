def main():
  account = SavingAccount()
  name = input("Enter person's name: ")
  account.setName(name)
  print('D = Deposit\nW = Withdrawal\nQ = Quit')
  request = input('Enter your request (D, W, or Q): ').upper()
  while True:
    if request == 'D':
      amount = float(input('Enter amount to deposit: '))
      account.makeDesposit(amount)
      print('Balance: ${0:,.2f}'.format(account.getBalance()))
      request = input('Enter your request (D, W, or Q): ').upper()
    elif request == 'W':
      amount = float(input('Enter amount to withdraw: '))
      account.makeWithdrawal(amount)
      print('Balance: ${0:,.2f}'.format(account.getBalance()))
      request = input('Enter your request (D, W, or Q): ').upper()
    elif request == 'Q':
      print(f'End of transactions. Have a good day, {account.getName()}!')
      break
    else:
      request = input('Invalid request. Please press D, W, or Q: ')

class SavingAccount:
  def __init__(self, name='', balance=0.0):
    self.name = name
    self.balance = balance

  def setName(self, name):
    self.name = name
  
  def getName(self):
    return self.name
  
  def setBalance(self, balance):
    self.balance = balance

  def getBalance(self):
    return self.balance
  
  def makeDesposit(self, amount):
    self.balance += amount

  def makeWithdrawal(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print('Insufficient funds, transaction denied.')

main()
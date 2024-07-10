from tkinter import *

def makeChange():
  amount = int(AMOUNT.get())
  remainder = amount
  quarters = remainder // 25
  remainder %= 25
  dimes = remainder // 10
  remainder %= 10
  nickels = remainder // 5
  remainder %= 5
  cents = remainder
  QUARTERS.set(str(quarters))
  NICKELS.set(str(nickels))
  DIMES.set(str(dimes))
  CENTS.set(str(cents))

window = Tk()
window.title('Change')

caption = 'Amount: '
Label(window, text=caption).grid(row=0, column=1, sticky=E)

AMOUNT = StringVar()
entAmount = Entry(window, width=5, textvariable=AMOUNT)
entAmount.grid(row=0, column=2, sticky=W)

caption = 'Determine Composition of Change'
btn = Button(window, text=caption, command=makeChange)
btn.grid(row=1, column=0, columnspan=4, padx=20, pady=10)

Label(window, text='Quarters: ').grid(row=2, column=0, sticky=E)
Label(window, text='Nickels: ').grid(row=3, column=0, sticky=E)
Label(window, text='Dimes: ').grid(row=2, column=2, sticky=E)
Label(window, text='Cents: ').grid(row=3, column=2, sticky=E)

QUARTERS = StringVar()
entQuarters = Entry(window, width=4, state='readonly', textvariable=QUARTERS)
entQuarters.grid(row=2, column=1, sticky=W)

NICKELS = StringVar()
entNickels = Entry(window, width=4, state='readonly',textvariable=NICKELS)
entNickels.grid(row=3, column=1, sticky=W)

DIMES = StringVar()
entDimes = Entry(window, width=4, state='readonly', textvariable=DIMES)
entDimes.grid(row=2, column=3, sticky=W)

CENTS = StringVar()
entCents = Entry(window, width=4, state='readonly', textvariable=CENTS)
entCents.grid(row=3, column=3, sticky=W)

window.mainloop()
from tkinter import *

def add():
  num1 = eval(FIRST.get())
  num2 = eval(SECOND.get())
  sum = num1 + num2
  RESULT.set('Sum: ' + str(sum))

def substract():
  num1 = eval(FIRST.get())
  num2 = eval(SECOND.get())
  difference = num1 - num2
  RESULT.set('Difference: ' + str(difference))

def multiply():
  num1 = eval(FIRST.get())
  num2 = eval(SECOND.get())
  product = num1 * num2
  RESULT.set('Product: ' + str(product))

window = Tk()
window.title('Calculator GUI')

Label(window, text='First\nNumber:').grid(row=0, column=0)
Label(window, text='Second\nNumber:').grid(row=0, column=2)

FIRST = StringVar()
entFirst = Entry(window, width=5, textvariable=FIRST)
entFirst.grid(row=1, column=0)

SECOND = StringVar()
entSecond = Entry(window, width=5, textvariable=SECOND)
entSecond.grid(row=1, column=2)

btnAdd = Button(window, text='+', width=3, command=add)
btnAdd.grid(row=0, column=1, padx=15, pady=5)

btnSubstract = Button(window, text='-', width=3, command=substract)
btnSubstract.grid(row=1, column=1, padx=15, pady=5)

btnMultiply = Button(window, text='x', width=3, command=multiply)
btnMultiply.grid(row=2, column=1, padx=15, pady=5)

RESULT = StringVar()
entResult = Entry(window, state='readonly', width=20, textvariable=RESULT)
entResult.grid(row=3, column=0, columnspan=3, padx=40, pady=5)

window.mainloop()
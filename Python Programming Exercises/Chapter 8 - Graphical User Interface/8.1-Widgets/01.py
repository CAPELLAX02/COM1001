from tkinter import *

def changeColor():
  if btnCalculate['bg'] == 'blue':
    btnCalculate['bg'] = 'red'
  else:
    btnCalculate['bg'] = 'blue'

window = Tk()

window.title('Button')

btnCalculate = Button(window, text='Change Color',fg='yellow', bg='blue', command=changeColor)

btnCalculate.grid(padx=100, pady=15)

window.mainloop()
from tkinter import *

def honorsFunction():
  gpa = float(GPA.get())
  
  if gpa >= 3.9:
    honor = ' summa cum laude.'
  elif gpa >= 3.6:
    honor = ' magna cum laude.'
  elif gpa >= 3.3:
    honor = ' cum laude.'
  else:
    honor = ''

  HONORS.set(f'You graduated {honor}')

window = Tk()
window.title('Graduation Honors')

caption = 'GPA (2 through 4):'
Label(window, text=caption).grid(row=0, column=0, pady=5, sticky=E)

GPA = StringVar()
entryGPA = Entry(window, width=4, textvariable=GPA)
entryGPA.grid(row=0, column=1, padx=5, sticky=W)

btn = Button(text='Determine Honors', command=honorsFunction)
btn.grid(row=1, column=0, columnspan=2, padx=100)

HONORS = StringVar()
entryHONORS = Entry(window, state='readonly', width=36, textvariable=HONORS)
entryHONORS.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
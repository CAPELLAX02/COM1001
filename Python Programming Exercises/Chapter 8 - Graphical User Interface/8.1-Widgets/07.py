from tkinter import *

def sortItems(event):
  L.sort()
  conOFlstColors.set(tuple(L))

window = Tk()
window.title('Colors')

L = ['red', 'blue', 'green', 'light gray', 'cyan', 'purple', 'orange', 'yellowgreen', 'black', 'white']

conOFlstColors = StringVar()

lstColors = Listbox(window, width=10, height=5, listvariable=conOFlstColors)
lstColors.grid(padx=100, pady=20)

conOFlstColors.set(tuple(L))

lstColors.bind('<Button-3>', sortItems)

window.mainloop()
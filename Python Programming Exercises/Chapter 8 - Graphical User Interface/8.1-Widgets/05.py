from tkinter import *

window = Tk()
window.title('Colors')

L = ['red', 'yellow', 'light blue', 'orange', 'cyan', 'green']

conOFlstColors = StringVar() # contents of the list box

lstColor = Listbox(window, width=12, height=5, listvariable=conOFlstColors)

lstColor.grid(padx=100, pady=20)

conOFlstColors.set(tuple(L))

window.mainloop()
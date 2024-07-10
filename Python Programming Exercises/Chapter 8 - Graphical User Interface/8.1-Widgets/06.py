from tkinter import *

def changeBackgroundColor(event):
  lstColors['bg'] = lstColors.get(lstColors.curselection())

window = Tk()
window.title('Colors')

L = ['red', 'blue', 'green', 'light gray', 'cyan', 'purple', 'orange', 'yellowgreen', 'black', 'white']

conOFlstColors = StringVar()

lstColors = Listbox(window, width=10, height=5, listvariable=conOFlstColors)
lstColors.grid(padx=120, pady=30)

conOFlstColors.set(tuple(L))

lstColors.bind('<<ListboxSelect>>', changeBackgroundColor)

window.mainloop()
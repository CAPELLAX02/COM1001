from tkinter import *

def convertToUpperCase(event):
  conOFentName.set(conOFentName.get().upper())

window = Tk()
window.title('Entry Widget')
conOFentName = StringVar() # contents of Entry widget
entName = Entry(window, textvariable=conOFentName)
entName.grid(padx=100, pady=15)
entName.bind('<Button-1>', convertToUpperCase) # on left click
window.mainloop()
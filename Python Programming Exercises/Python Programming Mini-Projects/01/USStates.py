from tkinter import *

window = Tk()
window.title('States')

infile = open('states.txt', 'r')

listOfStates = [line.split(',')[0] + ' (' + line.split(',')[2] + ')' for line in infile]

infile.close()

conOFlstStates = StringVar()

lstStates = Listbox(window, height=10, width=30, listvariable=conOFlstStates)
lstStates.grid(row=1, column=0, padx=40, pady=5)

conOFlstStates.set(tuple(listOfStates))

window.mainloop()
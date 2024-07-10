from tkinter import *

def changeColor(event): 
  if entName["fg"] == "blue":
    entName["fg"] = "red"
  else:
    entName["fg"] = "blue"

window = Tk()

window.title('Entry Widget')

entName = Entry(window, fg='blue')

entName.grid(padx=100, pady=20)

entName.bind('<Button-3>', changeColor) # specify right-click as an event

window.mainloop()
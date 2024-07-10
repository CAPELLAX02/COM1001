from tkinter import *

window = Tk()

window.title('ReadOnly Entry Widget')

conOFentOutput = StringVar() # contents of widget

entOutput = Entry(window, state='readonly', textvariable=conOFentOutput)

entOutput.grid(padx=100, pady=20)

conOFentOutput.set('Hello World!')

window.mainloop()
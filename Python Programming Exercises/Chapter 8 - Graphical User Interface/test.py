# from tkinter import *
# window = Tk()
# window.mainloop()

from tkinter import *
window = Tk()
window.title("Button")
btnCalculate = Button(window, text="Calculate", bg="light blue")
btnCalculate.grid(padx=75, pady=15)
window.mainloop()
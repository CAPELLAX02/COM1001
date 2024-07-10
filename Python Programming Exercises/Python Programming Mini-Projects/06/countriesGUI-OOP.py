from tkinter import *
import pickle

class Nations:
  def __init__(self):
    window = Tk()
    window.title('Countries')

    infile = open('countries.dat', 'rb')
    self.nationDictionary = pickle.load(infile)
    infile.close()

    self.nationList = list((self.nationDictionary).keys())
    self.nationList.sort()
    self.NATIONS = StringVar()

    yscroll = Scrollbar(window, orient=VERTICAL)
    yscroll.grid(row=0, column=1, rowspan=7, sticky=NS)

    self.lstNations = Listbox(window, height=10, width=30, listvariable=self.NATIONS, yscrollcommand=yscroll.set)
    self.lstNations.grid(row=0, column=0,padx=10, pady=5, rowspan=7, sticky=NSEW)

    self.NATIONS.set(tuple(self.nationList))

    self.lstNations.bind('<<ListboxSelect>>', self.displayData)

    yscroll['command'] = self.lstNations.yview

    Label(window, text='Continent:').grid(row=0, column=3, padx=4, sticky=E)
    Label(window, text='Population:').grid(row=1, column=3, padx=4, sticky=E)
    Label(window, text='Area (sq. miles):').grid(row=2, column=3, padx=4, sticky=E)

    self.CONTINENT = StringVar()
    self.POPULATION = StringVar()
    self.AREA = StringVar()

    entContinent = Entry(window, width=20, state='readonly', textvariable=self.CONTINENT)
    entContinent.grid(row=0, column=4,padx=10, pady=5, sticky=W)

    entPopulation = Entry(window, width=20, state='readonly', textvariable=self.POPULATION)
    entPopulation.grid(row=1, column=4,padx=10, pady=5, sticky=W)

    entArea = Entry(window, width=20, state='readonly', textvariable=self.AREA)
    entArea.grid(row=2, column=4, padx=10, pady=5, sticky=W)

    window.mainloop()


  def displayData(self, event):
    nation = self.lstNations.get(self.lstNations.curselection())
    self.CONTINENT.set(self.nationDictionary[nation]['cont'])
    self.POPULATION.set('{0:,.0f}'.format(1000000 * float(self.nationDictionary[nation]['popl'])))
    self.AREA.set('{0:,.0f}'.format(self.nationDictionary[nation]['area']))

Nations()
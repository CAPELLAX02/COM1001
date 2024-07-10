from tkinter import *

def films(e):
    # Get the selected genre
    selection = lstGenres.curselection()
    if selection:
        genre = lstGenres.get(selection[0])
        # Open the Oscars.txt file and find films for the selected genre
        with open('Oscars.txt', 'r') as infile:
            films_for_genre = [line.split(', ')[1:] for line in infile if line.strip().startswith(genre)]
        # Flatten the list of films and remove new line characters
        F = [film.strip() for sublist in films_for_genre for film in sublist]
        # Update the list of films
        lstFilms.delete(0, END)  # Clear the listbox before adding new items
        for film in F:
            lstFilms.insert(END, film)

window = Tk()
window.title("Academy Award Winners")

# Swap the labels for genres and films
Label(window, text="FILMS").grid(row=0, column=0)
Label(window, text="GENRES").grid(row=0, column=1)

# Open the Oscars.txt file and read the contents
infile = open("Oscars.txt", "r")
# Create a set of genres
genreSet = {line.split(',')[0].strip() for line in infile}
infile.close()

# Convert the set to a sorted list
L = list(genreSet)
L.sort()

# Create a StringVar for films instead of genres
FILMS = StringVar()
lstFilms = Listbox(window, width=45, listvariable=FILMS)
lstFilms.grid(row=1, column=0, padx=10, sticky=NSEW)

# Create a scrollbar for the list of films
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=1, column=2, sticky=NS)
yscroll['command'] = lstFilms.yview
lstFilms['yscrollcommand'] = yscroll.set

# Create a StringVar for genres instead of films
GENRES = StringVar()
lstGenres = Listbox(window, width=10, height=len(L), listvariable=GENRES)
lstGenres.grid(row=1, column=1, sticky=N)
GENRES.set(tuple(L))
lstGenres.bind('<<ListboxSelect>>', films)

window.mainloop()

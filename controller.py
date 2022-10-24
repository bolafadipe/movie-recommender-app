from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
import view2

def genre_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Great choice',
        message=f'You selected {view2.selected_genre.get()}!'
    )
ttk.combobox.bind('<<ComboboxSelected>>', genre_changed)
if __name__ == '__main__':
    genre_changed(event)
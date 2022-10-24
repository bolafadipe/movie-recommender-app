import tkinter as tk
from tkinter import TclError, ttk
from tkinter.messagebox import showinfo


def create_header_frame(container):
    frame = ttk.Frame(container, width=200, height=100,border=10, borderwidth=5,relief='raised', padding=5)

    # grid layout for the input frame
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=3)
    

    header_label = ttk.Label(frame, text='What movie would you love to watch tonight? Choose a movie genre from the drop down below')
    #header_label.grid(column=3, row=0, columnspan=1)
    header_label.pack(fill='both')

    
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_genres_frame(container):
    global selected_genre
    global keepgenres
    frame = ttk.Frame(container)

    # configure frame rows and columns
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=3)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    genres = ['Drama', 'Crime', 'Action', 'Biography', 'Adventure', 'Comedy',
       'Animation', 'Horror', 'Western', 'Mystery', 'Film-Noir']

    # grid layout for the input frame
    # frame.rowconfigure(0, weight=1)
    # frame.rowconfigure(1, weight=3)

    # create genre dropdown
    ttk.Label(frame, text='please select a genre:').grid(row=0, column=0)
    value = tk.StringVar()
    keepgenres = value.get() # to persists the values for the Stringvar method
    selected_genre = ttk.Combobox(frame, textvariable=keepgenres, state='readonly', values=genres)
    #selected_genre.current(0)
    selected_genre.grid(row=1, column=1, columnspan=1, sticky='W')
    selected_genre.current(0)
    

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_movies_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    window = tk.Tk()
    #window.resizable(0, 0)
    window.title('Movie Recommender App')
    window.geometry('600x400')

    # layout on the window window
    window.rowconfigure(0, weight=1,)
    window.rowconfigure(1, weight=2)
    window.rowconfigure(2, weight=5)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.columnconfigure(4, weight=1)
    window.columnconfigure(5, weight=1)
    
    
    header_frame = create_header_frame(window)
    header_frame.grid(column=0, row=0, columnspan=5, sticky='N')

    input_frame = create_genres_frame(window)
    input_frame.grid(column=0, columnspan=1, row=1)

    output_frame = create_movies_frame(window)
    output_frame.grid(column=1, row=2)

    window.mainloop()


def genre_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Great choice',
        message=f'You selected {keepgenres.get()}!'
    )
selected_genre.bind('<<ComboboxSelected>>', genre_changed)

if __name__ == "__main__":
    create_main_window()

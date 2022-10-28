from tkinter import *
from tkinter import ttk


window = Tk()

# configure root window
window.title('Movie Recommender App')
window.geometry('900x600')
window.resizable(0, 0)

# create abd configure window grids
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# create the frame objects
input_frame = ttk.Frame(window)
input_frame.grid(column=1, row=0, columnspan=3)
labl = Label(input_frame, fg='#000', text='hello').pack()

output_frame = ttk.Frame(window)
output_frame.grid(column=0, row=0, columnspan=9)
labl2 = Label(output_frame, fg='#253ecd', text='this is for output').pack()






window.mainloop()
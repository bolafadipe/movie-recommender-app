from tkinter import *
from tkinter import ttk


window = Tk()

window.title('Movie Recommender App')
window.geometry('900x600')

# create the frame objects

input_frame = ttk.Frame(window)
input_frame.grid(column=1, row=0, columnspan=3)
labl = Label(input_frame, fg='#000', text='hello').pack()

output_frame = ttk.Frame(window)
output_frame.grid(column=0, row=0, columnspan=9)
labl2 = Label(output_frame, fg='#253ecd', text='this is for output').pack()






window.mainloop()
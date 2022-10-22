from tkinter import *
import test2

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        #self.init_window()

    button = tk.Button(text='click')


root = Tk()
root.geometry("400x300")
if __name__ == '__main__':
    app = Window(root)

    root.mainloop()
import tkinter as tk
from tkinter import N, ttk
from tkinter.messagebox import showerror, showinfo, askokcancel, askquestion
from PIL import ImageTk, Image
import ast
import webbrowser


class HeaderFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
    
    #def create_header_frame(self):
        self.frame = ttk.Frame(container, width=400, height=50,border=10, borderwidth=5,relief='raised', padding=5, style='HF.TFrame')

        # configure frame styles
        self.style = ttk.Style(self)
        self.style.configure('HF.TFrame', background='black')

        # # grid layout for the input frame
        # frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        
       
        img = ImageTk.PhotoImage(Image.open('daily_cloud.png'))
        #photo = tk.PhotoImage(file='./images/gf.png')
        self.header_label = ttk.Label(self.frame, text='What movie would you love to watch tonight?', font=("Helvetica", 14),
                                        background = 'tomato', foreground ="black")
        #header_label.grid(column=3, row=0, columnspan=1)
        #tk.Label(self.frame, image=img).pack()
        self.header_label.pack(ipadx=10, ipady=10)  #(column=1, columnspan=2, sticky=tk.EW, **options)

        

        
        # for widget in self.winfo_children():
        #     widget.grid(padx=5, pady=5)

        #return frame

        self.frame.grid(padx=10, pady=10, row=0, column=0, columnspan=2)
        self.frame.grid(sticky=tk.N, column=1, columnspan=4, row=0, padx=10)


class SelectGenreFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}
        self.frame = ttk.Frame(container, width=400, height=500,border=10, borderwidth=5, padding=5, style='SGF.TFrame')
        #self.choose_genre()
        #self.get_movies()
        self.style = ttk.Style(self)
        self.style.configure('SGF.TFrame', background='#010203')

    #def choose_genre(self):
        genres = ['Drama', 'Crime', 'Action', 'Biography', 'Adventure', 'Comedy',
       'Animation', 'Horror', 'Western', 'Mystery', 'Film-Noir']
        self.titles = []
        self.movie_urls = []
        
        # grid layout for the input frame
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=2)
        self.frame.rowconfigure(2, weight=10)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        # create genre dropdown
        ttk.Label(self.frame, text='please select a genre:').grid(row=0, column=0)
        self.selection = tk.StringVar()
        #self.keepgenres = self.value.get() # to persists the values for the Stringvar method
        self.selected_genre = ttk.Combobox(self.frame, textvariable=self.selection, state='readonly', values=genres)
        #selected_genre.current(0)
        self.selected_genre.grid(row=1, column=0, columnspan=2)
        self.selected_genre.current(0)
        self.selected_genre.bind('<<ComboboxSelected>>', self.genre_changed)

        b1=tk.Button(self.frame,text='Show Movies',command=lambda: self.show_movies(),font=6,background='tomato')
        b1.grid(row=1, column=3, padx=2)

        
        # self.title_label = ttk.Label(self.frame, text='title', font=("Helvetica", 12),foreground ="black",)
        # self.title_label.grid(row=1, column=4, padx=10)

        


        # add padding to the frame and show it
        self.frame.grid(padx=10, pady=10, row=1, column=2, columnspan=2)

    def genre_changed(self,event):
        self.get_movies()
        """ handle the month changed event """
        showinfo(
            title='Great choice!',
            message="Click the 'Show Movies' button to display the movies. Select any movie from the drop down to watch the trailer."
        )

    def get_movies(self):
        #title_label = ttk.Label(self, text='title', font=("Helvetica", 14),foreground ="black",).grid(row=0, column=2, padx=10)

        with open('movies.txt', 'r') as f:
            data = f.read()
            movies = ast.literal_eval(data)
    
        for v in movies.values():
            if v['genre'] == self.selection.get():
                #print(v['genre'])
                title = v['title']
                url = v['movie link']
                #self.title_label.config(text=title)
                self.movie_urls.append(url)
                self.titles.append(title)
                #print(title)
            # else:
        
        zipped_movies = zip(self.titles, self.movie_urls)
        self.movie_info = list(zipped_movies)
        #print(self.movie_info)
        #print(self.titles)
    
    def show_movies(self):
        #self.get_movies()
        self.movies_list = tk.Listbox(self.frame, height=6, selectmode=tk.ACTIVE)
        self.movies_list.grid(row=2,column=0, columnspan=2)
        self.movies_list.configure(background="#ff6e4a", foreground="white", font=('Aerial 13'), width=0) 
        #print(self.titles)
        for element in self.titles:
            self.movie_element = self.movies_list.insert(tk.END,element)

        scrollbar = ttk.Scrollbar(self.frame,orient=tk.VERTICAL,command=self.movies_list.yview)
        self.movies_list['yscrollcommand'] = scrollbar.set
        #scrollbar.grid(side=tk.LEFT, expand=True, fill=tk.Y)
        self.movies_list.bind('<<ListboxSelect>>', self.select_movie)
                
        self.grid(row=1, column=1)
        self.selected_genre.configure(state='disabled')


    def select_movie(self,event):
        # get selected indices
        #print(self.movie_info)
        selected_movie_index = self.movies_list.curselection()
            # get selected items
        if selected_movie_index:
            selected_movie = self.movies_list.get(selected_movie_index)
            #print(selected_movie)

            for index, tup in enumerate(self.movie_info):
                #print(f'the tuple is: {tup}')
                #print(selected_movie)
                if tup[0] == selected_movie:
                    #print(tup[0])
                    movie_url = tup[1]
                    #print(f'movie_url: {movie_url}')
                    webbrowser.open(movie_url)
        else:
            self.show_error()
    
    def show_error(self):
        """ handle the month changed event """
        showinfo(
            title='Error!',
            message="Please select a movie."
        )

       
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Movie Recommender App')
        self.geometry('800x500')
        #self.resizable(False, False)

        self.rowconfigure(0, weight=1,)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        # Add image file
        # bgimg = tk.PhotoImage(file = "daily_cloud.png")

        # canvas1 = tk.Canvas(self, width = 400,
        #          height = 400)
        # canvas1.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        # # Display image
        # canvas1.create_image( 0, 0, image = bgimg, 
        #              anchor = "nw")

         # create a canvas to show image on
        canvas_for_image = tk.Canvas(self, height=800, width=500, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, column=0, rowspan=3, columnspan=6, sticky='nesw', padx=0, pady=0)

        # create image from image location resize it to 200X200 and put in on canvas
        image = Image.open('banner.png')
        canvas_for_image.image = ImageTk.PhotoImage(image.resize((800, 500), Image.Resampling.LANCZOS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')

        


if __name__ == "__main__":
    app = App()
    HeaderFrame(app)
    SelectGenreFrame(app)
    #ChooseMovieFrame(app)
    app.mainloop()

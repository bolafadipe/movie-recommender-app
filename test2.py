from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
import ast
from genres import genres
from pprint import pprint
import webbrowser


genres = [genre.lower() for genre in genres]
#print(genres)
class Movies:
    def __init__(self):
        self.titles = []
        self.movie_links = []
        self.descriptions = []


    def open_file(self):
        #title_label = ttk.Label(self, text='title', font=("Helvetica", 14),foreground ="black",).grid(row=0, column=2, padx=10)

        with open('file.txt', 'r') as f:
            data = f.read()
            movies = ast.literal_eval(data)
            #print(type(movies))
            return movies
    
    def choose_genre(self, movies):
        user_choice = input('choose a movie genre: ').lower() 
        #print(user_choice)

        while user_choice not in genres:
            print('not a valid genre name') 
            user_choice = input('choose a movie genre: ').lower() 
            
        if user_choice in genres:  
            print('good') 
            #print(movies.values())  
            for v in movies.values():
                v['genre'] = v['genre'].lower()
                if v['genre'] == user_choice:
                    title = v['title']
                    url = v['movie link']
                    description = v['description']
                    self.movie_links.append(url)
                    self.titles.append(title)
                    self.descriptions.append(description)
            #pprint(self.titles)
            zipped_movies = zip(self.titles, self.movie_links, self.descriptions)
            self.movie_info = list(zipped_movies)

            print('Great choice!')
            print(f'here is a list of {user_choice} movies:')
            
            pprint(self.titles)
            #self.get_movie_title()
            #self.get_movie_title(self.movie_info)
        #return self.movie_info


    def get_movie_title(self):
        for title in self.titles:
            print(title)
            pass

    def choose_movie(self):
        movie_choice = input('which movie would you love to watch? ')
    
        for index, value in enumerate(self.movie_info):
            if value[0] == movie_choice:
                print(value[2])
                message = input('y or n')
                if message == 'y':
                    webbrowser.open(value[1])
        
            
       
            
        
      


movie = Movies()
movies = movie.open_file()
movie.choose_genre(movies)
#movie.get_movie()
movie.choose_movie()
import ast
from time import sleep
from genres import genres
from pprint import pprint
import json
import webbrowser


 # move this to the init

class Movies:
    def __init__(self):
        self.genres = [genre.lower() for genre in genres]
        self.titles = []
        self.movie_links = []
        self.descriptions = []


    def open_file(self):
        with open('movies.json') as json_file:
            movies = json.load(json_file)
            #pprint(movies)
            return movies


    def choose_genre(self):
        print('choose a genre from the list of genres below:')
        print(self.genres)
        user_choice = input('type your choice here: ').lower() 
        while user_choice not in self.genres:
            print('invalid genre name. Please enter a valid name') 
            
            user_choice = input('type your choice here: ').lower()
            
        
        return user_choice

    def get_movie_info(self, user_choice, movies):
        if user_choice in self.genres:
            print(user_choice)
            print(self.genres)    
            for v in movies.values():
                v['genre'] = v['genre'].lower()
                if v['genre'] == user_choice:
                    title = v['title']
                    url = v['movie link']
                    description = v['description']
                    self.movie_links.append(url)
                    self.titles.append(title)
                    self.descriptions.append(description)
            
            zipped_movies = zip(self.titles, self.movie_links, self.descriptions)
            movie_info = list(zipped_movies)
            print(movie_info[0])

            print('Great choice!')
            print(f'here is a list of {len(self.titles)} {user_choice} movies for your viewing pleasure:')


def main():
    movie = Movies()
    movies = movie.open_file()
    user_choice = movie.choose_genre()
    movie.get_movie_info(user_choice, movies)

main()
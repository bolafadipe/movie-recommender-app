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
            return movies
    
    def choose_genre(self):
        user_choice = input(f'choose a genre from this list of genres: {self.genres} ').lower() 
        while user_choice not in self.genres:
            print('invalid genre name. Please enter a valid name') 
            user_choice = input(f'choose a genre from this list of genres: {self.genres} ').lower() 
        
        return user_choice
            

    def get_movie_info(self, user_choice, movies):
        if user_choice in self.genres:    
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

            print('Great choice!')
            print(f'here is a list of {len(user_choice)} {user_choice} movies for your viewing pleasure:')
            
            pprint(self.titles)
            print(movie_info[0])
            
        return movie_info

    def get_movie(self, movie_info):
        movie_choice = input('which movie would you love to watch? ').lower()
        for index, value in enumerate(movie_info):
            print(index, value)
            if value[0].lower() == movie_choice:
                print()
                print(f'About the movie: {movie_choice}')
                for i in value[2].split(' '):
                    print(i, end=' ', flush=True)
                    sleep(0.25)
                print()
                message = input('Do you want to watch the movie trailer? Yes(y) / No(n) ').lower()
                if message in 'yes':
                    webbrowser.open(value[1])
                else:
                    print('Thank you for your time.')
        
            
       
            
        
# move this to the __main__ file     
# if __main__ == '__main__:
    #do


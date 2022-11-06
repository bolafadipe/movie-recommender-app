import ast
from time import sleep
from genres import genres
from pprint import pprint
import webbrowser


genres = [genre.lower() for genre in genres]
class Movies:
    def __init__(self):
        self.titles = []
        self.movie_links = []
        self.descriptions = []


    def open_file(self):
        with open('file.txt', 'r') as f:
            data = f.read()
            movies = ast.literal_eval(data)
            
            return movies
    
    def choose_genre(self, movies):
        user_choice = input('choose a movie genre: ').lower() 
        while user_choice not in genres:
            print('not a valid genre name') 
            user_choice = input('choose a movie genre: ').lower() 
            
        if user_choice in genres:    
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
            
        return movie_info

    def choose_movie(self, movie_info):
        movie_choice = input('which movie would you love to watch? ').lower()
        for index, value in enumerate(movie_info):
            if value[0].lower() == movie_choice:
                print()
                print(f'About the movie: {movie_choice}')
                for i in value[2].split(' '):
                    print(i, end=' ', flush=True)
                    sleep(0.25)
                print()
                message = input('Do you want to watch the movie trailer? Yes(y) / No(n) ').lower()
                if message == 'y' or message == 'yes':
                    webbrowser.open(value[1])
                else:
                    print('Thank you for your time.')
        
            
       
            
        
      


movie = Movies()
movies = movie.open_file()
movie_info = movie.choose_genre(movies)
movie.choose_movie(movie_info)
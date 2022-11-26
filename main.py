from controller import Movies


def run_movie_app():
    movie = Movies()
    movies = movie.open_file()
    user_choice = movie.choose_genre()
    movie_info = movie.get_movie_info(user_choice, movies)
    movie.get_movie(movie_info)

if __name__ == "__main__":
    run_movie_app()
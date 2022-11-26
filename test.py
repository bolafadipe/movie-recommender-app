# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
import ast
import json




with open('movies.json') as json_file:
    data = json.load(json_file)
    print(type(data))
    # movies = ast.literal_eval(data)
    # print(type(movies))

# with open('movies.json', 'w') as f:
#     json.dump(movies, f)
# for value in movies.values():
#     if value['genre'] == 'Animation':
#         print(value['title'])




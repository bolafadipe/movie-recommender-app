import json
import ast

with open('file.txt', 'r') as f:
    data = f.read()
    movies = ast.literal_eval(data)

#print(movies.keys())
if __name__ == '__main__':
    title = input('enter movie title: ')
    for k,v in movies.items():
        if v['title'] == title:
            print(title)


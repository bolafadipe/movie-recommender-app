import json
import ast
import time
from plyer import notification


with open('file.txt', 'r') as f:
    data = f.read()
    movies = ast.literal_eval(data)

#print(movies.keys())

if __name__ == '__main__':
    title = input('enter movie title: ')
    for k,v in movies.items():
        if v['title'] == title:
            print(title)
            notification.notify(
            title = "HEADING HERE",
            message=" DESCRIPTION HERE" ,
           
            # displaying time
            timeout=2)
            time.sleep(5)


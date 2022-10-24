# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
import ast

my_list = [('a', 'one'), ('b', 'two'), ('c', 'three')]


for index, tup in enumerate(my_list):
    if tup[1] == 'one':
    #print(index)
        print(tup[1])

    #print(tup[1])


# genres = ['Drama', 'Crime', 'Action', 'Biography', 'Adventure', 'Comedy',
#        'Animation', 'Horror', 'Western', 'Mystery', 'Film-Noir']


# with open('file.txt', 'r') as f:
#     data = f.read()
#     movies = ast.literal_eval(data)

# for value in movies.values():
#     if value['genre'] == 'Animation':
#         print(value['title'])


#print(movies.keys())
#if __name__ == '__main__':
movie_titles = []
#genre = input('enter movie title: ')

# if genre in genres:
#     print('true')
#     for v in movies.values():
#         if v['genre'] == genre:
#             title = v['title']
#             print(title)
    # title = (v['title'])
    # movie_link = (v['movie link'])
    # description = (v['description'])
    # image_url = (v['image_url'])
    # drama = []
    # if genre in genres:
    #     if genre in v['']
    #     #print(genre)
    #     movies = v['title']
    #     drama.append(movies)
#print(len(movies))
        # movie = v['title']
        # print(movie)
        # movie_titles.append(movie)
        #print(movie_titles)
            

# Create an instance of tkinter window
# win = Tk()

# # Define the geometry of the window
# win.geometry("700x500")

# frame = Frame(win, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("daily_cloud.png"))

# # Create a Label Widget to display the text or Image
# label = Label(frame, image = img)
# label.pack()

# win.mainloop()
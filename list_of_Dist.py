from collections import Counter
from shutil import move 

movie_data = {}
with open("imdb.csv") as f:
    for line in f:
        movie_data.append(line.rstrip('\n').split(','))
print(type(movie_data))
'''ctr = Counter(movie_data)
ctr.most_common(0)'''
my_dict = {}
my_dict.append(movie_data)
print(my_dict)
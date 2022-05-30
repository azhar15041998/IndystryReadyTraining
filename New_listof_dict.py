import csv
data = []
with open('imdb.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for d in reader:
        d['Actors'] = [name.strip() for name in d['Actors'].split(",")]
        d['Genre'] = [genre.strip() for genre in d['Genre'].split(",")]
        data.append(d)
        
director_actor_count = {}
for d in data:
    for actor in d["Actors"]:
        combo = (d["Director"], actor)
        if combo not in director_actor_count:
            director_actor_count[combo] = 1
        else:
            director_actor_count[combo] += 1
            
(director, actor), count = max(director_actor_count.items(), key=lambda x: x[1])
print(f"Combo '{director} - {actor}' has done maximum number of movies count :{count}")
names = ['atish', 'piyush', 'badheer', 'fa2',]
l = []


for people in names:
  l.append(people + ' Gadhe kahi ke ')
print (l)

print([people + ' Idiot ' for people in names])

movies_and_ratings = {'Avengers': 7, 'Bingo': 6, 'AnyThing': 8, 'NOO': 6, 'Flex': 3, 'shroud':3, 'Tenz': 3}
l = []
for movie in movies_and_ratings:
  if movies_and_ratings[movie] > 3:
    l.append(movie)
print (l)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] == 3])
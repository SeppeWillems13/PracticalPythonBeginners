current_movies = {
    'The Matrix': '10:00',
    'Finding Dory': '12:00',
    'Jaws': '14:00',
    'Star Wars: The Force Awakens': '16:00',
}

print("We're showing these movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)
if showtime:
    print('The showtime for ' + movie + ' is ' + showtime)
else:
    print("We don't have that movie")
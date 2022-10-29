# Make a list of your favourite Movies, the list should have minimum 8 elements.

movies = ["Ready Player One", "Jurassic World Dominion", "Transformers", "Terminator: Dark Fate", "Sonic the Hedgehog 2", "The Tomorrow War", "Edge of Tomorrow", "E.T. the Extra-Terrestrial"]

# Print a specified list after removing the 5th element.

del movies[4]
print(movies)

# Insert your favourite movie director name at the 4th index position of the list and print out the list elements.

movies.insert(4, "Michael Bay")
print(movies)

# List out the 4th element in the list.

print(movies[3])

# Add additional item to the current list and display the list.

movies.append("Independence Day")
movies.append("Battleship")
print(movies)



movies = [["Deadpool", "2016", "8.0"], 
        ["Casino Royale", "2006", "8.1"], 
        ["Star Wars: A New Hope", "1977", "8.6"]]

movie = ["Monsters, Inc.", "2001", "8.1"]

movies.append(movie)

# The first number is the row,
# The second number is the column
print("Item in movies position [0][0]: " + movies[0][0])
print("Item in movies position [3][2]: " + movies[3][2])

print()
# Display all elements in the movies list
# We will need to use a nest for loop to do 

# The first loop goes through the row
for movie in movies:
    # The second loop goes through the columns
    for item in movie:
        print(item, end=" | ")
    print()
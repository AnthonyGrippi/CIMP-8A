FILENAME = "A:\\Python Projects\\Assignments\\Assignment6\\movies.txt"

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()

def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
        return movies

def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)

def add(movie_list):
    movie = input("Movie: ")
    movie_list.append(movie)
    write_movies(movie_list)
    print(movie + " was added.\n")

def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + ". " + movie)
    print()

def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(movie + " was added.\n")

def delete_movie(movies):
    number = int(input("Number: "))
    if number < 1 or number > len(movies):
        print("Invalid movie number. \n")
    else:
        movie = movies.pop(number - 1)
        write_movies(movies)
        print(movie + " was deleted.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(movie + " was deleted.\n")


def main():
    # Create and Initialize the movie
    movie_list = ["Deadpool", "Casino Royale", "Goodfellas"]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "exit":
            break
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
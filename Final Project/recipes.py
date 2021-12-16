import Myrequests

def show_title():

    """
        This method will display the title to the screen
    """
    print("My Recipe Program")
    print()


def show_menu():

    """
        This method will display the title to the screen
    """
    print("COMMAND MENU")
    print("1    -   List all categories")
    print("2    -   List all meals for the categories")
    print("0    -   Exit the application")
    print()

def list_categories():
    
    """
        This method will get and display the list of catefories to the screen
    """
    categories = Myrequests.get_categories()
    if categories is None:
        print("Technical difficulties, please try again later")
        
    else:
        print("CATEGORIES")
        for i in range(len(categories)):
            category = categories[i]
            print("    " + category.get_name())
    print()

def list_meals(title, meals):
    
    """
        This method will display the list of meals
        for a category or ara to screen
    """
    if meals is None:
        print("Technical difficulties, plese try again later")

    else:
        print(title.upper(), "MEALS")

        for i in range(len(meals)):
            meal = meals[i]
            print("    " + meal.get_name())
        print()

def list_meals_by_category():

    lookup_category = input("Enter a category: ")

    categories = Myrequests.get_categories()
    found = False

    if categories is None:
        print("Technical difficulties, please try again later.")

    else:
        for i in range(len(categories)):
            category = categories[i]
            if category.get_name().lower() == lookup_category.lower():
                found = True
                break

        if found:
            meals = Myrequests.get_meal_by_category(lookup_category)
            list_meals(lookup_category, meals)
        else:
            print("Invalid category please try again.")


def main():

    """
        This method controls the flow of the program
    """
    show_title()
    show_menu()

    while True:
        command = input("What would you like to do? ")
        if command == "1":
            list_categories()
        elif command == "2":
            list_meals_by_category()


if __name__ == "__main__":
    main()

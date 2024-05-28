# Import Pickle module to work with binary files
import pickle

# Function that takes one recipe as an argument and prints all attributes
def display_recipe(recipe):
    print("Recipe: " + recipe["name"])
    print("Cooking Time (minutes): " + str(recipe["cooking_time"]))
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: " + recipe["difficulty"])

# Function that searches for an ingredient in the given data
def search_ingredient(data):
    all_ingredients = enumerate(data["all_ingredients"])
    numbered_ingredients = list(all_ingredients)

    # Displays each ingredient with a number
    print("Ingredients available across all recipes:")
    print("-----------------------------------------")
    for ingredient in numbered_ingredients:
        print(ingredient[0], ingredient[1])
    
    # Tries to search user-defined ingredient number
    try:
        n = int(input("Enter the number of an ingredient to search: "))

        # Stores the user-defined ingredient 
        ingredient_searched = numbered_ingredients[n][1]
        print("Searching for recipes with that ingredient...")

    # If user enters anything but an integer, informs user
    except ValueError:
        print("Invalid input. Enter a number only.")

    # Prints every recipe that contains the given ingredient
    else:
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)

# Tries to load user-defined filename
file_name = input("Enter the filename that contains recipe data: ")

try:
    file = open(file_name, "rb")
    data = pickle.load(file)
    print("File loaded.")

# If user-defined filename not found, informs user
except FileNotFoundError:
    print("File with that name not found.")

# Closes file stream and initializes search_ingredient()
else:
    file.close()
    search_ingredient(data)

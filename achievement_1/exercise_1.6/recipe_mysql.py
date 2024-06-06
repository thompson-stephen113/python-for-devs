# ------------------------- SQL / PYTHON CONNECTION ------------------------- #
import mysql.connector

# Initialize connection object to the MySQL server
conn = mysql.connector.connect(
    host = "localhost",
    user = "cf-python",
    passwd = "password"
)

# Performs operations on the database using SQL queries
cursor = conn.cursor()

# Creates the task_database with a condition to prevent multiple creations
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Connects to the database
cursor.execute("USE task_database")

# Creates Recipes table with a condition to prevent multiple creations
cursor.execute("""CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)""")


# ------------------------- Recipe Difficulty ------------------------- #
# Determines recipe difficulty
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty


# ------------------------- Main Menu ------------------------- #
# Defines function for the main menu and all of its functions
def main_menu():
    # Defines function to create a new recipe
    def create_recipe(conn, cursor):
        # Stores an empty list for the recipe ingredients
        ingredients_list = []

        # Stores user input for recipe attributes
        name = str(input("\nEnter recipe name: "))
        cooking_time = int(input("Enter cooking time (minutes): "))
        ingredients = input("Enter ingredients, separated by a comma: ")

        # Appends user inputted ingredients to list, then converts list to a joined string
        ingredients_list.append(ingredients)
        ingredients_str = ", ".join(ingredients_list)

        difficulty = calc_difficulty(cooking_time, ingredients_list)

        # Builds SQL query string
        sql_query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
        sql_values = (name, ingredients_str, cooking_time, difficulty)
        cursor.execute(sql_query, sql_values)
        conn.commit()

        print("\nRecipe successfully created.\n")


    # Defines function to search for a recipe
    def search_recipe(conn, cursor):
        # Stores an empty list for all ingredients
        all_ingredients = []
        
        # Selects values in "ingredients" column from table "Recipes"
        cursor.execute("SELECT ingredients FROM Recipes")
        results = cursor.fetchall()

        # Retrieves ingredients from the "ingredients" column and adds them to all_ingredients
        for ingredients_list in results:
            for ingredient in ingredients_list:
                split_ingredients = ingredient.split(", ")
                all_ingredients.extend(split_ingredients)

        # Removes duplicate ingredients from all_ingredients
        all_ingredients = list(dict.fromkeys(all_ingredients))
        numbered_ingredients = list(enumerate(all_ingredients))

        # Numbers and sorts each ingredient from the list and prints them
        print("\nIngredients list:")
        print("-----------------\n")

        for index, ingredient in enumerate(numbered_ingredients):
            print(str(ingredient[0] + 1) + ". " + ingredient[1])

        # Tries to search user-defined ingredient number
        try:
            n = int(input("\nEnter the number of an ingredient to search: "))
            true_index = n - 1

            # Stores the user-defined ingredient 
            ingredient_searched = numbered_ingredients[true_index][1]
            print(f"\nSearching for recipes with {ingredient_searched}...")

        # If user enters anything but an integer, informs user
        except ValueError:
            print("\nInvalid input. Enter a number only.")

        # Prints every recipe that contains the given ingredient
        else:
            print(f"\nRecipes containing {ingredient_searched}:")
            print("---------------------------------------")

            # Selects "ingredients" from "Recipes"
            cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ("%" + ingredient_searched + "%",))
            recipes_searched = cursor.fetchall()

            # Prints each recipe containing the searched ingredient if present
            if recipes_searched:
                for recipe in recipes_searched:
                    print("\nID: ", recipe[0])
                    print("Name: ", recipe[1])
                    print("Ingredients: ", recipe[2])
                    print("Cooking Time (minutes): ", recipe[3])
                    print("Difficulty: ", recipe[4])
                    print()
            else:
                print(f"No recipes found with {ingredient_searched}.\n")
        

    # Defines function to update an existing recipe
    def update_recipe(conn, cursor):
        # Selects all recipes from "Recipes"
        cursor.execute("SELECT * FROM Recipes")
        recipes_selected = cursor.fetchall()

        print("\nRecipes:")
        print("------\n")

        # Lists all recipes
        for recipe in recipes_selected:
            # Splits the ingredients list with a comma
            ingredients_list = recipe[2].split(", ")
            ingredients_str = ", ".join(ingredients_list)

            print("ID: ", recipe[0])
            print("Name: ", recipe[1])
            print("Ingredients: ", ingredients_str)
            print("Cooking Time (minutes): ", recipe[3])
            print("Difficulty: ", recipe[4])

        # Stores user input for recipe and attribute to update
        id_to_update = int(input("\nEnter the ID of the recipe to update: "))
        column_to_update = str(input("Enter one of the following to udpate: \nname \ncooking_time \ningredients\n\n"))
        new_value = input("\nEnter the new value: ")

        # Determines inputted column and updates its value with new_value
        if column_to_update == "name":
            cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_value, id_to_update))
            print(f"Recipe name updated to {new_value}\n")

        elif column_to_update == "cooking_time":
            cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (new_value, id_to_update))
            print(f"Cooking Time updated to {new_value}\n")

            # Reselects recipe to work with the new value
            cursor.execute("SELECT * FROM Recipes WHERE id = %s", (id_to_update,))
            working_recipe = cursor.fetchall()
            ingredients = tuple(working_recipe[0][2].split(", "))
            cooking_time = working_recipe[0][3]

            # Recalculates difficulty based on new cooking time and ingredients
            updated_difficulty = calc_difficulty(cooking_time, ingredients)
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, id_to_update))
            print(f"Difficulty updated to {updated_difficulty}\n")
        
        elif column_to_update == "ingredients":
            cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (new_value, id_to_update))
            print(f"Ingredients updated to {new_value}\n")

            # Reselects recipe to work with the new value
            cursor.execute("SELECT * FROM Recipes WHERE id = %s", (id_to_update,))
            working_recipe = cursor.fetchall()
            ingredients = tuple(working_recipe[0][2].split(", "))
            cooking_time = working_recipe[0][3]

            # Recalculates difficulty based on new cooking time and ingredients
            updated_difficulty = calc_difficulty(cooking_time, ingredients)
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, id_to_update))
            print(f"Difficulty updated to {updated_difficulty}\n")

        conn.commit()
    
    # Defines funciton to delete a recipe
    def delete_recipe(conn, cursor):
        cursor.execute("SELECT * FROM Recipes")
        recipes_selected = cursor.fetchall()

        print("\nRecipes:")
        print("------\n")

        # Lists all recipes
        for recipe in recipes_selected:
            # Splits the ingredients list with a comma
            ingredients_list = recipe[2].split(", ")
            ingredients_str = ", ".join(ingredients_list)

            print("ID: ", recipe[0])
            print("Name: ", recipe[1])
            print("Ingredients: ", ingredients_str)
            print("Cooking Time (minutes): ", recipe[3])
            print("Difficulty: ", recipe[4])
            print()

        id_to_delete = input("\nEnter the ID of a recipe to delete: ")
        cursor.execute("DELETE FROM Recipes WHERE id = %s", (id_to_delete,))

        print("\nRecipe successfully deleted.\n")
        conn.commit()


    # for loop running the main menu, ends when user chooses to quit
    choice = ""
    while(choice != "quit"):
        print("Welcome to Recipes! Select a number from the list.")
        print("1. Create a recipe.")
        print("2. Search for a recipe.")
        print("3. Update an existing recipe.")
        print("4. Delete a recipe.")
        print("Type 'quit' to exit the program.\n")
        choice = input("Select an option: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        else:
            conn.commit()
            conn.close()


# ------------------------- MAIN CODE ------------------------- #
# Calls main_menu() in the main code
main_menu()

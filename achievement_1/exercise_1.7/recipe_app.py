# ------------------------- SQLAlchemy Imports ------------------------- #
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

# Connects SQLAlchemy to task_database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Creates a Session by binding engine and initializes session object
Session = sessionmaker(bind=engine)
session = Session()


# ------------------------- Recipe Model ------------------------- #
# Stores declarative base class
Base = declarative_base()

# Defines Recipe model
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Defines string representation to identify objects in terminal
    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} ({self.difficulty})>"

    # Defines string representation for printing
    def __str__(self):
        ingredients_list = self.ingredients.split(", ")
        ingredients_str = ", ".join(ingredients_list)

        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {ingredients_str}\n"
            f"Cooking Time (minutes): {self.cooking_time}\n"
            f"Difficulty: {self.difficulty}\n"
        )
    
    # Determines recipe difficulty
    def calc_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "Hard"
        return self.difficulty

    # Retrieves ingredients string as a list 
    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return self.ingredients.split(", ")
        
# Creates the table from the database
Base.metadata.create_all(engine)


# ------------------------- Main Operations ------------------------- #
# Defines create_recipe()
def create_recipe():
    # Takes user input for recipe name and checks for validity
    while True:
        name = input("Enter the name of a recipe: ").strip()

        if len(name) > 50:
            print("Name must be 50 characters or less.")
            continue

        if not name.replace(" ", "").isalnum():
            print("Name must only contain alphanumeric characters and spaces.")
            continue

        break

    # Takes user input for cooking time and checks for validity
    while True:
        cooking_time = input("Enter the cooking time in minutes: ").strip()

        if not cooking_time.isnumeric():
            print("Cooking time must be a number.")
            continue

        cooking_time = int(cooking_time)

        break

    # Takes user input for ingredients and checks for validity
    ingredients = []

    while True:
        try:
            n = int(input("How many ingredients would you like to enter? ").strip())

            if n <= 0:
                print("You must enter at least one ingredient.")
                continue

            break

        except ValueError:
            print("Enter a valid number.")

    for i in range(n):
        while True:
            ingredient = input(f"Enter ingredient {i + 1}: ").strip()

            if not all(char.isalpha() or char.isspace() for char in ingredient):
                print("Ingredient must only contain alphabetical characters and spaces.")
                continue

            ingredients.append(ingredient)

            break
        
    ingredients_str = ", ".join(ingredients)

    # Creates recipe object
    recipe_entry = Recipe(
        name = name,
        cooking_time = cooking_time,
        ingredients = ingredients_str,
        difficulty = ""
    )

    # Calculates recipe difficulty
    recipe_entry.difficulty = recipe_entry.calc_difficulty()

    # Adds recipe to the sessions and commits changes
    session.add(recipe_entry)
    session.commit()

    print("\nRecipe successfully added.")

# Defines view_all_recipes()
def view_all_recipes():
    # Gets all recipes from database and stores it in recipes object
    recipes = session.query(Recipe).all()

    if not recipes:
        print("There are no recipes in the database.")
        return None
    
    # Prints each recipe via the __str__() method
    for recipe in recipes:
        print(recipe)

# Defines search_by_ingredients()
def search_by_ingredients():
    # Checks if the table has any entries
    if session.query(Recipe).count() == 0:
        print("There are no entries in this table.")
        return None
    
    # Gets values from ingredients column
    results = session.query(Recipe.ingredients).all()
    
    # Initializes empty list for all_ingredients
    all_ingredients = []

    # Adds each ingredient from results to all_ingredients if not already present
    for result in results:
        ingredients_list = result[0].split(", ")

        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Displays numbered ingredients
    print("\nAvailable Ingredients:")
    print("----------------------\n")

    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    # Takes user input to select ingredients by number
    selected_numbers = input("Select ingredients by their numbers, separated by spaces: ").split()

    try:
        true_index = [int(num) - 1 for num in selected_numbers]

        if any(i < 0 or i >= len(all_ingredients) for i in true_index):
            raise ValueError
    
    except ValueError:
        print("Invalid input.")
        return None
    
    # Creates list of ingredients to search
    search_ingredients = [all_ingredients[i] for i in true_index]

    # Initializes list of conditions and uses a search string to add like terms to it
    conditions = []

    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    
    # Retrieves recipes matching conditions
    recipes = session.query(Recipe).filter(*conditions).all()

    # Displays recipes if found
    if recipes:
        for recipe in recipes:
            print()
            print(recipe)
    else:
        print("No recipes found with the selected ingredients.")

# Defines edit_recipe()
def edit_recipe():
    # Checks if there are any recipes in the database
    if session.query(Recipe).count() == 0:
        print("There are no recipes in the database.")
        return None

    # Gets ID and name of each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # Displays available recipes
    print("\nAvailable Recipes:")
    print("------------------\n")

    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")

    # Takes user input to select recipe by ID
    try:
        selected_id = int(input("\nEnter the ID of the recipe to edit: ").strip())
    
    except ValueError:
        print("Invalid input.")
        return None
    
    # Get corresponding recipe by ID
    recipe_to_edit = session.query(Recipe).filter_by(id=selected_id).first()
    
    if not recipe_to_edit:
        print("The selected ID does not exist.")
        return None
    
    # Displays recipe details
    print("\nSelected recipe:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Cooking Time (minutes): {recipe_to_edit.cooking_time}")
    print(f"3. Ingredients: {recipe_to_edit.ingredients}")

    # Takes user input to select an attribute to edit
    try:
        attribute_choice = int(input("\nEnter the number of the attribute to edit: ").strip())

        if attribute_choice not in [1, 2, 3]:
            raise ValueError
    
    except ValueError:
        print("Invalid input.")
        return None
    
    # Edits the user selected attribute
    # ----- Name ----- #
    if attribute_choice == 1:
        new_name = input("\nEnter new recipe name: ").strip()

        if len(new_name) > 50:
            print("Name must be 50 characters or less.")
            return None
        
        if not new_name.replace(" ", "").isalnum():
            print("Name should only contain alphanumeric characters.")
            return None
        
        recipe_to_edit.name = new_name

    # ----- Cooking Time ----- #
    elif attribute_choice == 2:
        try:
            new_cooking_time = int(input("\nEnter new cooking time (minutes): ").strip())

        except ValueError:        
            print("Cooking time must be a number.")
            return None
        
        recipe_to_edit.cooking_time = new_cooking_time

    # ----- Ingredients ----- #
    elif attribute_choice == 3:
        new_ingredients = input("\nEnter new ingredients, separated by a comma: ").strip()

        ingredients_list = [ingredient.strip() for ingredient in new_ingredients.split(", ")]

        if not all(all(char.isalpha() or char.isspace() for char in ingredient) for ingredient in ingredients_list):
            print("Each ingredient must only contain alphabetical characters.")
            return None
        
        recipe_to_edit.ingredients = ", ".join(ingredients_list)

    # Recalculates recipe difficulty
    recipe_to_edit.difficulty = recipe_to_edit.calc_difficulty()

    # Commits changes to database
    session.commit()
    
    print("\nRecipe successfully updated.")

# Defines delete_recipe()
def delete_recipe():
    # Checks if there are any recipes in the database
    if session.query(Recipe).count() == 0:
        print("There are no recipes in the database.")
        return None

    # Gets ID and name of each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # Displays available recipes
    print("\nAvailable Recipes:")
    print("------------------\n")

    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")

    # Takes user input to select recipe by ID
    try:
        selected_id = int(input("\nEnter the ID of the recipe to delete: ").strip())
    
    except ValueError:
        print("Invalid input.")
        return None
    
    # Get corresponding recipe by ID
    recipe_to_delete = session.query(Recipe).filter_by(id=selected_id).first()
    
    if not recipe_to_delete:
        print("The selected ID does not exist.")
        return None
    
    # Displays selected recipe name
    print(f"\nRecipe to delete: {recipe_to_delete.name}")

    # Takes user input to confirm recipe deletion
    confirmation = input("\nAre you sure you want to delete this recipe? (Y/N)\n").strip()

    if confirmation == "Y":
        session.delete(recipe_to_delete)
        session.commit()

        print("\nRecipe successfully deleted.")
    else:
        print("\nCancelling deletion...")

# ------------------------- Main Menu ------------------------- #
# Defines main_menu()
def main_menu():
    while True:
        # Displays menu options
        print("\nRecipes Main Menu")
        print("-----------------\n")
        print("1. Create new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("Type 'quit' to exit the app\n")

        # Takes user input for selecting a menu option
        choice = input("Select an option: ").strip()

        # Executes corresponding function based on user input
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("\nExiting the app...")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid input.")

# ------------------------- Main Code ------------------------- #
main_menu()

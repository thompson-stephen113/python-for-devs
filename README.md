# python-for-devs
 Specialization course for Python in the Full-Stack Web Developer online course by CareerFoundry

<br>

## Achievement 1: Introduction to Python

### Objective
Build the command line version of a Recipe app, which acts as a precursor to its web app counterpart in Achievement 2.

### Exercise 1.1
1. Install Python v. 3.8.7 onto the system.
2. Set up a virtual environment. 
3. Create a Python script file on Visual Studio Code or equivalent text editor.
4. Set up an IPython shell in the virtual environment.
5. Export a requirements file.

<br>

### Exercise 1.2
1. Create a structure named <code>recipe_1</code> with keys for <code>name</code>, <code>cooking_time</code>, and <code>ingredients</code>.
2. The attributes for the <code>recipe_1</code> structure are:
    * Name: Tea
    * Cooking time: 5 minutes
    * Ingredients: Tea leaves, Sugar, Water
3. Create the <code>all_recipes</code> structure and add <code>recipe_1</code> to it.
4. Create your own recipes (up to 5).
5. Print the ingredients of each recipe as five different lists in the IPython shell.

<br>

### Exercise 1.3
1. Open a Python script and name it "exercise_1.3.py".
2. Initialize two empty lists: <code>recipes_list</code> and <code>ingredients_list</code>.
3. Define <code>take_recipe()</code>, which takes user input for:
    * <code>name (str)</code>: Stores recipe name
    * <code>cooking_time (int)</code>: Stores cooking time (minutes)
    * <code>ingredients (list)</code>: Stores ingredients, each as a string
    * <code>recipe (dict)</code>: Stores <code>name</code>, <code>cooking_time</code>, <code>ingredients</code>
4. Take user input for number of recipes to be entered, stored in variable <code>n</code>.
5. Run a <code>for</code> loop for <code>n</code> times:
    * Run <code>take_recipe()</code> and store output in variable recipe.
    * Run another <code>for</code> loop inside this loop, iterating through recipe's ingredients, picking them out individually.
        * Checks if an ingredient is present in <code>ingredients_list</code> and appends it if not.
    * Append recipe to <code>recipes_list</code>.
6. Run another <code>for</code> loop that iterates through <code>recipes_list</code> and picks out each recipe individually:
    * Determine difficulty of recipe:
        * If <code>cooking_time</code> < 10 minutes and number of ingredients < 4, set variable difficulty to Easy.
        * If <code>cooking_time</code> < 10 minutes and number of ingredients >= 4, set variable difficulty to Medium.
        * If <code>cooking_time</code> >= 10 minutes and number of ingredients < 4, set variable difficulty to Intermediate.
        * If <code>cooking_time</code> >= 10 minutes and number of ingredients >= 4, set variable difficulty to Hard.
    * Display recipe in format a specified format.
7. Display all ingredients, entered by user, in alphabetical order.

<br>

### Exercise 1.4
#### Part 1: recipe_input.py Script
1. Import <code>pickle</code>.
2. Define <code>take_recipe()</code> to take recipes from user.
    * Takes recipe name, cooking time, and ingredients.
    * Calculates difficulty of recipe with <code>calc_difficulty()</code>.
    * Returns all attributes in a dictionary.
3. Define <code>calc_difficulty()</code>.
    * If <code>cooking_time</code> < 10 minutes and number of ingredients < 4, set variable difficulty to Easy.
    * If <code>cooking_time</code> < 10 minutes and number of ingredients >= 4, set variable difficulty to Medium.
    * If <code>cooking_time</code> >= 10 minutes and number of ingredients < 4, set variable difficulty to Intermediate.
    * If <code>cooking_time</code> >= 10 minutes and number of ingredients >= 4, set variable difficulty to Hard.
4. Have user enter filename and define a <code>try-except-else-finally</code> block.
    * <code>try</code> will open the given file and load contents through <code>pickle</code> into variable <code>data</code> as a dictionary containing:
        * <code>recipes_list</code>
        * <code>all_ingredients</code>
    * First <code>except</code> handles <code>FileNotFoundError</code> and creates new dictionary <code>data</code>, containing recipes under key <code>recipes_list</code> and another list containing all ingredients, <code>all_ingredients</code>.
    * Second <code>except</code> handles all other exceptions, performs same operations as first.
    * <code>else</code> closes file stream opened in <code>try</code> block.
    * <code>finally</code> extracts values from dictionary into two lists: <code>recipes_list</code> and <code>all_ingredients</code>.
5. Ask user how many recipes to enter, and define <code>for</code> loop that calls <code>take_recipe()</code>. Append the output into <code>recipes_list</code>. Define inner loop that scans through the recipe's ingredients and adds them to <code>all_ingredients</code> if not already present.
6. Gather updated <code>recipes_list</code> and <code>all_ingredients</code> into dictionary, <code>data</code>.
7. Open binary file with user-defined filename and write <code>data</code> to it using <code>pickle</code>.

<br>

#### Part 2: recipe_search.py Script
1. Import <code>pickle</code>.
2. Define <code>display_recipe()</code>, which takes one recipe (dictionary type) as an argument and prints all attributes.
3. Define <code>search_ingredient</code>, which takes <code>data</code> (dictionary type):
    * Shows user all available ingredients in <code>data</code>, under <code>all_ingredients</code> key. Each ingredient is enumerated, and their index number is displayed with them.
    * <code>try</code> block has user pick a number corresponding with an ingredient from the list, which is stored in <code>ingredient_searched</code>.
    * <code>except</code> warns user if input is incorrect.
    * <code>else</code> iterates through every recipe in <code>data</code> and prints each one containing <code>ingredient_searched</code>.
4. Ask user for name of the file containing recipe data.
5. Use <code>try</code> block to open file, and extract its contents into <code>data</code> using <code>pickle</code>.
6. Add <code>except</code> to warn user if file is not found.
7. Add <code>else</code> block that calls <code>search_ingredient</code> with <code>data</code> as its argument.

<br>

#### Part 3:
1. Run "recipe_input.py" and enter sample recipes. Confirm .bin file generation. Take screenshots of results.
2. Run "recipe_search.py", enter ingredient to search for, and confirm output of relevant recipes. Take screenshots of results.

<br>

### Exercise 1.5
1. Define class <code>Recipe</code> with attributes:
    * <code>name</code>
    * <code>ingredients</code>
    * <code>cooking_time</code>
    * <code>difficulty</code>
2. Define procedural attributes (methods) for the class:
    * Initialization method that takes all data attributes.
    * Getter and setter methods for <code>name</code> and <code>cooking_time</code>.
    * <code>add_ingredients()</code>: takes variable-length arguments for recipes's ingredients.
        * Method should take in these ingredients and add them to <code>ingredients</code>.
        * Once all ingredients are added, call <code>update_all_ingredients()</code>.
    * Getter method for <code>ingredients</code> that calls itself.
    * <code>calc_difficulty()</code>: calculates difficulty of recipes using method from prior Exercises.
    * <code>search_ingredient()</code>: takes an ingredient as an argument, searches for it in a recipe, and returns <code>True</code> or <code>False</code>.
    * <code>update_all_ingredients()</code>: goes through the current object's ingredients and adds them to class variable <code>all_ingredients</code> if not already present.
        * This variable keeps track of all ingredients across all recipes.
    * String representation that prints entire recipe.
3. <code>recipe_search()</code>: finds recipes with a specified ingredient.
    * Takes 2 parameters:
        * <code>data</code>: takes in a list of <code>Recipe</code> objectsto search from.
        * <code>ingredient</code>: ingredient search term.
    * Runs a <code>for</code> loop through <code>data</code>, and:
        * Within the object, calls <code>search_ingredient()</code> to see if ingredient is present.
        * If above condition is satisfied, print recipe.
4. In main code, make an object under <code>Recipe</code> class:
    * Initialize object <code>tea</code> under <code>Recipe</code>.
    * Set name to <code>"Tea"</code>.
    * Set cooking time to <code>5</code>.
    * Add ingredients to recipe: <code>"Tea Leaves"</code>, <code>"Sugar"</code>, <code>"Water"</code>.
    * Display string representation.
5. Add 3 more recipes:
    * Coffee:
        * Ingredients: Coffee Powder, Sugar, Water
        * Cooking Time: 5
    * Cake:
        * Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
        * Cooking Time: 50
    * Banana Smoothie:
        * Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
        * Cooking Time: 5
6. Wrap recipes into a list called <code>recipes_list</code>.
7. Use <code>recipe_search()</code> to search for recipes containing Water, Sugar, Bananas.

<br>

### Exercise 1.6
#### Part 1: Create & Connect Database
1. Import mysql.connector.
2. Initialize <code>conn</code>.
3. Initialize <code>cursor</code> from <code>conn</code>.
4. Create a database, <code>task_database</code>.
5. Have script access database with <code>USE</code> statement.
6. Create <code>Recipes</code> table with columns:
    * <code>id</code>: integer type; increments automatically with primary key.
    * <code>name</code>: string type; character limit of 50.
    * <code>ingredients</code>: string type; character limit of 255.
    * <code>cooking_time</code>: integer type.
    * <code>difficulty</code>: string type; character limit of 20.

<br>

#### Part 2: The Main Menu
<code>main_menu()</code>:
1. <code>create_recipe(conn, cursor)</code>
2. <code>search_recipe(conn, cursor)</code>
3. <code>update_recipe(conn, cursor)</code>
4. <code>delete_recipe(conn, cursor)</code>
5. If the user exits this loop, changes should be committed, then the file stream should be closed. Call <code>main_menu()</code> in the main code.

<br>

#### Part 3: <code>create_recipe()</code>
1. Take user input for data attributes:
    * <code>name</code>: name of recipe, string.
    * <code>cooking_time</code>: time in minutes, integer.
    * <code>ingredients</code>: ingredients of recipe, string list.
2. Define <code>calc_difficulty</code> using same logic as previous exercises.
3. Write SQL queries to convert <code>ingredients</code> into a comma-separated string.
4. Execute query and commit changes.

<br>

#### Part 4: <code>search_recipe()</code>
1. Display list of all ingredients from <code>Recipes</code> table. Obtain list using <code>SELECT</code> on the <code>ingredients</code> column and store in variable <code>results</code>.
2. <code>results</code> is made up of a list of rows, each row being a tuple of column values. Add all ingredients from <code>ingredients</code> column to new list <code>all_ingredients</code> with no duplicates.
3. Allow user to pick a number corresponding with the ingredient to search. Store ingredient in variable <code>search_ingredient</code>.
4. Use <code>WHERE</code> with <code>LIKE</code> to search rows of the table for <code>search_ingredient</code> in <code>ingredients</code> column.
    * Search pattern for ingredient: <code>%{search_ingredient}%</code>.
5. Use this logic to build the query, fetch results, and display to user.

<br>

#### Part 5: <code>update_recipe()</code>
1. Fetch all recipes in database and list to user. User will pick recipe to update by its ID and the column name containing the value to be modified (<code>name</code>, <code>cooking_time</code>, <code>ingredients</code>).
2. Once column is selected, take new value input from user.
3. Build query in string form to update an entry on the table for the given ID, column, and updated value. If user updates <code>cooking_time</code> or <code>ingredients</code>, <code>difficulty</code> must be recalculated and updated.
4. Execute queries and commit changes.

<br>

#### Part 6: <code>delete_recipe()</code>
1. Displays all recipes, and user selects one by its ID to delete.
2. Build query using <code>DELETE</code>, where the row to be deleted is identified by the specified ID.
3. Execute query and commit changes.

<br>

### Exercise 1.7
#### Part 1: Set Up Script & SQLAlchemy
1. Open a script file called <code>recipe_app.py</code>.
2. Import all packages and methods necessary to build app.
3. Set up SQLALchemy. Make sure MySQL server is running.
4. Use credentials to create <code>engine</code> object that connects to database.
5. Make a session object to make changes to database.
    * Generate <code>Session</code> class, <code>bind</code> it to <code>engine</code>, and initialize <code>session</code> object.

<br>

#### Part 2: Create Model & Table
Store declarative base class into variable <code>Base</code> and begin definition for <code>Recipe</code> model.
1. <code>Recipe</code> should inherit <code>Base</code>.
2. Define attribute to set table's name to <code>final_recipes</code>.
3. Define recipe attributes to create table columns:
    * <code>id</code>: integer; primary key; incremenets automatically
    * <code>name</code>: string (50 character limit)
    * <code>ingredients</code>: string (255 character limit)
    * <code>difficulty</code>: string (20 character limit)
4. Define <code>\_\_repr__</code> method that shows quick representation of recipe, including <code>name</code>, <code>id</code>, and <code>difficulty</code>.
5. Define <code>\_\_str__</code> method that prints recipe in a readable format.
6. Define <code>calc_difficulty</code> using logic from past exercises.
7. Define method that retrieves <code>ingredients</code> string inside <code>Recipe</code> as a list, called <code>return_ingredients_as_list()</code>
    * If the instance variable <code>self.ingredients</code> is an empty string, return an empty list.
    * Otherwise, use <code>split()</code> to split the string whenever there is a comma followed by a space.
8. Create the corresponding table on the database using <code>create_all</code> method from <code>Base.metadata</code>.

<br>

#### Part 3: Define Main Operations as Functions
<code>create_recipe()</code>
1. Collect details of recipe (<code>name</code>, <code>ingredients</code>, <code>cooking_time</code>) from user.
2. Ensure all inputs are appropriate.
3. Collect ingredients from user:
    * Define a temporary empty list <code>ingredients</code>.
    * Ask user how many ingredients to enter.
    * Based on this number, run a <code>for</code> loop to collect each ingredient and add it to the temporary list.
4. Convert <code>ingredients</code> list into a string using <code>join()</code>, where each ingredient is joined with a comma followed by a space.
5. Create <code>recipe_entry</code> object from <code>Recipe</code> using the above details.
6. Generate <code>difficutly</code> for the recipe by calling <code>calc_difficulty</code>.

<br>

<code>view_all_recipes()</code>
1. Retrieve all recipes from database as a list.
2. If there are no entries, inform the user, and exit the function to return to main menu.
3. Loops through list of recipes and call each of their <code>\_\_str__</code>
methods to display them.

<br>

<code>search_by_ingredients()</code>
1. Check if the table has any entries. Use <code>count()</code> to get number of entries in the given table: <code>session.query(\<model name>).count()</code>. If no entries, notify user, and exit the function.
2. Retrieve only values from <code>ingredients</code> column of the table, and store them into variable <code>results</code>.
3. Initialize empty list <code>all_ingredients</code>.
4. Go through each entry in <code>results</code>, split up ingredients into a temporary list, and add each ingredient from this list to <code>all_ingredients</code>. Check each ingredient is not already present before adding.
5. Display ingredients to user, where each ingredient has a number displayed next to it. Ask user to select ingredients by number, separated by spaces, to search for recipes.
6. Check that the user's inputs match available options. Otherwise, inform user and exit function.
7. Based on user's selection, make a list of ingredients to be searched, <code>search_ingredients</code>, which contains these ingredients as strings.
8. Initialize empty list <code>conditions</code>, which will contain <code>like()</code> conditions for each ingredient being searched.
9. Run a loop through <code>search_ingredients</code>:
    * Make a search string, <code>like_term</code>, which is the ingredient, surrounded by "%" on either side.
    * Append search condition containing <code>like_term</code> to <code>conditions</code> list (e.g., <code>\<Model name>.\<column to serach in>.like(like_term)</code>).
10. Retrieve all recipes from database using <code>filter()</code>, containing <code>conditions</code>. Display recipes using <code>\_\_str__</code> method.

<br>

<code>edit_recipe</code>
1. Check if there are any recipes in the database, and continue only if there are. Otherwise, exit function.
2. Retrieve <code>id</code> and <code>name</code> for each recipe and store them into <code>results</code> variable.
3. For each item in <code>results</code>, display recipes to user.
4. User selects recipe by <code>id</code>. If chosen <code>id</code> does not exist, exit function.
5. Retrieve entire corresponding recipe and store in variable <code>recipe_to_edit</code>.
6. Display recipe <code>name</code>, <code>ingredients</code>, and <code>cooking_time</code>. <code>difficulty</code> cannot be edited.
7. Ask user which attribute to edit by entering its corresponding number.
8. Based on input, use <code>if-else</code> statements to edit attribute inside <code>recipe_to_edit</code>. Recalculate difficulty using <code>calc_difficulty</code>.
9. Commit changes.

<br>

<code>delete_recipe()</code>
1. Check if any there are any recipes in database, and continue only if there are. Otherwise, exit function.
2. Retrieve <code>id</code> and <code>name</code> for each recipe and store them into <code>results</code> variable.
3. For each item in <code>results</code>, display recipes to user.
4. User selects recipe by <code>id</code>. If chosen <code>id</code> does not exist, exit function.
5. Retrieve entire corresponding recipe and store in variable <code>recipe_to_delete</code>.
6. Ask user if they are sure they want to delete this entry. If yes, perform delete operation. If not, exit function.

<br>

#### Part 4: Design Main Menu
Main menu is contained in a <code>while</code> loop, where condition to exit loop will be based on user choice. Loop continues as long as user does not choose <code>quit</code>.

1. Inside loop, display six options:
    * Create a new recipe
    * View all recipes
    * Search for recipes by ingredients
    * Edit a recipe
    * Delete a recipe
    * Type "quit" to exit app
2. Use <code>if-elif</code> statements to launch the function that corresponds to the user's selection. Use <code>else</code> statement to handle improper input and display menu again.
3. Once user chooses to quit, close <code>session</code> and <code>engine</code> with their respective <code>close</code> methods.

<br>


## Achievement 2: Web Development & Django

### Objective
Take your Recipe app from Achievement 1 and use the Django web framework to develop a fully fledged web application with multiple users and an admin panel.

### Exercise 2.1
1. Download and install Python.
2. Create a folder for upcoming projects.
3. Setup and create a virtual environment and name it achievement2-practice.
4. Install Django.

<br>

### Exercise 2.2
1. Create folder "A2_Recipe_App".
2. Create virtual environment "a2_env_recipeapp" and activate it.
3. Install Django in the virtual environment.
4. In "A2_Recipe_App", create Django project "recipe_project".
5. Rename "recipe_project" project directory to "src".
6. From with "src", run migrations and then run the server.
7. Create superuser.

<br>

### Exercise 2.3
Coming soon

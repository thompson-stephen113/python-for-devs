# python-for-devs
 Specialization course for Python in the Full-Stack Web Developer online course by CareerFoundry

<br>

## Achievement 1: Introduction to Python

### Objective
Build the command line version of a Recipe app, which acts as a precursor to its
web app counterpart in Achievement 2.

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
Coming soon

## Achievement 2
Coming soon

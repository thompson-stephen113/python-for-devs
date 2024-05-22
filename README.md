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
1. Create a structure named recipe_1 with keys for name, cooking_time, and ingredients.
2. The attributes for the recipe_1 structure are:
    * Name: Tea
    * Cooking time: 5 minutes
    * Ingredients: Tea leaves, Sugar, Water
3. Create the all_recipes structure and add recipe_1 to it.
4. Create your own recipes (up to 5).
5. Print the ingredients of each recipe as five different lists in the IPython shell.

<br>

### Exercise 1.3
1. Open a Python script and name it "exercise_1.3.py".
2. Initialize two empty lists: recipes_list and ingredients_list.
3. Define take_recipe(), which takes user input for:
    * name (str): Stores recipe name
    * cooking_time (int): Stores cooking time (minutes)
    * ingredients (list): Stores ingredients, each as a string
    * recipe (dict): Stores name, cooking_time, ingredients
4. Take user input for number of recipes to be entered, stored in variable n.
5. Run a for loop for n times:
    * Run take_recipe() and store output in variable recipe.
    * Run another for loop inside this loop, iterating through recipe's ingredients, picking them out individually.
        * Checks if an ingredient is present in ingredients_list and appends it if not.
    * Append recipe to recipes_list.
6. Run another for loop that iterates through recipes_list and picks out each recipe individually:
    * Determine difficulty of recipe:
        * If cooking_time < 10 minutes and number of ingredients < 4, set variable difficulty to Easy.
        * If cooking_time < 10 minutes and number of ingredients >= 4, set variable difficulty to Medium.
        * If cooking_time >= 10 minutes and number of ingredients < 4, set variable difficulty to Intermediate.
        * If cooking_time >= 10 minutes and number of ingredients >= 4, set variable difficulty to Hard.
    * Display recipe in format a specified format.
7. Display all ingredients, entered by user, in alphabetical order.

<br>

### Exercise 1.4
Coming soon

## Achievement 2
Coming soon

import pickle

with open("recipe_binary.bin", "rb") as my_file:
    recipe = pickle.load(my_file)
    
print("Recipe:")
print("_______")
print("Name: " + recipe["Name"])
print("Ingredients: " + ", ".join(recipe["Ingredients"]))
print("Cooking Time: " + str(recipe["Cooking_Time"]))
print("Difficulty: " + recipe["Difficulty"])

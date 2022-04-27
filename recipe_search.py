import requests

# function to search the API for an ingredient
def search_recipes(ingredient):
    app_id = "a0cb0c15"
    app_key = "068175e611a772b947fd4ffad584b799"
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    recipes_json = result.json()
    return recipes_json

def print_recipe(ingredient):
    # prints out each of the recipe titles, with a numerical index
    if recipes_filtered == []:
        print("No recipes - try again")
        quit()
    else:
        print(f"\nRecipes using: {ingredient}")
        i = 1
        for r in recipes_filtered:
            print(f"{i}. {r['label']}")
            i += 1
        print("\n")

# requesting the user to input an ingredient
ingredient = input('What ingredient do you want to use? ')

# calling the function to search for the users ingredient
recipe_results = search_recipes(ingredient)
recipe_titles = recipe_results['hits']

dietary = input("Do you have any of the following dietary requirements?\n1. Vegan\n2. Vegetarian\n3. Gluten-Free\n(1/2/3/no) ")

recipes_filtered = []

if dietary == '1':
    for recipe in recipe_titles:
        if "Vegan" in recipe['recipe']['healthLabels']:
            recipes_filtered.append(recipe['recipe'])
elif dietary == '2':
    for recipe in recipe_titles:
        if "Vegetarian" in recipe['recipe']['healthLabels']:
            recipes_filtered.append(recipe['recipe'])
elif dietary == '3':
    for recipe in recipe_titles:
        if "Gluten-Free" in recipe['recipe']['healthLabels']:
            recipes_filtered.append(recipe['recipe'])
else:
    for recipe in recipe_titles:
            recipes_filtered.append(recipe['recipe'])

print_recipe(ingredient)

# requesting the user to input which recipe they would like to choose using the index
choice = int(input("Which recipe would you like to choose? (number) "))
choice_index = choice - 1
chosen_recipe = recipes_filtered[choice_index]


def choose_recipe ():
    print(f"You have chosen recipe: {chosen_recipe['label']}")
    print(f"{chosen_recipe['uri'] }\n")
    ingredients = chosen_recipe['ingredientLines']
    for ingredient in ingredients:
        print(ingredient)
    print("\n")

def diet_labels():
    diet_labels = input("Would you like to see the diet labels of this recipe? (y/n) ")
    if diet_labels == 'y' and chosen_recipe['dietLabels'] != []:
        for label in chosen_recipe['dietLabels']:
            print(f"{label}")
        print("\n")
    elif diet_labels == 'n':
        print("\n")
    else:
        print("No diet labels.")

choose_recipe()
diet_labels()


def download():
    download = input("Would you like to download this recipe? (y/n) ")

# writing the recipe title and ingredients to a file depending on user choice
    if download == 'y':
        with open("recipe_download.txt", 'w+') as file:
            file.write(chosen_recipe['label'] + '\n')
            file.write("url: " + chosen_recipe['uri'] + '\n' + '\n')
            ingredients = chosen_recipe['ingredientLines']
            for ingredient in ingredients:
                file.write(ingredient + '\n')
            print("This has been downloaded into file 'recipe_download.txt'")
    else:
        print("Find another recipe to download.")

download()
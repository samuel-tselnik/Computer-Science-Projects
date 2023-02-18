import json
import drinks
inputting = 1
ingredients = []
exitAliases = ['exit', 'quit', 'done', "that's all", 'thats all', 'no more', 'esc', 'escape']

def ingredientCheck(neededIngredients, availableIngredients):
    within = True
    while within == True:
        for x in neededIngredients:
            if not x in availableIngredients:
                within = False
        return within
    return within

while inputting == 1:
    a = input('Ingredient:     ').lower()
    if a in exitAliases:
        inputting = 0
    else:
        ingredients.append(a)

makeableDrinks = []
for key in drinks.drinks.keys():
    if ingredientCheck(drinks.drinks[key]['ingredients'], ingredients) == True:
        makeableDrinks.append(key)

print(f'\n')
for x in makeableDrinks:
    print(x)

asking = True
while asking == True:
    a = input('')
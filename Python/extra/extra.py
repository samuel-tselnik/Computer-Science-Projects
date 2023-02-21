print('Loading.......')
import drinks
ingredients = []

def aliasFix(originalInput):
    fixedInput = originalInput
    searching = True
    while searching == True:
        for z in drinks.aliases:
            if originalInput in drinks.aliases[z]:
                fixedInput = z
                searching = False
        searching = False
    return fixedInput

def ingredientCheck(neededIngredients, availableIngredients):
    within = True
    while within == True:
        for x in neededIngredients:
            x = aliasFix(x)
            if not x in availableIngredients:
                passing = False
                if type(x) == list:
                    for a in x:
                        if a in availableIngredients:
                            passing = True
                    if passing == False:        
                        within = False
                else:
                    within = False
        return within
    return within

inputting = 1
while inputting == 1:
    originalInput = input('Ingredient:    ').lower()
    specNeeded = ['rum', 'orange liqueur', 'whisky', 'whiskey']
    if originalInput in specNeeded:
        originalInput = input('Specify type:   ').lower()
    fixedInput = aliasFix(originalInput)
    if fixedInput == 'Exit':
        inputting = 0
    elif fixedInput == 'not found':
        print(f"Error: Ingredient name '{originalInput}' not recognized.")
    else:
        ingredients.append(fixedInput)
        ingredients.append(originalInput)

makeableDrinks = []
for key in drinks.drinks.keys():
    if ingredientCheck(drinks.drinks[key]['ingredients'], ingredients) == True:
        makeableDrinks.append(key)

asking = True
print(f'\n')
for x in makeableDrinks:
    print(x)
if makeableDrinks == []:
    print('No drinks found.')
    asking = False

while asking == True:
    drinkName = input('Enter a drink name to learn more.     ').title()
    if drinkName in drinks.aliases['Exit']:
        asking = False
        print('Ending session...')
    elif not drinkName in drinks.drinks:
        print('Drink name not recognized.')
    else:
        subject = input('Recipe, History, or Instructions?     ').lower()
        if subject in drinks.drinks[drinkName]:
            print(drinks.drinks[drinkName][subject])
        else:
            print(f'No {subject} entry for {drinkName}')
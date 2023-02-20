aliases = {
#ADD SPECIFIC VERSIONS OF LIQUORS
    'Exit': ['exit', 'quit', 'done', "that's all", 'thats all', 'no more', 'esc', 'escape'],

    'pineapple juice': ['juiced pineapple', 'pineapple juice', 'fresh pineapple juice', 'pineapple',],
    'demerara syrup': ['dem syrup', 'demerara simple syrup', 'demerara syrup', 'demerara simple', 'dem simple',],
    'simple syrup': ['simple syrup', 'simple', 'simp syrup'],
    'sugar': ['sugar', 'sugar cube', 'cane sugar'],
    'bourbon': ['bourbon'],
    'sweet vermouth': ['sweet vermouth'],
    'dry vermouth': ['dry vermouth'],
    'orange': ['orange twist', 'orange peel', 'orange', 'orange juice', 'oj', 'oranges'],
    'rye': ['rye'],
    'angostura bitters': ['ango', 'angostura', 'ango bitters', 'angostura bitters'],
    'luxardo cherry': ['luxardo cherries', 'lux cherries', 'lux cherry', 'luxardos', 'luxardo cherry'],
    'lemon': ['lemon peel', 'lemon twist', 'lemon juice', 'lemon', 'lemons'],
    'absinthe': ['absinthe', 'absinthe rinse'],
    'peychauds bitters': ['peychauds', 'peychaud bitters', 'peychauds bitters'],
    'gin': ['gin'],
    'campari': ['campari'],
    'mint': ['mint leaves', 'mint', 'mint sprig', 'mint springs',],
    'club soda': ['soda water', 'fizzy water', 'bubbling water', 'carbonated water', 'bubly water', 'club soda',],
    'goslings rum': ['goslings', 'goslings rum', 'goslings dark rum', 'goslings black rum', 'goslings black seal rum'],
    'dark rum': ['dark rum', 'dark jamaican rum'],
    'light rum': ['light rum'],
    'rum agricole': ['agricole', 'rum agricole'],
    'cognac': ['cognac'],
    'brandy': ['brandy', 'cognac'],
    'white creme de cacao': ['white creme de cacao'],
    'creme de cacao': ['creme de cacao', 'chocolate liqueur', 'chocolate liquer'],
    'heavy cream': ['cream', 'heavy cream', 'whipping cream'],
    'lime': ['lime', 'lime juice', 'lime peel', 'lime twist', 'limes'],
    'honey syrup': ['honey', 'honey syrup'],
    'benedictine': ['benedictine'],
    'prosecco': ['prosecco'],
    'champagne': ['champagne'],
    'egg': ['egg', 'eggs'],
    'grenadine': ['grenadine', 'grenadine syrup'],
    'applejack': ['applejack'],
    'cachaca': ['cachaca'],
    'tequila': ['tequila'],
    'maraschino liqueur': ['marachino liqueur', 'marachino liquer'],
    'green chartreuse': ['green chartreuse'],
    'cocchi americano': ['cocchi americano'],
    'cointreau': ['cointreau'],
    'triple sec': ['cointreau', 'triple sec'],
    'curacao': ['orange curacao', 'curacao'],
    'orange bitters': ['orange bitters'],
    'cherry heering': ['cherry heering', 'cherry liqueur'],
    'fino sherry': ['fino sherry'],
    'ginger syrup': ['ginger syrup'],
    'ginger beer': ['ginger beer'],
    'lillet blanc': ['lillet blanc'],
    'olives': ['olive', 'olives', 'green olives'],
    'grapefruit': ['grapefruits', 'grapefruit'],
    'pisco': ['pisco'],
    'cream of coconut': ['cream of coconut'],
    'ginger ale': ['ginger ale']

}

anyRum = ['dark rum', 'light rum', 'rum agricole']
anyWhisky = ['bourbon', 'rye', 'irish whisky', 'scotch']


drinks = {

    '20th Century': {
        'ingredients': ['gin', 'cocchi americano', 'white creme de cacao', 'lemon'],
        'recipe': '\n---20TH CENTRY---\n1.5oz Gin\n0.75oz Cocchi Americano\n0.5oz White creme de cacao\n0.75oz Lemon\nLemon twist'
    },

    'Americano': {
        'ingredients': ['campari', 'sweet vermouth', 'club soda', 'orange'],
        'recipe': '\n---AMERICANO---\n1oz Campari\n1.5oz Sweet vermouth\nTop club soda\nOrange twist'
    },

    'Aperol Spritz': {
        'ingredients': ['prosecco', 'aperol', 'orange'],
        'recipe': '\n---APEROL SPRITZ---\n2oz Aperol\n3oz Prosecco\nHalf orange wheel\nSplash club soda (if available)'
    }, 

    'Bamboo': {
        'ingredients': ['dry vermouth', 'fino sherry', 'angostura bitters', 'orange bitters'],
        'recipe': '\n---BAMBOO---\n1.5oz Fino Sherry\n1.5oz Dry vermouth\n2 Dashes angostura bitters\n1 Dash orange bitters\nLemon twist'
    },

    'Bees Knees': {
        'ingredients': ['gin', 'lemon', 'honey syrup'],
        'recipe': ['\n---BEES KNEES---\n2oz Gin\n0.75 Honey Syrup\n0.75oz Lemon juice']
    },

    'Boulevardier': {
        'ingredients': ['bourbon', 'campari', 'sweet vermouth'],
        'recipe': '\n---BOULEVARDIER---\n1.5oz Bourbon\n0.75oz Campari\n0.75oz Sweet vermouth'
    },

    'Brandy Alexander': {
        'ingredients': ['brandy', 'creme de cacao', 'heavy cream'],
        'recipe': '\n---BRANDY ALEXANDER---\n1.5oz Brandy\n1oz Creme de Cacao\nTop heavy cream'
    },

    'Champagne Cocktail': {
        'ingredients': ['champagne', 'sugar cube', 'angostura bitters'],
        'recipe': '\n---CHAMPAGNE COCKTAIL---\nChampagne\nAngostura soaked (~4 dashes) sugar cube'
    },

    'Corpse Reviver No.2': {
        'ingredients': ['gin', 'cointreau', 'cocchi americano', 'lemon', 'absinthe'],
        'recipe': '\n---CORPSE REVIVER NO.2---\n0.75oz Gin\n0.75oz Cointreau\n0.75oz Cocchi Americano\n0.75oz Lemon juice\nAbsinthe rinse\nLemon twist'
    },

    'Daiquiri': {
        'ingredients': [anyRum, 'lime', 'simple syrup'],
        'recipe': '\n---DAIQUIRI---\n2oz Rum\n0.75oz Lime Juice\n0.75oz Simple Syrup\nLime Wheel'
    },

    'Daisy': {
        'ingredients': ['gin', 'club soda', 'curacao', 'lemon'],
        'recipe': '\n---DAISY---\n1.5oz Gin\n0.75oz Curacao\n0.75oz Lemon\n2 barspoons club soda\nLemon twist'
    },

    'Dark N Stormy': {
        'ingredients': ['goslings rum', 'lime', 'ginger syrup', 'ginger beer'],
        'recipe': '\n---DARK N STORMY---\n2oz Goslings rum\n0.5oz Lime\n0.75oz Ginger syrup\nTop ginger beer\nLime wheel'
    },

    'French 75': {
        'ingredients': ['champagne', 'gin', 'lemon', 'simple syrup',],
        'recipe': '\n---FRENCH 75---\n1oz Gin\n0.5oz Lemon\n0.5oz Simple\nTop champagne\nLong lemon twist'
    },

    'Gin Fix': {
        'ingredients': ['gin', 'lemon', 'simple syrup'],
        'recipe': '\n---GIN FIX---\n2oz Gin\n0.75oz Lemon\nSimple syrup\nLemon wheel'
    },

    'Gin Rickey': {
        'ingredients': ['gin', 'lime', 'club soda'],
        'recipe': '\n---GIN RICKEY---\n2oz Gin\n4 Lime wedges\nTop club soda'
    },

    'Hemingway Daiquiri': {
        'ingredients': ['maraschino liqueur', anyRum, 'grapefruit', 'lime'],
        'recipe': '\n---HEMINGWAY DAIQUIRI---\n1.5oz Rum\n0.75oz Maraschino Liqueur\n1oz Grapefruit\n0.5oz Lime\nLime wheel'
    },

    'Improved Whisky Cocktail': {
        'ingredients': ['rye', 'absinthe', 'maraschino liqueur', 'peychauds bitters', 'angostura bitters', 'sugar', 'lemon'],
        'recipe': '\n---IMPROVED WHISKY COCKTAIL---\n2oz Rye\nBarspoon absinthe\nBarspoon maraschino liqueur\n1 dash peychauds\n1 dash angostura\nSugar cube\nLemon twist'
    },

    'Jack Rose': {
        'ingredients': ['applejack', 'lime', 'grenadine', 'lime'],
        'recipe': '\n---JACK ROSE---\n2oz Applejack\n0.75oz Lime juice\n0.75oz Grenadine\nLime wheel'
    },

    'Last Word': {
        'ingredients': ['gin', 'green chartreuse', 'marachino liqueur', 'lime'],
        'recipe': '\n---LAST WORD---\n0.75oz Gin\n0.75oz Green Chartreuse\n0.75oz Maraschino Liqueuer\n0.75oz Lime juice'
    },

    'Manhattan': {
        'ingredients': [['bourbon', 'rye'], 'sweet vermouth', 'luxardo cherry', 'angostura bitters'],
        'recipe': '\n---MANHATTAN---\n2oz Bourbon or Rye\n1oz Sweet Vermouth\n4 Dashes Angostura Bitters'
    },
    
    'Martinez': {
        'ingredients': ['gin', 'sweet vermouth', 'maraschino liqueuer', 'orange bitters'],
        'recipe': '\n---MARTINEZ---\n1.5oz Gin\n1.5oz Sweet Vermouth\n1 barspoon maraschino liqueuer\n2 dashes orange bitters\nLemon twist'
    },

    'Mexican Firing Squad Special': {
        'ingredients': ['tequila', 'lime', 'grenadine', 'angostura bitters', 'lime',],
        'recipe': '\n---MEXICAN FIRING SQUAD SPECIAL---\n0.75oz Lime\n0.75oz Grenadine\n3-4 Dashes angostura\nLime wedge\nLuxardo cherry'
    },

    'Mint Julep': {
        'ingredients': ['mint', 'bourbon', 'simple syrup', 'sugar'],
        'recipe': '\n---MINT JULEP---\n2oz Bourbon\n0.25oz Simple Syrup\n4-5 Mint Leaves\n1 Sugar Cube\nMint Sprig'
    },

    'Monte Carlo': {
        'ingredients': ['rye', 'benedictine', 'angostura bitters', 'lemon'],
        'recipe': '\n---MONTE CARLO---\n2oz Rye\n0.5oz Benedictine\n3-4 Dashes angostura bitters\nLemon twist'
    },

    'Moscow Mule': {
        'ingredients': ['ginger beer', 'vodka', 'lime'], 
        'recipe': '\n---MOSCOW MULE---\n2oz Vodka\n0.75oz Lime\nTop ginger beer\nLime wheel'
    },

    'Negroni': {
        'ingredients': ['gin', 'campari', 'sweet vermouth', 'orange'],
        'recipe': '\n---NEGRONI---\n1oz Gin\n1oz Campari\n1oz Sweet Vermouth\nOrange Twist'
    },

    'Old Fashioned': {
        'ingredients': [['bourbon', 'rye'], ['simple syrup', 'sugar', 'demerara syrup'], 'orange', 'angostura bitters'],
        'recipe': '\n---OLD FASHIONED---\n2oz Bourbon or Rye\n0.5oz Simple, Demerara, or a Sugar Cube\n4 Dashes Angostura Bitters\nOrange Twist\nLemon Twist or Luxardo Cherry if desired',
    },

    'Pink Lady': {
        'ingredients': ['egg', 'grenadine', 'gin', 'applejack'],
        'recipe': '\n---PINK LADY---\n1oz Gin\n1oz Applejack\n0.75oz Lemon juice\n0.75oz Grenadine\nEgg white'
    },

    'Pisco Sour': {
        'ingredients': ['egg', 'lemon', 'simple syrup', 'pisco', 'lime', 'angostura bitters'],
        'recipe': '\n---PISCO SOUR---\n0.75oz Simple\n0.75oz Lemon-Lime\nEgg white\nAngostura bitters garnish'
    },
    
    'Presbyterian': {
        'ingredients': [anyWhisky, 'ginger beer', 'club soda'],
        'recipe': '\n---PRESBYTERIAN---\n2oz Whisky\nTop Ginger beer & club soda'
    },

    'Rye Buck': {
        'ingredients': ['rye', 'ginger syrup', 'club soda', 'lime', 'angostura bitters'],
        'recipe': '\n---RYE BUCK---\n2oz Rye\n0.75oz Ginger syrup\n0.5oz Lime\n2 dashes angostura\nTop club soda\nLime twist'
    },

    'Sazerac': {
        'ingredients': ['rye', 'absinthe', 'peychauds bitters', ['simple syrup', 'sugar'], 'lemon'],
        'recipe': '\n---SAZERAC---\n2oz Rye\n4 Dashes Peychauds Bitters\nAbsinthe Rinse\nLemon Twist'
    },

    'Silver Fizz': {
        'ingredients': ['lemon', 'simple syrup', 'gin', 'egg', 'club soda'],
        'recipe': '\n---SILVER FIZZ---\n1.5oz Gin\n0.75oz Simple syrup\n0.75oz Lemon\nEgg white'
    },

    'Singapore Sling': {
        'ingredients': ['gin', 'cointreau', 'cherry heering', 'beneditcine', 'triple sec', 'lime', 'grenadine', 'pineapple', 'angostura bitters', 'club soda', 'grenadine', 'pineapple'],
        'recipe': '\n---SINGAPORE SLING---\n1.5oz Gin\n0.25oz Cherry Heering\n0.25oz Benedictine\n0.25oz Cointreau\n1oz Lime\n0.25oz Grenadine\n0.75oz Pineapple juice\n1 dash angostura\nTop club soda\nPineapple & Luxardo cherry'
    },

    'Tom Collins': {
        'ingredients': ['gin', 'lemon', 'simple syrup', 'club soda', 'luxardo cherry'],
        'recipe': '\n---TOM COLLINS---\n2oz Gin\n0.75oz Lemon Juice\n0.75oz Simple Syrup\nTop Club Soda\nLemon Twist\nLuxardo Cherry'
    },

    'Vesper Martini': {
        'ingredients': ['gin', 'vodka', 'lillet blanc', 'lemon'],
        'recipe': '\n---VESPER---\n2oz Gin\n1oz Vodka\n0.5oz Lillet Blanc\nLemon twist'
    },

    'Vieux Carre': {
        'ingredients': ['rye', 'cognac', 'sweet vermouth', 'benedictine', 'angostura bitters', 'peychauds bitters', 'orange'],
        'recipe': '\n---VIEUX CARRE---\n1oz Rye\n1oz Cognac\n1oz Sweet vermouth\n0.25oz Benedictine\n2 Dashes angostura\n2 Dashes peychauds\nOrange twist\nLuxardo cherry'
    },

    'Vodka Martini': {
        'ingredients': ['vodka', 'dry vermouth', 'olives'],
        'recipe': '\n---VODKA MARTINI---\n2.25oz Vodka\n0.75oz Dry Vermouth\nOlive'
    },

    'Whisky Smash': {
        'ingredients': ['mint', 'sugar', 'simple syrup', 'lemon', anyWhisky],
        'recipe': '\n---WHISKY SMASH---\n2oz Whisky\n0.5oz Simple\n6-8 Mint leaves\n4 Lemon wedges\nSugar cube\nMint sprig'
    },

    'Whisky Sour': {
        'ingredients': ['egg', anyWhisky, 'lemon', 'simple syrup', 'whisky sour'],
        'recipe': '\n---WHISKY SOUR---\n2oz Whisky\n0.75oz Lemon\n0.75oz Simple syrup\nEgg white\nAngostura bitters garnish'
    },


#   MOCKTAILS


    'Mini Colada': {
        'ingredients': ['milk', 'cream of coconut', 'pineapple'],
        'recipe': '\n---MINI COLADA---\n5.25oz Milk\n2.5oz Cream of coconut\n3.5oz Pineapple\nPineapple chunk & Frawn\nLuxardo cherry'
    },

    'Shirley Temple': {
        'ingredients': ['lemon', 'grenadine', 'simple syrup', 'ginger ale'],
        'recipe': '\n---SHIRLEY TEMPLE---\n1.75oz Lemon\n0.5oz Grenadine\n0.5oz Simple\nTop ginger ale\nOrange twist'
    },

    
}
aliases = {
#ADD SPECIFIC VERSIONS OF LIQUORS
    'Exit': ['exit', 'quit', 'done', "that's all", 'thats all', 'no more', 'esc', 'escape'],

    'pineapple juice': ['juiced pineapple', 'pineapple juice', 'fresh pineapple juice', 'pineapple',],
    'demerara syrup': ['dem syrup', 'demerara simple syrup', 'demerara syrup', 'demerara simple', 'dem simple',],
    'simple syrup': ['simple syrup', 'simple', 'simp syrup'],
    'sugar': ['sugar', 'sugar cube', 'cane sugar'],
    'bourbon': ['bourbon'],
    'sweet vermouth': ['sweet vermouth'],
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
    'dark rum': ['dark rum', 'dark jamaican rum'],
    'light rum': ['light rum'],
    'rum agricole': ['agricole', 'rum agricole'],
    'brandy': ['brandy', 'cognac',],
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

}

anyRum = ['dark rum', 'light rum', 'rum agricole']


drinks = {

    'Old Fashioned': {
        'ingredients': [['bourbon', 'rye'], ['simple syrup', 'sugar', 'demerara syrup'], 'orange', 'angostura bitters'],
        'recipe': '\n---OLD FASHIONED---\n2oz Bourbon or Rye\n0.5oz Simple, Demerara, or a Sugar Cube\n4 Dashes Angostura Bitters\nOrange Twist\nLemon Twist or Luxardo Cherry if desired',
    },

    'Manhattan': {
        'ingredients': [['bourbon', 'rye'], 'sweet vermouth', 'luxardo cherry', 'angostura bitters'],
        'recipe': '\n---MANHATTAN---\n2oz Bourbon or Rye\n1oz Sweet Vermouth\n4 Dashes Angostura Bitters'
    },
    
    'Sazerac': {
        'ingredients': ['rye', 'absinthe', 'peychauds bitters', ['simple syrup', 'sugar'], 'lemon'],
        'recipe': '\n---SAZERAC---\n2oz Rye\n4 Dashes Peychauds Bitters\nAbsinthe Rinse\nLemon Twist'
    },

    'Negroni': {
        'ingredients': ['gin', 'campari', 'sweet vermouth', 'orange'],
        'recipe': '\n---NEGRONI---\n1oz Gin\n1oz Campari\n1oz Sweet Vermouth\nOrange Twist'
    },

    'Mint Julep': {
        'ingredients': ['mint', 'bourbon', 'simple syrup', 'sugar'],
        'recipe': '\n---MINT JULEP---\n2oz Bourbon\n0.25oz Simple Syrup\n4-5 Mint Leaves\n1 Sugar Cube\nMint Sprig'
    },

    'Tom Collins': {
        'ingredients': ['gin', 'lemon', 'simple syrup', 'club soda', 'luxardo cherry'],
        'recipe': '\n---TOM COLLINS---\n2oz Gin\n0.75oz Lemon Juice\n0.75oz Simple Syrup\nTop Club Soda\nLemon Twist\nLuxardo Cherry'
    },

    'Daiquiri': {
        'ingredients': [anyRum, 'lime', 'simple syrup'],
        'recipe': '\n---DAIQUIRI---\n2oz Rum\n0.75oz Lime Juice\n0.75oz Simple Syrup\nLime Wheel'
    },

    'Brandy Alexander': {
        'ingredients': ['brandy', 'creme de cacao', 'heavy cream'],
        'recipe': '\n---BRANDY ALEXANDER---\n1.5oz Brandy\n1oz Creme de Cacao\nTop heavy cream'
    },

    'Improved Whisky Cocktail': {
        'ingredients': ['rye', 'absinthe', 'maraschino liqueur', 'peychauds bitters', 'angostura bitters', 'sugar']
    },

    'Gin Rickey': {
        'ingredients': ['gin', 'lime', 'club soda'],
        'recipe': '\n---GIN RICKEY---\n2oz Gin\n4 Lime wedges\nTop club soda'
    },

    'Bees Knees': {
        'ingredients': ['gin', 'lemon', 'honey syrup'],
        'recipe': ['\n---BEES KNEES---\n2oz Gin\n0.75 Honey Syrup\n0.75oz Lemon juice']
    },

    'Monte Carlo': {
        'ingredients': ['rye', 'benedictine', 'angostura bitters', 'lemon'],
        'recipe': '\n---MONTE CARLO---\n2oz Rye\n0.5oz Benedictine\n3-4 Dashes angostura bitters\nLemon twist'
    },

    'Boulevardier': {
        'ingredients': ['bourbon', 'campari', 'sweet vermouth'],
        'recipe': '\n---BOULEVARDIER---\n1.5oz Bourbon\n0.75oz Campari\n0.75oz Sweet vermouth'
    },

    'Aperol Spritz': {
        'ingredients': ['prosecco', 'aperol', 'orange'],
        'recipe': '\n---APEROL SPRITZ---\n2oz Aperol\n3oz Prosecco\nHalf orange wheel\nSplash club soda (if available)'
    }, 

    'Champagne Cocktail': {
        'ingredients': ['champagne', 'sugar cube', 'angostura bitters'],
        'recipe': '\n---CHAMPAGNE COCKTAIL---\nChampagne\nAngostura soaked (~4 dashes) sugar cube'
    },

    'Pink Lady': {
        'ingredients': ['egg', 'grenadine', 'gin', 'applejack'],
        'recipe': '\n---PINK LADY---\n1oz Gin\n1oz Applejack\n0.75oz Lemon juice\n0.75oz Grenadine\nEgg white'
    },

    'Jack Rose': {
        'ingredients': ['applejack', 'lime', 'grenadine', 'lime'],
        'recipe': '\n---JACK ROSE---\n2oz Applejack\n0.75oz Lime juice\n0.75oz Grenadine\nLime wheel'
    },

    'Mexican Firing Squad Special': {
        'ingredients': ['tequila', 'lime', 'grenadine', 'angostura bitters', 'lime',],
        'recipe': '\n---MEXICAN FIRING SQUAD SPECIAL---\n0.75oz Lime\n0.75oz Grenadine\n3-4 Dashes angostura\nLime wedge\nLuxardo cherry'
    },

    'Last Word': {
        'ingredients': ['gin', 'green chartreuse', 'marachino liqueur', 'lime'],
        'recipe': '\n---LAST WORD---\n0.75oz Gin\n0.75oz Green Chartreuse\n0.75oz Maraschino Liqueuer\n0.75oz Lime juice'
    },

    'Corpse Reviver No.2': {
        'ingredients': ['gin', 'cointreau', 'cocchi americano', 'lemon', 'absinthe'],
        'recipe': '\n---CORPSE REVIVER NO.2---\n0.75oz Gin\n0.75oz Cointreau\n0.75oz Cocchi Americano\n0.75oz Lemon juice\nAbsinthe rinse\nLemon twist'
    },

    'Martinez': {
        'ingredients': ['gin', 'sweet vermouth', 'maraschino liqueuer', 'orange bitters'],
        'recipe': '\n---MARTINEZ---\n1.5oz Gin\n1.5oz Sweet Vermouth\n1 barspoon maraschino liqueuer\n2 dashes orange bitters\nLemon twist'
    },

    'Singapore Sling': {
        'ingredients': ['gin', 'cointreau', 'cherry heering', 'beneditcine', 'triple sec', 'lime', 'grenadine', 'pineapple', 'angostura bitters', 'club soda', 'grenadine', 'pineapple'],
        'recipe': '\n---SINGAPORE SLING---\n1.5oz Gin\n0.25oz Cherry Heering\n0.25oz Benedictine\n0.25oz Cointreau\n1oz Lime\n0.25oz Grenadine\n0.75oz Pineapple juice\n1 dash angostura\nTop club soda\nPineapple & Luxardo cherry'
    },

    'Silver Fizz': {
        'ingredients': ['lemon', 'simple syrup', 'gin', 'egg', 'club soda'],
        'recipe': '\n---SILVER FIZZ---\n1.5oz Gin\n0.75oz Simple syrup\n0.75oz Lemon\nEgg white'
    },

    'Daisy': {
        'ingredients': ['gin', 'club soda', 'curacao', 'lemon'],
        'recipe': '\n---DAISY---\n1.5oz Gin\n0.75oz Curacao\n0.75oz Lemon\n2 barspoons club soda\nLemon twist'
    },

    'Americano': {
        'ingredients': ['campari', 'sweet vermouth', 'club soda', 'orange'],
        'recipe': '\n---AMERICANO---\n1oz Campari\n1.5oz Sweet vermouth\nTop club soda\nOrange twist'
    }
    
}
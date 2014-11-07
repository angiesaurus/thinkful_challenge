import sys
import random
import getopt

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

#print questions.values()
#print ingredients.keys()

desired_ingredients = []
key = questions.keys()
yes_list = ['y', 'yes']

def drink_preference(dictionary):
    for i in range(len(questions.values())):
        if raw_input(questions.values()[i]) in yes_list:
            desired_ingredients.append(key[i])
#    print desired_ingredients
            wanted_ingredients = {}
            for i in desired_ingredients:
                wanted_ingredients[i] = []
#    print wanted_ingredients

    ingredient_key = ingredients.keys()
    ingredient_list = []
    for i in range(len(wanted_ingredients.keys())):
        if wanted_ingredients.keys()[i] in ingredient_key:
            ingredient_list.append(random.choice(ingredients.values()[i]))
    print ingredient_list
    
if __name__=="__main__":
    drink_preference(questions)
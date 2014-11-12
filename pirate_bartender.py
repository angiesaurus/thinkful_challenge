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


key = questions.keys()

def drink_preference():
    desired_ingredients = {}
    for i in questions:
        response = raw_input(questions[i] + " ")
        desired_ingredients[i] = True if (response == 'y' or response == 'yes') else False
    return desired_ingredients


def make_drink():
    drink = []
    for i in desired_ingredients:
        if desired_ingredients[i]:
            drink.append(random.choice(ingredients[i]))
    print '-'*80+ '\nYour drink is ' + ', '.join(drink)


if __name__=="__main__":
    desired_ingredients = drink_preference()
    make_drink()
#Capitals guessing game but with functions

from random import choice

capitals = {
    'Albania':	'Tirana',
    'Austria':	'Vienna',
    'Belarus':	'Minsk',
    'Belgium':	'Brussels',
    'Bulgaria': 'Sofia',
    'Croatia':	'Zagreb',
    'Czechia':	'Prague',
    'Denmark':	'Copenhagen',
    'Estonia':	'Tallinn',
    'Finland':	'Helsinki',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Greece': 'Athens',
    'Hungary': 'Budapest',
    'Iceland': 'Reykjavik',
    'Ireland':	'Dublin',
    'Italy': 'Rome',
    'Latvia': 'Riga',
    'Lithuania': 'Vilnius',
    'Luxembourg': 'Luxembourg',
    'Netherlands': 'Amsterdam',
    'Norway': 'Oslo',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Romania': 'Bucharest',
    'Slovakia': 'Bratislava',
    'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Ukraine': 'Kiev',
    'UnitedKingdom': 'London',
}

def new_game():

    guesses = 0
    correct_guesses = 0
    country = choice(list(capitals.keys()))
    capital = capitals[country]
    print("--------------")
    print(country)
    print("--------------")

    answer = input("Enter the capital: ")
    if answer == capital:
        print("Correct, +1 Score")
        correct_guesses += 1
    else:
        print("Wrong!")
        correct_guesses += 0
        print(f"Correct answer: {capital}")
    
    guesses += 1
    print(f"You tried {guesses} times")

    while play_again() == True:

        country = choice(list(capitals.keys()))
        capital = capitals[country]
        print("--------------")
        print(country)
        print("--------------")
        
        answer = input("Enter the capital: ")
        if answer == capital:
            print("Correct, +1 Score")
            correct_guesses += 1
            print(f"You've got {correct_guesses} score!")
        else:
            print("Wrong!")
            correct_guesses += 0
            print(f"You've got {correct_guesses} score")
            print(f"Correct answer: {capital}")

        guesses += 1
        print(f"You tried {guesses} times")
        
    else:
        print("Byeee")
        quit

def play_again():
    
    playagain = input("Do you want to play again? y/n: ")
    
    if playagain == "y":
        return True
    else:
        return False  

new_game()
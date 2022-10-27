#Simple "Guessing Game" 
from random import choice

points = 0
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
    'United': 'Kingdom London',
}

yn = input("Hello! Do you want to play a game? y/n: ")
if yn == "n":
    quit()

while yn != "n":
    selected_country = choice(list(capitals.keys()))

    print(f"Guess the capitals of European Countries! Your points: {points}")

    capital = input(f"Whats the capital of {selected_country}? ")
    if capitals[selected_country] == capital:
        print("You are right! +1 point")
        points += 1
        print(f"You've got {points} points!")
    else:
        print("You are wrong!")
        print(f"Correct answer: {capitals[selected_country]}")
        print(f"You've got {points} points!")
    yn = input("Play again? y/n: ")
print(f"Thank you for playing. Your final score {points}")
import requests
from random import randint

url = ("https://icanhazdadjoke.com/search")   # Adding search at the end so I can add parameters

userInput = input("What joke do you want to search for? ")

# Searches for whatever user inputted
response = requests.get(url, headers={"Accept": "application/json"}, params={"term": (userInput)})

data = response.json()      # Returns a dictionary with all the data; all the jokes have the key "result"

joke = data["results"]      # ["results] returns all jokes as a list

# If there is no joke returns Try again! Otherwise outputs the joke
if joke == []:
    print("Try again!")
else:
    # Added functionality to choose a random joke and not just the same one each time
    index = randint(0, (len(joke)-1))

    joke = joke[index]  # This returns the first joke as a dictionary along with its key

    joke = list(joke.values())  # This returns a list where the joke is at index [1]

    joke = joke[1]
    print(joke)

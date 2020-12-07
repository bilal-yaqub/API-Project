import requests

url = ("https://icanhazdadjoke.com/search")   # Adding search at the end so I can add parameters

# Requests for the file in JavaScript Object Notation
response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()      # Returns a dictionary with all the data; all the jokes have the key "result"

joke = data["results"]      # ["results] returns all jokes as a list

joke = joke[0]  # This returns the first joke as a dictionary along with its key

joke = list(joke.values())  # This returns a list with the joke at index [1]

joke = joke[1]
print(joke)

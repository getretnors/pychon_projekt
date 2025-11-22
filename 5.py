import requests

API_KEY = "14131132"
BASE_URL = "https://www.omdbapi.com/"

print("welcome")
print("Enter movie name: ")
print("Text 'exit' to leave")

while True:
    movieName = input("Enter movie name you want to find: ")

    if movieName.lower() == 'exit':
        print("bye")
        break
    
    params = {
        "t": movieName,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["Response"] == "False":
        print("Error film not found")
    else:
        print(f"name: {data['Title']}")
        print(f"year: {data['Year']}")
        print(f"Released: {data['Released']}")
        print(f"Runtime: {data['Runtime']}")
        print(f"Genre: {data['Genre']}")
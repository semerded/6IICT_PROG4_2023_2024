# Request om een grap af te halen van JokeAPI.
import requests

url = "https://v2.jokeapi.dev/joke/Any"
response = requests.get(url)

print(response)        # <Response [200]>
print(response.json()) # Data in JSON-formaat
print("#"*40) # Scheiding in opdrachtprompt

response_json = response.json()
if response_json["type"] == "single":
    print(response_json["joke"])
else:
    print(response_json["setup"])    # De setup
    print(response_json["delivery"]) # De punchline


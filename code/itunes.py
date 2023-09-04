import requests, sys , json

if len(sys.argv) < 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

print(response, "\n", response.json())

print(json.dumps(response.json(), indent = 1))

for i in response.json()["results"]:
    print(i["trackName"])
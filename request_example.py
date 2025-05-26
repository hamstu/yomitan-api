import requests

params = {
    "term": "わかる",
    "profileIndex": 0
}
response = requests.post("http://127.0.0.1:8766/termEntries", json = params)
print(response)
print(response.text)

import requests

params = {
    "text": "わかる",
    "details": {},
    "optionsContext": {"index": 0}
}
response = requests.post("http://127.0.0.1:8766/termsFind", json = params)
print(response)
print(response.text)

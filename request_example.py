import requests

request_url = "http://127.0.0.1:8766"

def elide(text):
    if len(text) > 100:
        return text[:100] + "..."
    return text

def termEntries():
    print("Requesting termEntries:")
    params = {
        "term": "わかる",
        "profileIndex": 0
    }
    response = requests.post(request_url + "/termEntries", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

def kanjiEntries():
    print("Requesting kanjiEntries:")
    params = {
        "character": "分",
        "profileIndex": 0
    }
    response = requests.post(request_url + "/kanjiEntries", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

print("Yomitan API request example demo")
print("Only the first 100 characters of the result data for each request will be printed")
print("--------------------------------------------------")
termEntries()
kanjiEntries()

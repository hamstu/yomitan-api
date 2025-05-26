import requests

request_url = "http://127.0.0.1:8766"

def termEntries():
    print("Requesting termEntries:")
    params = {
        "term": "わかる",
        "profileIndex": 0
    }
    response = requests.post(request_url + "/termEntries", json = params)
    print(response)
    print(str(response.json()["data"])[:100] + "...")

def kanjiEntries():
    print("Requesting kanjiEntries:")
    params = {
        "character": "分",
        "profileIndex": 0
    }
    response = requests.post(request_url + "/kanjiEntries", json = params)
    print(response)
    print(str(response.json()["data"])[:100] + "...")

print("Yomitan API request example demo")
print("Only the first 100 characters of the result data for each request will be printed")
print("--------------------------------------------------")
termEntries()
kanjiEntries()

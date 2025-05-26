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
    }
    response = requests.post(request_url + "/termEntries", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

def kanjiEntries():
    print("Requesting kanjiEntries:")
    params = {
        "character": "分",
    }
    response = requests.post(request_url + "/kanjiEntries", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

def ankiFields():
    print("Requesting ankiFields:")
    params = {
        "text": "わかる",
        "type": "term",
        "handlebar": "glossary",
    }
    response = requests.post(request_url + "/ankiFields", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

print("Yomitan API request example demo")
print("Only the first 100 characters of the result data for each request will be printed")
print("--------------------------------------------------")
termEntries()
kanjiEntries()
ankiFields()

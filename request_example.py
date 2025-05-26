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

def ankiFields_term():
    print("Requesting ankiFields type term:")
    params = {
        "text": "わかる",
        "type": "term",
        "markers": ["audio", "cloze-body-kana", "conjugation", "expression", "furigana", "furigana-plain", "glossary", "glossary-brief", "glossary-no-dictionary", "glossary-first", "glossary-first-brief", "glossary-first-no-dictionary", "part-of-speech", "phonetic-transcriptions", "pitch-accents", "pitch-accent-graphs", "pitch-accent-graphs-jj", "pitch-accent-positions", "pitch-accent-categories", "reading", "tags", "clipboard-image", "clipboard-text", "cloze-body", "cloze-prefix", "cloze-suffix", "dictionary", "dictionary-alias", "document-title", "frequencies", "frequency-harmonic-rank", "frequency-harmonic-occurrence", "frequency-average-rank", "frequency-average-occurrence", "screenshot", "search-query", "popup-selection-text", "sentence", "sentence-furigana", "sentence-furigana-plain", "url"],
        "maxEntries": 1,
    }
    response = requests.post(request_url + "/ankiFields", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

def ankiFields_kanji():
    print("Requesting ankiFields type kanji:")
    params = {
        "text": "分",
        "type": "kanji",
        "markers": ["character", "glossary", "kunyomi", "onyomi", "onyomi-hiragana", "stroke-count", "clipboard-image", "clipboard-text", "cloze-body", "cloze-prefix", "cloze-suffix", "dictionary", "dictionary-alias", "document-title", "frequencies", "frequency-harmonic-rank", "frequency-harmonic-occurrence", "frequency-average-rank", "frequency-average-occurrence", "screenshot", "search-query", "popup-selection-text", "sentence", "sentence-furigana", "sentence-furigana-plain", "url"],
        "maxEntries": 1,
    }
    response = requests.post(request_url + "/ankiFields", json = params)
    print(response)
    print(elide(str(response.json()["data"])))

print("Yomitan API request example demo")
print("Only the first 100 characters of the result data for each request will be printed")
print("--------------------------------------------------")
termEntries()
kanjiEntries()
ankiFields_term()
ankiFields_kanji()

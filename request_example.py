import requests

request_url = "http://127.0.0.1:19633"
request_timeout = 10

def elide(text: str) -> str:
    elide_max_length = 100
    if len(text) > elide_max_length:
        return text[:100] + "..."
    return text

def yomitan_version() -> None:
    print("Requesting yomitanVersion:")
    response = requests.post(request_url + "/yomitanVersion", timeout = request_timeout)
    print(response)
    print(response.text)

def term_entries() -> None:
    print("Requesting termEntries:")
    params = {
        "term": "わかる",
    }
    response = requests.post(request_url + "/termEntries", json = params, timeout = request_timeout)
    print(response)
    print(elide(response.text))

def kanji_entries() -> None:
    print("Requesting kanjiEntries:")
    params = {
        "character": "分",
    }
    response = requests.post(request_url + "/kanjiEntries", json = params, timeout = request_timeout)
    print(response)
    print(elide(response.text))

def anki_fields_term() -> None:
    print("Requesting ankiFields type term:")
    params = {
        "text": "わかる",
        "type": "term",
        "markers": ["audio", "cloze-body-kana", "conjugation", "expression", "furigana", "furigana-plain", "glossary", "glossary-brief", "glossary-no-dictionary", "glossary-first", "glossary-first-brief", "glossary-first-no-dictionary", "part-of-speech", "phonetic-transcriptions", "pitch-accents", "pitch-accent-graphs", "pitch-accent-graphs-jj", "pitch-accent-positions", "pitch-accent-categories", "reading", "tags", "clipboard-image", "clipboard-text", "cloze-body", "cloze-prefix", "cloze-suffix", "dictionary", "dictionary-alias", "document-title", "frequencies", "frequency-harmonic-rank", "frequency-harmonic-occurrence", "frequency-average-rank", "frequency-average-occurrence", "screenshot", "search-query", "popup-selection-text", "sentence", "sentence-furigana", "sentence-furigana-plain", "url"],
        "maxEntries": 1,
        "includeMedia": False,
    }
    response = requests.post(request_url + "/ankiFields", json = params, timeout = request_timeout)
    print(response)
    print(elide(response.text))

def anki_fields_kanji() -> None:
    print("Requesting ankiFields type kanji:")
    params = {
        "text": "分",
        "type": "kanji",
        "markers": ["character", "glossary", "kunyomi", "onyomi", "onyomi-hiragana", "stroke-count", "clipboard-image", "clipboard-text", "cloze-body", "cloze-prefix", "cloze-suffix", "dictionary", "dictionary-alias", "document-title", "frequencies", "frequency-harmonic-rank", "frequency-harmonic-occurrence", "frequency-average-rank", "frequency-average-occurrence", "screenshot", "search-query", "popup-selection-text", "sentence", "sentence-furigana", "sentence-furigana-plain", "url"],
        "maxEntries": 1,
        "includeMedia": False,
    }
    response = requests.post(request_url + "/ankiFields", json = params, timeout = request_timeout)
    print(response)
    print(elide(response.text))

def tokenize() -> None:
    print("Requesting tokenize:")
    params = {
        "text": "自民党の総裁選挙",
        "scanLength": 10,
    }
    response = requests.post(request_url + "/tokenize", json = params, timeout = request_timeout)
    print(response)
    print(elide(response.text))

print("Yomitan API request example demo")
print("Only the first 100 characters of the result data for each request will be printed")
print("--------------------------------------------------")
yomitan_version()
term_entries()
kanji_entries()
anki_fields_term()
anki_fields_kanji()
tokenize()

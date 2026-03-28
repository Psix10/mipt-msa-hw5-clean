import re
import requests
from collections import Counter


URL = "https://eng.mipt.ru/why-mipt/"
WORDS_FILE = "words.txt"


def get_clean_words(url: str) -> list[str]:
    resp = requests.get(url)
    resp.raise_for_status()
    text = resp.text.lower()
    text = re.sub(r"[^a-z0-9а-яё\s]", " ", text)
    return text.split()


def load_words_to_count(path: str) -> list[str]:
    words = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.append(word)
    return words


def main():
    words = get_clean_words(URL)
    freq = Counter(words)

    target_words = load_words_to_count(WORDS_FILE)

    result = {w: freq.get(w, 0) for w in target_words}
    print(result)


if __name__ == "__main__":
    main()
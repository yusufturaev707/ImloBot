from uzwords import words
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words, 10))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words, 10))
    elif 't' in word:
        word = word.replace('t', 'd')
        matches.update(get_close_matches(word, words, 10))
    elif 'd' in word:
        word = word.replace('d', 't')
        matches.update(get_close_matches(word, words, 10))
    elif 'k' in word:
        word = word.replace('k', 'q')
        matches.update(get_close_matches(word, words, 10))
    elif 'q' in word:
        word = word.replace('q', 'k')
        matches.update(get_close_matches(word, words, 10))
    elif 'p' in word:
        word = word.replace('p', 'b')
        matches.update(get_close_matches(word, words, 10))
    elif 'b' in word:
        word = word.replace('b', 'p')
        matches.update(get_close_matches(word, words, 10))
    elif 'v' in word:
        word = word.replace('v', 'f')
        matches.update(get_close_matches(word, words, 10))
    elif 'f' in word:
        word = word.replace('f', 'v')
        matches.update(get_close_matches(word, words, 10))

    return {'available': available, 'matches': matches}


if __name__ == '__main__':
    print(checkWord('тарих'))
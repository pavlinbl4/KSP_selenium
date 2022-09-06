import string
from random_word import RandomWords


def make_random_voc(n):
    r = RandomWords()
    words = r.get_random_words(limit=n)
    alphabet = string.ascii_uppercase
    return {alphabet[x]:words[x] for x in range(n)}




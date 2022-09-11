__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Set

################################################################################

def load_words(path: str) -> Set[str]:
    """
    Returns set of words from the dictionary file that are longer than one
    letter, unless the word is "a" or "i".

    :return: set of words from the dictionary file
    """

    with open(path, "r") as f:
        words = set(word.strip().lower() for word in f.readlines())
        words = set(filter(lambda word: len(word) > 1 or word == "a" or word == "i", words))
        return words

################################################################################
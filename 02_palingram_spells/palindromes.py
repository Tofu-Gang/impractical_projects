__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from utils.utils import load_words

################################################################################

DICT_PATH = "../utils/2of4brif.txt"

################################################################################

def is_palindrome(word: str) -> bool:
    """
    Challenge project from page 34.
    Recursively checks if the first and last letter of the word is the same,
    then cuts the first and last letter from the word. This process repeats
    until the word has the length 0 or 1 letter, in which case the word is
    indeed a palindrome.

    :param word: input word
    :return: True if the input word is a palindrome, False otherwise
    """

    if len(word) > 1:
        return word[0] == word[-1] and is_palindrome(word[1:-1])
    else:
        return True

################################################################################

if __name__ == '__main__':
    words = load_words(DICT_PATH)
    palindromes = tuple(filter(lambda word: word == word[::-1], words))
    palindromes_recursive = tuple(filter(lambda word: is_palindrome(word), words))
    print("Results of recursive and non-recursive approach are the same:", palindromes == palindromes_recursive)
    print("Palindromes from the dict file", DICT_PATH + ":")
    print(*palindromes, sep="\n")

################################################################################
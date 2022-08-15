__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from src.utils import load_words
from palindromes import is_palindrome

################################################################################

DICT_PATH = "src/2of4brif.txt"

################################################################################

if __name__ == '__main__':
    words = load_words(DICT_PATH)

    palingrams = []
    for core_word in words:
        for delimiter in range(len(core_word)):
            left = core_word[:delimiter]
            right = core_word[delimiter:]

            # reversed word|palindromic sequence
            # core word = nurses
            # reversed word = nur (run)
            # palindromic sequence = ses
            # nurses run
            if left[::-1] in words and is_palindrome(right):
                palingrams.append(core_word + " " + left[::-1])

            # palindromic sequence|reverse word
            # core word = grits
            # palindromic sequence = g
            # reversed word = rits (stir)
            # stir grits
            if right[::-1] in words and is_palindrome(left):
                palingrams.append(right[::-1] + " " + core_word)
    print("Palingrams from the dict file", DICT_PATH + ":")
    print(*palingrams, sep="\n")

################################################################################
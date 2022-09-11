__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple
from collections import Counter
from sys import exit
from itertools import permutations

from utils.utils import load_words

################################################################################

class Anagrams(object):
    """
    Anagrams engine which accepts any phrase as an input. By selecting words
    from sub-anagrams set, an anagram phrase can be built.
    """

    DICT_PATH = "../utils/2of4brif.txt"

    def __init__(self, phrase: str):
        self._ORIGINAL_PHRASE = phrase
        self._words = load_words(self.DICT_PATH)
        self._cv_map = set(self.cv_map(word) for word in self._words)
        self._remaining = Counter(phrase.lower().replace(" ", ""))
        self._anagram_phrase = ""
        self._gallic_gambit = False

################################################################################

    @property
    def sub_anagrams(self) -> Tuple:
        """
        :return: alphabetically sorted set of all words that can be built from
        remaining letters
        """

        if self._gallic_gambit:
            perms = [''.join(i) for i in permutations(self.remaining_letters)]
        else:
            return tuple(sorted(
                word for word in self._words
                if word != self._ORIGINAL_PHRASE
                and all(key in self._remaining.keys()
                        and self._remaining[key] >= Counter(word)[key]
                        for key in Counter(word).keys())))

################################################################################

    @property
    def remaining_letters(self) -> str:
        """
        :return: remaining letters to build anagram phrase from
        """

        return "".join(letter * self._remaining[letter]
                       for letter in self._remaining.keys())

################################################################################

    @property
    def anagram_phrase(self) -> str:
        """
        :return: current state of the anagram phrase
        """

        return self._anagram_phrase

################################################################################

    def set_gallic_gambit(self) -> None:
        """

        :return:
        """

        self._gallic_gambit = True

################################################################################

    def build_anagram_phrase(self, word: str) -> None:
        """
        Attaches the param word to the anagram phrase. Removes its letters
        from the set of remaining letters to build the anagram phrase from.

        :param word: one of the words that can be built from the remaining
        letters
        """

        word = word.lower()

        if self._gallic_gambit:
            pass
        else:
            if word in self.sub_anagrams:
                self._anagram_phrase += word
                self._anagram_phrase += " "

                word = Counter(word)
                for letter in word.keys():
                    self._remaining[letter] -= word[letter]

################################################################################

    def cv_map(self, word: str) -> str:
        """

        :param word:
        :return:
        """

        return "".join("v" if letter in "aeiouy" else "c" for letter in word)

################################################################################

if __name__ == '__main__':
    print("Welcome to the Anagrams practice.")
    user_input = input("\n\nEnter the word/phrase to find its anagrams: \n ")
    anagrams = Anagrams(user_input)

    while len(anagrams.remaining_letters) > 0:
        remaining_anagrams = anagrams.sub_anagrams
        print("Remaining letters: {}".format(anagrams.remaining_letters))
        print("Current anagram phrase: {}".format(anagrams.anagram_phrase))
        print("Remaining anagrams: {}".format(len(remaining_anagrams)))
        if len(remaining_anagrams) > 0:
            input("\nPress Enter to view remaining anagrams.")
            print("\n".join(remaining_anagrams))

        user_choice = input("\nMake a choice else Enter to start over or # to end: ")
        if len(user_choice) == 0:
            # start over
            anagrams = Anagrams(user_input)
        elif user_choice == "#":
            # user exit
            input("\nPress Enter to exit.")
            exit()
        else:
            if user_choice.lower() not in remaining_anagrams:
                print("Won't work! Make another choice!")
                input("\nPress Enter to continue.")
            else:
                anagrams.build_anagram_phrase(user_choice)

    print("\n*****FINISHED!!!*****\n")
    print("The anagram: {}".format(anagrams.anagram_phrase))
    input("\nPress Enter to exit.")

################################################################################
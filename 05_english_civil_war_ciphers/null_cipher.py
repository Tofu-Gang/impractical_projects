__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from string import punctuation
from random import randint
import sys
from typing import Tuple

sys.path.append('..')
from utils.utils import load_words

################################################################################

def encode_null_cipher(message: str, offset: int) -> Tuple[str, ...]:
    """
    Builds a list of words where every nth letter is part of a secret message.
    The "n" is the param offset. It is an easy way to create a null cipher
    without the result looking too suspicious.

    :param message: the secret message to be encoded with a null cipher
    :param offset: which letter in every word is part of the secret message
    :return: list of words where the secret message is hidden by a null cipher
    """

    WORD_SIZE_MIN = offset + 2
    WORD_SIZE_MAX = offset + 5

    prepared = message.replace(" ", "").lower()
    words = load_words("../utils/2of4brif.txt")
    cipher_list = []

    for char in prepared:
        word_size = randint(WORD_SIZE_MIN, WORD_SIZE_MAX)
        possible_words = filter(lambda word:
                                len(word) == word_size
                                and word.lower()[offset] == char,
                                words)
        cipher_list.append(next(possible_words))
    return tuple(cipher_list)

################################################################################

def decode_null_cipher(plaintext: str, offset: int) -> str:
    """
    Finds a hidden message in the plaintext using null cipher. The message
    consists of every nth letter after a punctuation mark. The "n" is the param
    offset. If there is another punctuation mark in the range, the count is
    restarted. As the result, punctuation marks themselves cannot be part of the
    hidden message.

    :param plaintext: original text
    :param offset: which letter after a punctuation mark is part of the message
    :return: the message hidden by a null cipher
    """

    return "".join([
        plaintext[i + offset]
        for i in range(len(plaintext))
        if plaintext[i] in punctuation
           and all([char not in punctuation
                    for char in plaintext[i + 1:i + offset + 1]])
           and i + offset < len(plaintext)])

################################################################################

def trevanion() -> None:
    """
    An example of null cipher; how Sir John Trevanion escaped a sure death.
    """

    OFFSET_LIMIT = 5
    with open("src/trevanion.txt", "r") as f:
        message = f.read()
        print("ORIGINAL MESSAGE =\n{}".format(message))
        print("List of punctuation marks to check = {}".format(punctuation))
        print("Number of letters to check after punctuation mark: {}"
              .format(OFFSET_LIMIT))
        plaintext = message.strip().replace(" ", "").replace("\n", "")
        for offset in range(1, OFFSET_LIMIT + 1):
            print("Using offset of {} after punctuation = {}"
                  .format(offset, decode_null_cipher(plaintext, offset)))

################################################################################

def build_vocab_list() -> None:
    """
    Embeds a null cipher within a list of dictionary words under the deception
    of vocabulary training.
    """

    vocab_list = encode_null_cipher("Panel at east end of chapel slides", 3)
    print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")

################################################################################

def saving_mary() -> None:
    """
    Embeds the message “Give your word and we rise” in a list of surnames using
    null cipher. The message is hidden in alternating second and third letter
    in the names.
    Some unused names are then inserted to indexes 0 (FIRST), 3 (STUART) and 6
    (JACOB) to help hide the presence of the cipher.
    """

    with open("src/supporters.txt", "r") as f:
        print("""
        Your Royal Highness: \n
        It is with the greatest pleasure I present the list of noble families who
        have undertaken to support your cause and petition the usurper for the
        release of your Majesty from the current tragical circumstances.
        """)
        message = "Give your word and we rise".lower().replace(" ", "")
        names = set(name.strip().lower() for name in f.readlines())
        cipher = list([
            next(filter(lambda name: name[(i % 2) + 1] == message[i], names))
            for i in range(len(message))])
        cipher.insert(0, "FIRST")
        cipher.insert(3, "STUART")
        cipher.insert(6, "JACOB")
        print(*cipher, sep='\n')

################################################################################

def colchester_catch(n: int) -> None:
    """
    Checks for and displays a null cipher based on the nth letter after the
    start of every nth word.

    :param n: nth letter of every nth word
    """

    with open("src/colchester_message.txt", "r") as f:
        plaintext = f.read()
        print("\nORIGINAL MESSAGE = {}\n".format(plaintext))
        plaintext_list = plaintext.strip().split()
        print("\nUsing increment of {}".format(n))
        try:
            message = ""
            for i in range(len(plaintext_list)):
                if (i + 1) % n == 0:
                    message += plaintext_list[i][n - 1]
            print("Secret message: {}".format(message))
        except IndexError:
            print("Interval doesn't work", file=sys.stderr)

################################################################################

if __name__ == '__main__':
    trevanion()
    print("###################################################################")
    build_vocab_list()
    print("###################################################################")
    saving_mary()
    print("###################################################################")
    colchester_catch(3)

################################################################################

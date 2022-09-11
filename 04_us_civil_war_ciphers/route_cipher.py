__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple, Iterator, Union, Dict
from itertools import permutations

################################################################################

def possible_keys(columns: int) -> Iterator[Tuple[int]]:
    """
    :param columns: desired key length
    :return: all possible column number combinations, including both directions
    (positive index UP -> DOWN, negative index DOWN -> UP)
    """

    # make permutations from all possible numbers of columns, including the
    # negative indexes; keep only the permutations which do not contain any
    # column in both positive and negative
    return filter(lambda permutation:
                  len(set([abs(column)
                           for column in permutation])) == len(permutation),
                  permutations(tuple(range(1, columns + 1)) +
                               tuple(range(-columns, 0)), 3))

################################################################################

def make_ciphertext(plaintext: str,
                    key: Tuple[int, ...],
                    code_words: Dict[str, str]) -> str:
    """
    Applies the route cipher to the plaintext.

    :param plaintext: original text
    :param key: transposition route (number of column+1, UP if < 0, DOWN if > 0)
    :param code_words: code words to be changed in the resulting cipher
    :return: cipher text
    """

    prepared = plaintext.upper()
    for word in code_words:
        prepared = prepared.replace(word.upper(), code_words[word].upper())
    plaintext_list = prepared.split(" ")

    columns = len(key)
    rows = len(plaintext_list) // columns
    transposition_matrix = [plaintext_list[i * columns: i * columns + columns]
                            for i in range(rows)]

    return " ".join([" ".join([row[column * -1 - 1]
                               for row in reversed(transposition_matrix)])
                     if column < 0
                     else
                     " ".join([row[column - 1]
                               for row in transposition_matrix])
                     for column in key])

################################################################################

def decipher(ciphertext: str,
             key: Tuple[int, ...],
             code_words: Dict[str, str]) -> str:
    """
    Decodes the text with applied route cipher.

    :param ciphertext: cipher text
    :param key: translation route (number of row+1, LEFT TO RIGHT if < 0,
                RIGHT TO LEFT if > 0
    :param code_words: code words to be changed in the resulting text
    :return: plain text
    """

    prepared = ciphertext.lower()
    for word in code_words:
        prepared = prepared.replace(word.lower(), code_words[word].lower())
    ciphertext_list = prepared.split(" ")

    rows = len(key)
    columns = len(ciphertext_list) // rows
    translation_matrix = [ciphertext_list[i * columns: i * columns + columns]
                          for i in range(rows)]

    key_applied = [[]] * len(key)
    for i in range(len(key)):
        row = key[i]
        if row > 0:
            key_applied[row - 1] = list(reversed(translation_matrix[i]))
        else:
            key_applied[row * -1 - 1] = translation_matrix[i]

    return " ".join([key_applied[row][column]
                     for column in reversed(range(columns))
                     for row in range(rows)])

################################################################################

def test_route_cipher(plaintext: str,
                      ciphertext: Union[str, None],
                      key: Tuple[int, ...],
                      code_words: Union[Dict[str, str], None]) -> None:
    """
    Tests encryption/decryption by the route cipher. If ciphertext is provided,
    it is compared to the result of the encryption process. Then, the encrypted
    message is decoded back and then this is compared to the provided original
    text.

    :param plaintext: original text
    :param ciphertext: cipher text; if provided, it is compared to the result
                       of encrypting the original text
    :param key: transposition route (number of column+1, UP if < 0, DOWN if > 0)
    :param code_words: code words to be changed in the resulting cipher and then
                       back in the original text
    """

    print("-------------------------------------------------------------------")
    print("The string to be encrypted: {}".format(plaintext))
    encrypted_result = make_ciphertext(plaintext, key, code_words)
    print("Encrypted string: {}".format(encrypted_result))
    if ciphertext is not None:
        if encrypted_result == ciphertext:
            print("Encryption result corresponds "
                  "with the given encrypted message.")
        else:
            print("ENCRYPTION ERROR!")
    decrypted_result = decipher(encrypted_result,
                                key,
                                {
                                    value: key
                                    for key, value in code_words.items()
                                })
    print("Decrypting back the original message: {}".format(decrypted_result))
    if decrypted_result == plaintext.lower():
        print("Decryption result corresponds with the given original message.")
    else:
        print("DECRYPTION ERROR!")
    print("-------------------------------------------------------------------")

################################################################################

if __name__ == '__main__':
    test_route_cipher(
        plaintext="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19",
        ciphertext="16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19",
        key=(-1, 2, -3, 4),
        code_words={})
    test_route_cipher(
        plaintext="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19",
        ciphertext=None,
        key=(-3, -1, 4, 2),
        code_words={})
    test_route_cipher(plaintext="Enemy cavalry heading to Tennessee "
                                "With Rebels gone you are free to transport "
                                "your supplies south REST IS JUST FILLER",
                      ciphertext="REST TRANSPORT YOU GODWIN VILLAGE ROANOKE "
                                 "WITH ARE YOUR IS JUST SUPPLIES FREE SNOW "
                                 "HEADING TO GONE TO SOUTH FILLER",
                      key=(-1, 2, -3, 4),
                      code_words={
                          "ENEMY": "VILLAGE",
                          "CAVALRY": "ROANOKE",
                          "TENNESSEE": "GODWIN",
                          "REBELS": "SNOW"
                      })
    test_route_cipher(plaintext="We will run the batteries at Vicksburg "
                                "the night of April 16 "
                                "and proceed to Grand Gulf "
                                "where we will reduce the forts "
                                "Be prepared to cross the river "
                                "on April 25 or 29 "
                                "Admiral Porter "
                                "THE REST IS JUST A FILLER",
                      ciphertext=None,
                      key=(-1, 3, -2, 6, 5, -4),
                      code_words={
                          "Batteries": "HOUNDS",
                          "Vicksburg": "ODOR",
                          "April": "CLAYTON",
                          "16": "SWEET",
                          "Grand": "TREE",
                          "Gulf": "OWL",
                          "Forts": "BAILEY",
                          "River": "HICKORY",
                          "25": "MULTIPLY",
                          "29": "ADD",
                          "Admiral": "HERMES",
                          "Porter": "LANGFORD"
                      })

################################################################################

__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

################################################################################

KEY_FREQUENCY = "FREQUENCY"
KEY_PROPORTION = "PROPORTION"
LETTERS_FREQUENCIES = {
    "E": {
        KEY_FREQUENCY: 11.1607,
        KEY_PROPORTION: 56.88
    }, "A": {
        KEY_FREQUENCY: 8.4966,
        KEY_PROPORTION: 43.31
    }, "R": {
        KEY_FREQUENCY: 7.5809,
        KEY_PROPORTION: 38.64
    }, "I": {
        KEY_FREQUENCY: 7.5448,
        KEY_PROPORTION: 38.45
    }, "O": {
        KEY_FREQUENCY: 7.1635,
        KEY_PROPORTION: 36.51
    }, "T": {
        KEY_FREQUENCY: 6.9509,
        KEY_PROPORTION: 35.43
    }, "N": {
        KEY_FREQUENCY: 6.6544,
        KEY_PROPORTION: 33.92
    }, "S": {
        KEY_FREQUENCY: 5.7351,
        KEY_PROPORTION: 29.23
    }, "L": {
        KEY_FREQUENCY: 5.4893,
        KEY_PROPORTION: 27.98
    }, "C": {
        KEY_FREQUENCY: 4.5388,
        KEY_PROPORTION: 23.13
    }, "U": {
        KEY_FREQUENCY: 3.6308,
        KEY_PROPORTION: 18.51
    }, "D": {
        KEY_FREQUENCY: 3.3844,
        KEY_PROPORTION: 17.25
    }, "P": {
        KEY_FREQUENCY: 3.1671,
        KEY_PROPORTION: 16.14
    }, "M": {
        KEY_FREQUENCY: 3.0129,
        KEY_PROPORTION: 15.36
    }, "H": {
        KEY_FREQUENCY: 3.0034,
        KEY_PROPORTION: 15.31
    }, "G": {
        KEY_FREQUENCY: 2.4705,
        KEY_PROPORTION: 12.59
    }, "B": {
        KEY_FREQUENCY: 2.0720,
        KEY_PROPORTION: 10.56
    }, "F": {
        KEY_FREQUENCY: 1.8121,
        KEY_PROPORTION: 9.24
    }, "Y": {
        KEY_FREQUENCY: 1.7779,
        KEY_PROPORTION: 9.06
    }, "W": {
        KEY_FREQUENCY: 1.2899,
        KEY_PROPORTION: 6.57
    }, "K": {
        KEY_FREQUENCY: 1.1016,
        KEY_PROPORTION: 5.61
    }, "V": {
        KEY_FREQUENCY: 1.0074,
        KEY_PROPORTION: 5.13
    }, "X": {
        KEY_FREQUENCY: 0.2902,
        KEY_PROPORTION: 1.48
    }, "Z": {
        KEY_FREQUENCY: 0.2722,
        KEY_PROPORTION: 1.39
    }, "J": {
        KEY_FREQUENCY: 0.1965,
        KEY_PROPORTION: 1.00
    }, "Q": {
        KEY_FREQUENCY: 0.1962,
        KEY_PROPORTION: 1
    }
}

################################################################################

def process_cipher(filename: str) -> None:
    """
    ETAOIN

    :param filename:
    """

    ETAOIN = "ETAOIN"

    with open(filename, "r") as f:
        contents = "".join([line.strip().upper() for line in f.readlines()])
        contents_len = len(contents)
        letters_frequencies = dict([
            (letter.upper(), (contents.count(letter.upper()) / contents_len) * 100)
            for letter in ETAOIN])
        print("letter: general; cipher")
        print("\n".join(["{}: {}; {}".format(letter, LETTERS_FREQUENCIES[letter][KEY_FREQUENCY], letters_frequencies[letter])
                         for letter in ETAOIN]))

################################################################################

if __name__ == '__main__':
    print("cipher_a.txt: most likely a letter transposition cipher")
    process_cipher("cipher_a.txt")
    print("cipher_b.txt: most likely a letter substitution cipher")
    process_cipher("cipher_b.txt")

################################################################################


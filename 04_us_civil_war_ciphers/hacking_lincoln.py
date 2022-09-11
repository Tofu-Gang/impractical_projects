__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from route_cipher import decipher

################################################################################

if __name__ == '__main__':
    CODE_WORDS = {
        "WAYLAND": "captured",
        "NEPTUNE": "Richmond"
    }
    ciphertext = "THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"

    for key in CODE_WORDS:
        ciphertext = ciphertext.replace(key, CODE_WORDS[key])
    ciphertext = ciphertext.lower()
    ciphertext_list = ciphertext.split(" ")

    for columns in [i for i in range(1, len(ciphertext_list)) if i % 2 == 0]:
        key_1 = tuple([i if i % 2 == 0 else -i for i in range(1, columns + 1)])
        key_2 = tuple([-i if i % 2 == 0 else i for i in range(1, columns + 1)])
        key_3 = tuple([i if i % 2 == 0 else -i for i in reversed(range(1, columns + 1))])
        key_4 = tuple([-i if i % 2 == 0 else i for i in reversed(range(1, columns + 1))])
        print("key = {}; {}".format(key_1, decipher(ciphertext, key_1)))
        print("key = {}; {}".format(key_2, decipher(ciphertext, key_2)))
        print("key = {}; {}".format(key_3, decipher(ciphertext, key_3)))
        print("key = {}; {}".format(key_4, decipher(ciphertext, key_4)))

    # correspondents of the tribune captured at richmond please ascertain why
    # they are detained and get them off if you can this fills it up
    print("SOLUTION: key = (-1, 2, -3, 4)")
    print(decipher(ciphertext, (-1, 2, -3, 4)))

################################################################################

__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Union

################################################################################

def make_ciphertext(plaintext: str,
                    word_length: int,
                    rails: int = 2) -> Union[str, None]:
    """
    Applies the rail fence cipher to the plaintext.

    :param plaintext: original text
    :param word_length: length of words the final cipher will be split to
    :return: cipher text
    """

    # remove whitespace and capitalize everything
    prepared = plaintext.replace(" ", "").upper()
    if rails > 1:
        # stack and stagger letters in a zigzag pattern
        rail_fence = "".join(["".join([
            prepared[i]
            for i in range(len(prepared))
            if i % rails == mod])
            for mod in range(rails)])
        # split the result into words of desired length
        words_count = len(rail_fence) // word_length
        ciphertext = " ".join(
            [rail_fence[i * word_length: (i + 1) * word_length]
             for i in range(words_count)])
        # if there is not enough characters to form the last word, don't forget
        # to append the rest as a shorter word
        ciphertext += " " + rail_fence[words_count * word_length:]
        return ciphertext.strip()
    else:
        return None

################################################################################

def decipher(ciphertext: str, rails: int = 2) -> Union[str, None]:
    """
    Decodes the text with applied rail fence cipher.

    :param ciphertext: cipher text
    :return: plain text
    """

    # remove whitespace and make everything lowercase for better readability
    rail_fence = ciphertext.replace(" ", "").lower()

    if rails > 1:
        # get slice indexes to make rails
        denominators = []
        denominators.append((len(rail_fence) // rails))
        if len(rail_fence) % rails > 0:
            denominators[0] += 1
        # if the message cannot be split into rails evenly, some of the first
        # rails get to be one character longer
        longer_rails_count = (len(rail_fence) % rails) - 1
        for i in range(1, rails - 1):
            denominator = denominators[i - 1] + len(rail_fence) // rails
            if longer_rails_count > 0:
                denominator += 1
                longer_rails_count -= 1
            denominators.append(denominator)

        # make the rails
        rails_list = []
        rails_list.append(rail_fence[:denominators[0]])
        rails_list += list([rail_fence[denominators[i - 1]:denominators[i]]
                            for i in range(1, len(denominators))])
        rails_list.append(rail_fence[denominators[-1]:])
        # to avoid IndexError, insert a space to the shorter rails, making
        # it the same length as the longer ones
        rails_list = list(map(lambda rail: rail + " "
                              if len(rail) != len(rails_list[0])
                              else rail, rails_list))
        return "".join(["".join(rail[i] for rail in rails_list) for i in
                        range(denominators[0])]).replace(" ", "")
    else:
        return None

################################################################################

def test_rail_fence_cipher(plaintext: str,
                           ciphertext: Union[str, None],
                           word_length: int,
                           rails: int = 2) -> None:
    """
    Tests encryption/decryption by the rail fence cipher. If ciphertext is
    provided, it is compared to the result of the encryption process. Then, the
    encrypted message is decoded back and then this is compared to the provided
    original text.

    :param plaintext: original text
    :param ciphertext: cipher text; if provided, it is compared to the result
                       of encrypting the original text
    :param word_length: length of words the final cipher will be split to
    """

    print("-------------------------------------------------------------------")
    print("The string to be encrypted: {}".format(plaintext))
    encrypted_result = make_ciphertext(plaintext, word_length, rails)
    print("Encrypted string: {}".format(encrypted_result))
    if ciphertext is not None:
        if encrypted_result == ciphertext:
            print("Encryption result corresponds "
                  "with the given encrypted message.")
        else:
            print("ENCRYPTION ERROR!")
    decrypted_result = decipher(encrypted_result, rails)
    print("Decrypting back the original message: {}".format(decrypted_result))
    if decrypted_result == plaintext.replace(" ", "").lower():
        print("Decryption result corresponds with the given original message.")
    else:
        print("DECRYPTION ERROR!")
    print("-------------------------------------------------------------------")

################################################################################

if __name__ == '__main__':
    test_rail_fence_cipher(plaintext="Buy more Maine potatoes",
                           ciphertext="BYOEA NPTTE UMRMI EOAOS",
                           word_length=5)
    test_rail_fence_cipher(plaintext="Let us cross over the river "
                                     "and rest under the shades of the trees",
                           ciphertext="LTSRS OETEI EADET NETEH DSFHT ESEUC "
                                      "OSVRH RVRNR SUDRH SAEOT ERE",
                           word_length=5)
    test_rail_fence_cipher(plaintext="123123123",
                           ciphertext=None,
                           word_length=3,
                           rails=3)

################################################################################

__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

################################################################################

if __name__ == '__main__':
    print("Welcome to the Pig Latin practice.' \n")
    print("The input can be any english word. \n")
    print("If it begins with a consonant, move that consonant to the end, and then add \"ay\" to the end of the word. \n")
    print("If the word begins with a vowel, you simply add \"way\" to the end of the word. ")

    while True:
        word = input("\n\nEnter the word to convert to the Pig Latin: \n ")

        if word[0].lower() in ("a", "e", "i", "o", "u", "y"):
            pig_latin_word = word + "way"
        else:
            pig_latin_word = word[1:] + word[0] + "ay"

        print(word + " in Pig Latin is: " + pig_latin_word)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

################################################################################
__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from random import choice
from json import load

################################################################################

if __name__ == '__main__':
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    with open("first.json", "r") as f:
        first = load(f)
    with open("last.json", "r") as f:
        last = load(f)

    while True:
        firstName = choice(first)
        lastName = choice(last)

        print("\n\n")
        print(firstName, lastName)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

################################################################################
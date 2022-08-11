__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from pprint import pprint
from string import punctuation

################################################################################

if __name__ == '__main__':
    print("Welcome to the Poor Man's Bar Chart practice.' \n")
    print("The input can be any english sentence. \n")
    print("The output is bar chart-like diagram of all used letters.")

    while True:
        sentence = input("\n\nEnter the sentence to see the bar chart: \n ")
        letters = sentence.translate(str.maketrans('', '', punctuation)).replace(" ", "").lower()
        bar_chart = {}
        for letter in letters:
            bar_chart.setdefault(letter, [])
            bar_chart[letter].append(letter)

        bar_chart = dict((key, ''.join(value)) for key, value in bar_chart.items())
        pprint(bar_chart)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

################################################################################
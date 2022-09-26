"""
Use genetic algorithm to simulate breeding race of super rats.
"""

from time import time
from random import triangular, shuffle, randint, random, uniform, choice
import statistics
from typing import List


################################################################################

class Simulation(object):
    # CONSTANTS (weights in grams)
    GOAL_WEIGHT = 50000
    RATS_MAX_COUNT = 20  # number of adult breeding rats in each generation
    # sum of males and females to breed has to be equal to number of adult
    # breeding rats
    TO_BREED_MALES = 4
    TO_BREED_FEMALES = 16
    INITIAL_MIN_WEIGHT = 200
    INITIAL_MAX_WEIGHT = 600
    INITIAL_COMMON_WEIGHT = 300
    MUTATE_ODDS = 0.01
    MUTATE_WEIGHT_MIN = 0.5
    MUTATE_WEIGHT_MAX = 1.2
    LITTER_SIZE = 8
    LITTERS_PER_YEAR = 10
    GENERATION_LIMIT = 500

    # ensure even-number of rats for breeding pairs:
    if RATS_MAX_COUNT % 2 != 0:
        RATS_MAX_COUNT += 1

################################################################################

    def __init__(self):
        """
        Initialize a population with a triangular distribution of weights.
        """

        self._population = [
            int(triangular(self.INITIAL_MIN_WEIGHT,
                           self.INITIAL_MAX_WEIGHT,
                           self.INITIAL_COMMON_WEIGHT))
            for _ in range(self.RATS_MAX_COUNT)]
        self._children = None
        self._generations = 0

################################################################################

    @property
    def _fitness(self) -> float:
        """
        :return: population fitness based on an attribute mean vs target
        """

        return statistics.mean(self._population) / self.GOAL_WEIGHT

################################################################################

    @property
    def _members_per_sex(self) -> int:
        """
        :return: total members of the current population, by sex;
        always 50% males and 50% females
        """

        return len(self._population) // 2

################################################################################

    @property
    def _male_parents(self) -> List[int]:
        """
        :return: largest males from the population that get to breed, in a
        random order
        """

        males = sorted(self._population)[self._members_per_sex:]
        selected_males = males[-self.TO_BREED_MALES:]
        shuffle(selected_males)
        return selected_males

################################################################################

    @property
    def _female_parents(self) -> List[int]:
        """
        :return: largest females from the population that get to breed, in a
        random order
        """

        females = sorted(self._population)[:self._members_per_sex]
        selected_females = females[-self.TO_BREED_FEMALES:]
        shuffle(selected_females)
        return selected_females

################################################################################

    def _breed(self) -> None:
        """
        Crossover genes among members of a population.
        """

        self._children = [
            randint(female, male)
            for male, female in [tuple([choice(self._male_parents), female])
                                 for female in self._female_parents]
            for _ in range(self.LITTER_SIZE)]

################################################################################

    def _mutate(self) -> None:
        """
        Randomly alter rat weights using input odds & fractional changes.
        """

        self._children = [
            round(rat * uniform(self.MUTATE_WEIGHT_MIN, self.MUTATE_WEIGHT_MAX))
            if self.MUTATE_ODDS >= random()
            else
            rat
            for rat in self._children]

################################################################################

    def evolve(self) -> None:
        """
        Initialize population, select, breed, and mutate, display results.
        """

        print("initial population weights = {}".format(self._population))
        print("initial population fitness = {}".format(self._fitness))
        print("number to retain = {}".format(self.RATS_MAX_COUNT))

        average_weights = []

        while self._fitness < 1 and self._generations < self.GENERATION_LIMIT:
            self._breed()
            self._mutate()
            self._population = self._male_parents + self._female_parents + self._children
            print("Generation {} fitness = {:.4f}".format(self._generations, self._fitness))
            average_weights.append(int(statistics.mean(self._population)))
            self._generations += 1

        print("average weight per generation = {}".format(average_weights))
        print("\nnumber of generations = {}".format(self._generations))
        print("number of years = {}".format(int(self._generations / self.LITTERS_PER_YEAR)))

################################################################################


if __name__ == '__main__':
    start_time = time()
    simulation = Simulation()
    simulation.evolve()
    end_time = time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))

################################################################################

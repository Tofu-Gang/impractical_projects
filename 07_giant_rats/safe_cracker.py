from time import time
from random import randrange, choice
from typing import List


################################################################################

class SafeCracker(object):
    COMBO_LENGTH = 10

################################################################################

    def __init__(self):
        """
        Chooses safe combination at random; creates the first guess attempt.
        """

        self._combo = self._random_combo()
        self._attempt = self._random_combo()
        self._attempts_count = 1
        print("Combination = {}".format("".join([str(n) for n in self._combo])))

################################################################################

    def _random_combo(self) -> List[int]:
        """
        :return: random combination of COMBO_LENGTH numbers
        """

        return list([randrange(10) for _ in range(self.COMBO_LENGTH)])

################################################################################

    @property
    def _fitness(self) -> int:
        """
        :return: number of matches in the combination and guess attempt
        """

        return sum(map(lambda i: self._attempt[i] == self._combo[i],
                       range(self.COMBO_LENGTH)))

################################################################################

    def guess_combo(self) -> None:
        """
        Gradually change the guess attempt one numeral at a time; keep the new
        guess when its fitness is greater than that of the previous attempt.
        """

        change_positions = list(range(self.COMBO_LENGTH))

        while self._attempt != self._combo:
            old_fitness = self._fitness
            change_pos = choice(change_positions)
            old_value = self._attempt[change_pos]
            new_value = choice([i for i in range(10)
                                if i != self._attempt[change_pos]])
            self._attempt[change_pos] = new_value

            if self._fitness > old_fitness:
                # exclude this position from the future guesses
                change_positions.remove(change_pos)
            else:
                self._attempt[change_pos] = old_value
            self._attempts_count += 1

        print("Cracked! {}".format("".join(str(n) for n in self._attempt)))
        print("in {} tries!".format(self._attempts_count))


################################################################################

if __name__ == '__main__':
    start_time = time()
    safe_cracker = SafeCracker()
    safe_cracker.guess_combo()
    end_time = time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))

################################################################################

#!/usr/bin/env python
import sys
import random
import itertools
import ast


def nbackseq(n, length, words):
    """Generate n-back balanced sequences

    :param n: int
        How many characters (including the current one) to look back
        to assure no duplicates
    :param length: int
        The total length of the sequence to produce
    :param words: list
        A list of words to be used to generate sequences
        NOTE: must input words parameter as a literal e.g., '[1, 2]' with the quotes!!
    :return: list
         A list of solutions where each solution is a list of words of length 'length'
    """
    solutions = []
    solution_attempts = []

    while len(solution_attempts) < len(list(itertools.permutations(words, length))):

        solution = random.sample(words, length)

        if solution not in solution_attempts:
            good = True
            for index in range(len(solution)):
                subseq = solution[index: index + n]
                if len(set(subseq)) != n:
                    good = False
                    break

                if good:
                    solutions.append(solution)

            solution_attempts.append(solution)

    return solutions


def test_nbackseq():
    assert nbackseq(2, 1, [1, 2]) == []
    assert nbackseq(1, 1, ['a']) == [['a']]
    assert nbackseq(2, 2, [1, 2]) == [[1, 2], [2, 1]]


if __name__ == '__main__':
    n = int(sys.argv[1])
    length = int(sys.argv[2])
    words = ast.literal_eval(sys.argv[3])
    solutions = nbackseq(n, length, words)
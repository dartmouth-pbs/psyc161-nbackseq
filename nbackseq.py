#!/usr/bin/env python
import random
import sys


def nbackseq(n, length, words):
    """Generate n-back balanced sequences

    Parameters
    ----------
    n : int
        How many characters (including the current one) to look
        back to assure no duplicates
    length : int
        The total length of the sequence to produce
    words : list
        A list of words to be used to generate sequences

    Returns
    -------
    list
        A list of solutions, where each solution is a list of words
        of length `length`

    """
    solutions = []

    solution = random.sample(words, length)
    # validate that the sequence is correct n-back sequence
    good = True
    for index in range(len(solution)):
        subseq = solution[index-(n-1): index]
        if len(set(subseq)) != n:
            good = False
            break
    if good:
        solutions.append(solution)

    return solutions


def test_nbackseq():
    assert nbackseq(2, 1, [1, 2]) == []
    assert nbackseq(1, 1, ['a']) == [['a']]
    assert nbackseq(2, 2, [1, 2]) == [[1, 2], [2, 1]]
    assert nbackseq(1, 2, [1, 2]) == [[1, 1], [1, 2], [2, 1], [2, 2]]


if __name__ == '__main__':
    n = int(sys.argv[1])
    length = int(sys.argv[2])
    words = sys.argv[3:]
    print(nbackseq(n, length, words))

#!/usr/bin/env python

import random
import sys


def make_nbackseq(l, words):
    seq = []
    # first make sure each word occurs at least once
    for w in words:
        seq.append(w)
    # now if length is less than l, append random words
    while len(seq) < l:
        word = random.sample(words,1)
        seq.append(word[0])
    #for i in range(l):
    #    word = random.sample(words,1)
    #    seq.append(word[0])
    return seq

def check_nbackseq_unique(n, sequence):
    """
    Function to check if there are repetitions in
    the given sequence

    Parameters
    ----------
    n : number of elements to go back by
    sequence : sequence to check for repetitions in
    """
    check_window = n
    repetitions = []
    for i in range(len(sequence)):
        check_until = i+1
        check_from = i - n
        if len(sequence[:check_until]) > check_window:
            window = sequence[check_from:check_until]
        else:
            window = sequence[:check_until]
        if len(set(window)) == len(window):
            repetitions.append(True)
        else:
            repetitions.append(False)

    # don't need the index for now
    # return False in repetitions, repetitions.index(False)

    return False in repetitions

def nbackseq(n, l, words):
    if len(words) == n:
        raise ValueError("Number of items needs to be greater than n-back!")
    else:
        seq = make_nbackseq(l, words)
        counter = 0
        while check_nbackseq_unique(n, seq):
            counter += 1
            seq = make_nbackseq(l, words)
            print "Checked {0} sequences so far".format(counter)
        return seq

if __name__ == '__main__':
    n = int(sys.argv[1])
    l = int(sys.argv[2])
    #words = sys.argv[3]
    words = sys.argv[3:]

    if len(words) == n:
        raise ValueError("Number of items needs to be greater than n-back!")
    else:
        s = nbackseq(n, l, words)
        print s

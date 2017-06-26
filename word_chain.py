
from functools import wraps
import sys
import itertools


def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def find_biggest_chain_with_prefix(prefix, words):
    biggest_chain_size = 0
    for word in words:
        if word[0] == prefix:
            smaller_problem_prefix = word[-1]
            smaller_problem_words = words - {word}
            smaller_problem_answer = find_biggest_chain_with_prefix(smaller_problem_prefix, smaller_problem_words)
            biggest_chain_size = max(biggest_chain_size, 1 + smaller_problem_answer)
    return biggest_chain_size


def found_bigest_chain(words):
    biggest_chain_size = 0
    for word in words:
        smaller_problem_prefix = word[-1]
        smaller_problem_words = words - {word}
        smaller_problem_answer = find_biggest_chain_with_prefix(smaller_problem_prefix, smaller_problem_words)
        biggest_chain_size = max(biggest_chain_size, 1 + smaller_problem_answer)
    return biggest_chain_size


def main():

    f = open(sys.argv[-1],'r').readlines()

    for line in f:
        list_line = frozenset(line.strip().split(','))
        size = found_bigest_chain(list_line)
        if size == 1:
            print "None"
        else:
            print size
main()
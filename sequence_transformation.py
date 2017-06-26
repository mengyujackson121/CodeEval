from functools import wraps
import sys
import re
import time


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
def can_match(ones_and_zeros, as_and_bs):
    if len(ones_and_zeros) == 0 and len(as_and_bs) == 0:
        return True
    elif len(ones_and_zeros) ==0 or len(as_and_bs) ==0:
        return False
    if ones_and_zeros[0] == '0':
        if as_and_bs[0] == 'B':
            return False
        elif as_and_bs[0] == 'A':
            return try_all_partitions(as_and_bs, "A", ones_and_zeros)

    elif ones_and_zeros[0] == '1':
        first_letter = as_and_bs[0]
        return try_all_partitions(as_and_bs, first_letter, ones_and_zeros)


def try_all_partitions(as_and_bs, first_letter, ones_and_zeros):
    count = 0
    while count < len(as_and_bs) and as_and_bs[count] == first_letter:
        count += 1
    for i in range(0, count):
        if can_match(ones_and_zeros[1:],  # Take off the Zero we found on line 23
                     as_and_bs[i + 1:]):  # Take away all the As that it might match
            return True
    return False


def main():
    #start = time.time()
    lines = open(sys.argv[-1], 'r').readlines()
    num = 0
    for line in lines:
        first, second = line.strip().split(' ')
        num = num + 1
        if can_match(first, second):
            print "Yes"
        else:
            print "No"

    #end = time.time()
    #print end-start
main()
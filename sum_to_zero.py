import sys
from itertools import combinations


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        number = map(int,line.strip().split(','))
        size = []
        for comb in combinations(number, 4):
            size.append(sum(comb))
        print size.count(0)

main()

import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        first, second = line.lower().strip().split(';')
        first_scheme,first_rest = first.strip().split('://')
        second_scheme,second_rest = second.strip().split('://')
        first_part1,first_part2,first_part3, = first_rest.strip().split('/')
        second_part1, second_part2, second_part3 = second_rest.strip().split('/')
        if first_part2.is
        print first_part1
        print first_part2
        print first_part3
        print second_part1
        print second_part2
        print second_part3

main()
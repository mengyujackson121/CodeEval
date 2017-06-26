import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        each_lines = line.strip().split(' ')
        print ' '.join(each_lines[::-2])
main()
import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        print line
main()
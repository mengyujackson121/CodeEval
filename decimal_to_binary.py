import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()

    for line in lines:
        integers = int(line.strip())
        binary = bin(integers)
        print binary[2:]

main()
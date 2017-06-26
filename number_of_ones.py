import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        binary = bin(int(line.strip()))
        count = 0
        for each in binary[2:]:
            if int(each) == 1:
                count += 1
        print count

main()
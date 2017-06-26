import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        value = int(line.strip())
        size = 0
        while value > 0:
            if value >= 5:
                size += 1
                value = value - 5
            elif value >= 3:
                size += 1
                value = value - 3
            elif 0 < value < 3:
                size +=1
                value = value - 1

        print size
main()
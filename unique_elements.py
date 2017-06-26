import sys
def main():
    f = open(sys.argv[-1], 'r').readlines()
    for line in f:
        a = line.strip().split(',')

        print ','.join(sorted(set(a), key = int))


if __name__ == "__main__":
    main()

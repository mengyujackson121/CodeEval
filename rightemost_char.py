import sys
def main():
    f = open(sys.argv[-1], 'r').readlines()

    for line in f:
        a, b = line.strip().split(',')
        rightmost = -1
        for i in range(len(a)):
            if a[i] == b:
                rightmost = i
        print rightmost

if __name__ == "__main__":
    main()

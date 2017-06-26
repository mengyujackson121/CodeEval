import sys
def main():
    f = open(sys.argv[-1], 'r').readlines()
    for line in f:
        a = map(int,line.strip().split())
        number = []
        for num in a:
            if a.count(num) == 1:
                number.append(num)
        b = sorted(number)
        if len(b) == 0:
            print 0
        else:
            print a.index(b[0])+1

if __name__ == "__main__":
    main()

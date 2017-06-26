import sys

def main():
    f = open(sys.argv[-1], 'r').readlines()
    for line in f:
        a,b = map(int,line.strip().split())
        size = 0
        for number in range(1,b+1):
            num = bin(number).count('0')
            if num == a+1:
                size += 1
        print size

if __name__ == "__main__":
    main()

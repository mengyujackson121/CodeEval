import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        first, second = map(int,line.strip().split(','))
        prime_list = []
        for number in range(first, second + 1):
            prime = True
            for i in range(2, number):
                if number % i == 0:
                    prime = False
            if prime:
                prime_list.append(str(number))
        print len(prime_list)


main()
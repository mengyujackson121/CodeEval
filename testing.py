import sys


def main():
    f = open(sys.argv[-1], 'r').readlines()
    for line in f:
        a, b = line.strip().split(' | ')
        zipped = zip(a, b)
        number = num_errors(zipped)
        print_error_lv(number)


def print_error_lv(number):
    if number == 0:
        print 'Done'
    elif number <= 2:
        print 'Low'
    elif number <= 4:
        print 'Medium'
    elif number <= 6:
        print 'High'
    else:
        print 'Critical'


def num_errors(zipped):
    number = 0
    for t1, t2 in zipped:
        if t1 != t2:
            number += 1
    return number


if __name__ == "__main__":
    main()

import sys

f = open(sys.argv[-1], 'r').readlines()

for line in f:
    a = line.strip().split(';')
    b = []
    for num in a:
        number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        b.append(str(number[num]))
    print ''.join(b)

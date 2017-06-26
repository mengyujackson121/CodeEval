import sys

f = open(sys.argv[-1], 'r').readlines()

for line in f:
    sum1 = 0
    sum2 = 0
    count = 0
    for char in line:
        if char.isdigit():
            number = int(char)
            count += 1
            if count % 2 != 0:
                sum1 += number * 2
            else:
                sum2 += number
    if (sum1 + sum2) % 10 == 0:
        print "Real"
    else:
        print "Fake"

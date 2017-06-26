import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = int(line.strip())
    f_1 = 0
    f_2 = 1
    if a > 1:
        for number in range(1,a):
            fn = f_1 + f_2
            f_1 = f_2
            f_2 = fn
        print f_2
    else:
        print a

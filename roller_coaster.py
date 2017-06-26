import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip()
    alpha = 1
    for char in a:
        if char.isalpha():
            alpha = alpha + 1
        if alpha %  2 == 0:
            sys.stdout.write(char.upper())
        else:
            sys.stdout.write(char.lower())
    print


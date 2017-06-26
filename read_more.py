import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip()
    if len(a) < 56:
        print a

    else:
        b = a[:40].split(' ')
        if len(b) == 1:
            print  ''.join(b) + '... <Read More>'
        else:
            print ' '.join(b[:-1]) + '... <Read More>'

import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a,b = line.strip().split(';')
    c = set(a.strip().split(','))
    d = set(b.strip().split(','))
    print ','.join(sorted(c & d))


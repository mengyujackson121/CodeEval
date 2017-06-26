import sys
import math

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().split(" ")
    b = ''.join(a)
    c = int(math.sqrt(len(a)))
    d = [list(b[i:i + c]) for i in range(0, len(b), c)]
    e = zip(*d[::-1])
    print ' '.join([' '.join(row) for row in e])
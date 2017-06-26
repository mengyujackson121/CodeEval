import sys
from collections import Counter
f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().split(',')
    length = len(a)/2
    b = Counter(a).most_common(1)
    b0 = b[0]
    c,d = b0[0],b0[1]
    if d > length:
        print c
    else:
        print "None"
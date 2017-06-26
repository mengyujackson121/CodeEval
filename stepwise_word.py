import sys
from collections import Counter
f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().split(' ')
    length = len(a)
    b = max(a, key=len)
    c = []
    # star = ''
    # for each in b:
    #     c.append(star + each)
    #     star = star + '*'
    for i in range(len(b)):
        c.append("*" * i + b[i])
    print ' '.join(c)

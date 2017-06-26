import sys
import time

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a, b = line.strip().split()

    c = (sum(int(x) * 60 ** i for i, x in enumerate(reversed(a.split(":")))))
    d = (sum(int(x) * 60 ** i for i, x in enumerate(reversed(b.split(":")))))
    print time.strftime("%H:%M:%S", time.gmtime(abs(c-d)))


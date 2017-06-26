import sys
import math

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().split(') (')
    a[0] = a[0].replace('(','')
    a[1] = a[1].replace(')','')
    x1,y1 = a[0].split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2,y2 = a[1].split(',')
    x2 = int(x2)
    y2 = int(y2)
    d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print int(d)
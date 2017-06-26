import sys
import datetime
f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = float(line.strip())
    deg = int(a)
    min = (a - deg) *60
    sec = (min - int(min)) * 60
    print str(deg) + "." + '%.2d' % int(min) + '\'' + '%.2d'% int(sec) + "\""
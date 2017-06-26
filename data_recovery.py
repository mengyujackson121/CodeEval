import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a, b= line.strip().split(";")
    c = a.split(" ")
    d = [int(string) for string in b.split(" ")]
    e = sorted(d)[-1]*(sorted(d)[-1] + sorted(d)[0]) / 2 - sum(sorted(d))
    if e == 0:
        d.append(max(d)+1)
    else:
        d.append(e)
    g = sorted(zip(d,c))
    print ' '.join([item[1] for item in g])
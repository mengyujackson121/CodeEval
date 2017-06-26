import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().strip(len(f))
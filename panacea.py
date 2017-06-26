import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a,b = line.strip().split('|')
    c = a.strip().split(" ")
    hex_number = [int(x, 16) for x in c]
    sum_h =sum(hex_number)
    d = b.strip().split(" ")
    bin_number = [int(x, 2) for x in d]
    sum_b = sum(bin_number)
    if sum_h == sum_b:
        print "True"
    elif sum_h < sum_b:
        print "True"
    else:
        print "False"
import sys
import re


def split_plus_or_minus(integer_string):
    if "+" in integer_string:
        first, second = integer_string.split("+")
        print int(first) + int(second)
    else:
        first, second = integer_string.split("-")
        print int(first) - int(second)

f = open(sys.argv[-1],'r').readlines()
for line in f:
    a = re.split('([- +])',line.strip())
   # print a
    n = len(a[2])
    l = a[0]
    split_plus_or_minus(l[:n] + a[3] + l[n:])










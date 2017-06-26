import sys

file_name = sys.argv[-1]
f = open(file_name,'r')
s = f.readlines()

list = []

for line in s:
    t = line.strip()
    a = t.split(',')
    x, n = [int(integer) for integer in a]
    # x = list_number[0]
    # n = list_number[1]

    if x <= n:
        print n
    else:
        times = 1
        while x > n:
            n = list_number[1] * times
            times = times + 1
        print n

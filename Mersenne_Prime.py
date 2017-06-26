import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    MP_list = [3, 7, 31, 127, 2047]
    result = []
    a = int(line.strip())
    for number in MP_list:
        if (a >= number):
            result.append(str(number))
    print ', '.join(result)
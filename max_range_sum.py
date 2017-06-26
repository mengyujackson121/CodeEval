import sys

f = open(sys.argv[-1],'r').readlines()


def function_sum_lenth(length, value):
    result = []
    for start_point in range(len(value) - lenth + 1):
        result.append(sum(value[start_point: start_point + length]))
    return sorted(result)[-1]


for line in f:
    a,b = line.strip().split(';')
    lenth = int(a)
    value = map(int,b.strip().split(' '))
    answer = function_sum_lenth(lenth, value)
    if answer > 0:
        print answer
    else:
        print 0



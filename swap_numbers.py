import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().split(' ')
    result = []
    final = []
    for each in a:
        list_value = list(each)
        list_value[0], list_value[-1] = list_value[-1], list_value[0]
        result.append(''.join(list_value))
    print ' '.join(result)


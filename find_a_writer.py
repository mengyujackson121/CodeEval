import sys
f = open(sys.argv[-1],'r').readlines()


def get_value(string_, value):
    return string_[value - 1]

for line in f:
    string,a = line.strip().split('|')
    place_list = [int(s) for s in a.strip().split(' ')]
    result = []

    for each_value in place_list:
        result.append(get_value(string, each_value))
    print ''.join(result)

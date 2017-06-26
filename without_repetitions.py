import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip()
    value = ''
    result = []
    for char in a:
        if char != value:
            result.append(char)
            value = char
        final = ''.join(result)
    print final

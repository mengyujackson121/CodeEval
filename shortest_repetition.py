import sys

f = open(sys.argv[-1],'r').readlines()


for line in f:
    a = line.strip()
    result = []
    for char in a:
        maybe_match = ''
        result.append(char)
        match = ''.join(result)
        while len(maybe_match) < len(a):
            maybe_match += match
        if maybe_match == a:
            print len(result)
            break


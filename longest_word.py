import sys
file_name = open(sys.argv[-1],'r').readlines()


for line in file_name:
    a = line.strip()
    sortedwords = sorted(a.split(), reverse=True, key=len)

    print sortedwords[0]
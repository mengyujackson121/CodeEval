import sys
file_name = open(sys.argv[-1],'r').readlines()


for line in file_name:
    a = line.strip()
    b = a.split()
    c = [str(int(number,16)) for number in b]
    d = ' '.join(c)
    print d


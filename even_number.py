import sys

file_name = open(sys.argv[-1],'r').readlines()


for line in file_name:
    a = line.strip()
    list_number = int(a)
    if list_number % 2 == 0:
        print 1
    else:
        print 0


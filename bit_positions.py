import sys
file_name = open(sys.argv[-1],'r').readlines()

list_number = []
for line in file_name:
    a = line.strip()
    b = a.split(',')
    list_number = [int(number) for number in b]
    x, y = list_number[1],list_number[2]
    z = str(bin(list_number[0])[2:])
    if z[-x] == z[-y]:
        print 'true'
    else:
        print 'false'

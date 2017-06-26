import sys
file_name = open(sys.argv[-1],'r').readlines()

list_number = []
for line in file_name:
    a = line.strip()
    b = a.split(',')
    list_number = [int(number) for number in b]
    N, M = list_number
    if M == 0:
        print 'False'
    else:
        print N % M



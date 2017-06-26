import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a,b = line.strip().split('|')
    list_number = map(int,a.strip().split(' '))
    value = int(b.strip())
    result = []
    for i in range(value):
        for j in range(len(list_number)-1):
            if list_number[j] > list_number[j+1]:
                list_number[j], list_number[j+1] = list_number[j+1], list_number[j]
                break
    print ' '.join(map(str,list_number))
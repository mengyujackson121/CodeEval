import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().split(',')
    L = []
    N = []
    for eachstr in a:
        if eachstr.isdigit() == True:
            N.append(eachstr)
        else:
            L.append(eachstr)

    letters =  ','.join(L)
    numbers = ','.join(N)
    if len(letters) ==  0 :
        print numbers
    elif len(numbers) ==  0 :
        print letters
    else:
        print letters + '|' + numbers


import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    F, B, Limited = map(int,line.strip().split(' '))
    result = []
    for num in range(1,Limited+1):
        if num % F == 0 and num % B == 0:
            result.append("FB")
        elif num % F == 0:
            result.append("F")
        elif num % B == 0:
            result.append("B")
        else:
            result.append(num)
    print ' '.join(map(str,result))
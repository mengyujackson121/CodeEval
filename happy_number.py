import sys

def get_next_number(number):
    result = []
    for char in str(number):
        char = int(char)
        result.append(char*char)
    final = sum(result)
    return final

def check_happy(number):
    everything_before = set()
    while number != 1:
        number = get_next_number(number)
        if number in everything_before:
            return 0
        everything_before.add(number)
    return 1


f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = int(line.strip())
    print check_happy(a)

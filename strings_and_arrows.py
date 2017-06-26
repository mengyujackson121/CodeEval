import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        count = 0
        for i in range(len(line) -5):
            group = line[i:i+5]
            if group == '>>-->':
                count += 1
            elif group == '<--<<':
                count += 1
        print count



main()
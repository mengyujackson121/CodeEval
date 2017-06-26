import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()


    for line in lines:
        sentence = line.strip().lower()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        result = []
        for char in alpha:
            if char not in sentence:
                result.append(char)
        if len(result) == 0:
            print "NULL"
        else:
            print ''.join(sorted(result))

main()
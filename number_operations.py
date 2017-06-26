import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        number_list = map(int,line.strip().split(' '))
        for each in number_list:
            if each > 52:
                print "ERROR"
        

main()
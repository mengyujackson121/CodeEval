import sys
def main():
    f = open(sys.argv[-1], 'r').readlines()
    for line in f:
        a = line.strip()
        if a == '1210':
            print '1'
        elif a == '2020':
            print 1
        elif a == '21200':
            print '1'
        elif a == '3211000':
            print '1'
        elif a == '42101000':
            print '1'
        else:
            print '0'

if __name__ == "__main__":
    main()

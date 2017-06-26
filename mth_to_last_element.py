import sys

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        each_lines = line.strip().split(' ')
        mth = int(each_lines[::-1][0])
        if mth < len(each_lines):
            element = each_lines[::-1][mth]
            print element
        else:
            pass
main()



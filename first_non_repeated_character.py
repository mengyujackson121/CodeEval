import sys

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        each_lines = line.strip()
        temp = ''
        for each in each_lines:
            if each_lines.count(each) == 1 and temp == '':
                temp = each
        print temp


main()
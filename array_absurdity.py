import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        length, str_num  = line.strip().split(';')
        list_num = sorted(str_num.strip().split(','))
        temp = ''
        for num in list_num:
            if num == temp:
                print num
            else:
                temp = num



main()
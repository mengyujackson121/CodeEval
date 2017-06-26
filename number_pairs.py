import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()

    for line in lines:
        str_num, key_num = line.strip().split(';')
        list_num = sorted(map(int,str_num.strip().split(',')))
        list_result = []
        length = 0
        for first in list_num:
            length += 1
            for second in list_num[:length - 1]:
                if first + second == int(key_num):
                    result = str(second) + ','+ str(first)
                    list_result.append(result)
        if len(list_result) > 0:
            print ';'.join(list_result[::-1])
        else:
            print 'NULL'

main()
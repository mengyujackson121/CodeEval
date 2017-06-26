import sys


def all_there(n,result):
    for each in range(1,n -1):
        if each not in result:
            return False
    return True

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        str_num  = map(int, line.strip().split(' '))
        n, num_list = str_num[0], str_num[1:]
        temp = num_list[0]
        result = []
        for num in num_list[1:]:
            if abs(num - temp) in range(1,n):
                result.append(abs(num - temp))
                temp = num
            else:
                result.append('error')
        if 'error' in result:
            print 'Not jolly'
        elif all_there(n, result):
            print "Jolly"
        else:
            print 'Not jolly'


main()
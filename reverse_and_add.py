import sys


def check_p(num):
    reverse_num = int(num[::-1])
    sum_num = str(int(num) + reverse_num)
    if sum_num == sum_num[::-1]:
        return 1,sum_num
    else:
        order,sum_num=check_p(sum_num)
        return order + 1,sum_num

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        num = line.strip()
        count,result = check_p(num)
        print count,result
main()
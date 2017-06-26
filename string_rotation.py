import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        first, second = line.strip().split(',')
        temp = []
        T_F = False
        for each in first:
            temp.append(each)
        for time in range(1,len(temp)):
            new_temp = temp[time:] + temp[:time]
            if ''.join(new_temp) == second:
                T_F = True
        print T_F
main()
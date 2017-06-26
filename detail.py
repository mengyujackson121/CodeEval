import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        each_line = line.strip().split(',')

        count = []
        for each in each_line:
            # new_each = each[each.rindex('X'):each.index('Y')]
            # count.append(new_each.count('.'))
            count.append(each.index('Y') - each.rindex('X') - 1)
        print min(count)


main()
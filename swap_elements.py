import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        number_line, swap = line.strip().split(':')
        number_line_list = number_line.strip().split(' ')
        swap_list = swap.strip().split(', ')
        split_list = map(str.split, swap_list,['-'] * len(swap_list))
        for first,second in split_list:
            number_line_list[int(first)],number_line_list[int(second)] = number_line_list[int(second)],number_line_list[int(first)]
        print ' '.join(number_line_list)

main()
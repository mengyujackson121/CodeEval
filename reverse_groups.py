import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        num_line, sprit_num = line.strip().split(';')
        num_list =  num_line.strip().split(',')
        int_split = int(sprit_num)
        list_piece = []
        while int(len(num_list)) >= int_split:
            next_piece = num_list[:int_split]
            list_piece.append(','.join(next_piece[::-1]))
            num_list = num_list[int_split:]
        if len(num_list) > 0:
            list_piece.append(','.join(num_list))
        print ','.join(list_piece)
main()
import sys


def split_list(new_list):
    if len(new_list) % 2 == 0:
        a, b = new_list[:(len(new_list) / 2)], new_list[(len(new_list) / 2):]
        e = zip(a,b)
        return  list(e)
    else:
        a, b, c = new_list[:(len(new_list) / 3)], new_list[(len(new_list) / 3):(len(new_list) / 3 * 2)], new_list[(len(new_list) / 3 * 2):]
        e = zip(a,b,c)
        return  list(e)

def sq_list(new_list):
    n_List = []
    for all in new_list:
        soduku = []
        for char in all:
            for cha in char:
                soduku.append(cha)
        n_List.append(soduku)
    return n_List

def match(List,N):
    for each in List:
        if map(int,sorted(each)) == map(int,range(1, N + 1)):
            return True
        else:
            return False


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        size, num = line.strip().split(';')
        list_num = map(int,num.strip().split(','))
        N = int(size)
        Hor_List = [list_num[n:n + N] for n in range(0, len(list_num), N)]
        Ver_List = [list_num[n::N] for n in range(0,N)]
        sq_List = []
        n = int(N**(0.5))
        new_list = [list_num[i:i + n] for i in xrange(0, len(list_num), n)]
        if len(new_list) % 2 == 0:
            a, b = new_list[:(len(new_list) / 2)], new_list[(len(new_list) / 2):]
            new_a = split_list(a)
            new_b = split_list(b)
            sq_List.append(sq_list(new_a))
            sq_List.append(sq_list(new_b))
        else:
            a, b, c = new_list[:(len(new_list) / 3)], new_list[(len(new_list) / 3):(len(new_list) / 3 * 2)], new_list[(len(new_list) / 3 * 2):]
            new_a = split_list(a)
            new_b = split_list(b)
            new_c = split_list(c)
            sq_List.append(sq_list(new_a))
            sq_List.append(sq_list(new_b))
            sq_List.append(sq_list(new_c))
        new_sq = []
        for each in sq_List:
            for char in each:
                new_sq.append(char)

        if match(Hor_List,N) and match(Ver_List,N) and match(new_sq,N):
            print 'True'
        else:
            print 'False'


main()
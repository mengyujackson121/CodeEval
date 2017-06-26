import sys

def remove_list(name_list,number):
    while len(name_list) <= number:
        name_list = name_list * 2
    value_remove = name_list[number]
    while value_remove in name_list:
        name_list.remove(value_remove)
    return name_list


def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        name, number = line.strip().split('|')
        name_list = name.strip().split(' ')
        while len(set(name_list)) > 1:
            name_list = remove_list(name_list,int(number)-1)
        print name_list[0]
main()
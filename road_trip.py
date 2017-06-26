import sys


def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        data = line.strip().rstrip(';').split(';')
        new_distances = []
        for name, distances in map(str.split, data, [','] * len(data)):
            new_distances.append(int(distances))
        new_distances.sort()
        different_list = []
        temp_each = 0
        different = 0
        for each in new_distances:
            if different == 0:
                different = each
                different_list.append(str(different))
            else:
                different = each - temp_each
                different_list.append(str(different))
            temp_each = each

        print ','.join(different_list)

main()
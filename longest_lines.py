import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    all_list = []
    for line in lines[1:]:
        all_list.append(line.strip())
    all_list.sort(key=len,reverse=True)
    for each in all_list[:int(lines[0])]:
        print each

main()
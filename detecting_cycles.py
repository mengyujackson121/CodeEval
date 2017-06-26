import sys

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        each_lines = line.strip().split(' ')
        temp = []
        for each in each_lines[::-1]:
            if each not in temp:
                temp.append(each)
            else:
                break
        print ' '.join(temp[::-1])

main()
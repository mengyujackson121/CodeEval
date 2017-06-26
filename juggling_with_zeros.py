import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:

        number_list = line.strip().split(' ')
        binary = []
        for i in range(0,len(number_list),2):
            if number_list[i] == '0':
                binary.append(number_list[i + 1])
            elif number_list[i] == '00':
                binary.append('1' * len(number_list[i+1]))
        print int(''.join(binary),2)

main()

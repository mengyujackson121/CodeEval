import sys


def decode(num_string, decoded= ''):
    num_way = 0
    if len(num_string) == 0:  #base case
        print decoded
        return 1
    if len(num_string) > 1 and int(num_string[:2]) in range(10,27):
        num_way += decode(num_string[2:], decoded + num_string[:2] + ' ')
    if int(num_string[0]) in range(1,10):
        num_way += decode(num_string[1:], decoded + num_string[0] + ' ')

    return num_way

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        print decode(line.strip())
        print "--------------"

main()
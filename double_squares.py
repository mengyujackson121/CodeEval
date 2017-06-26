import sys
import time
import math

def main():
    first_time = True
    start = time.time()
    lines = open(sys.argv[-1], 'r').readlines()

    for line in lines:
        if first_time == True:
            first_time = False
            continue
        number = int(line.strip())
        new_number_list = []
        size = 0
        for each in range(0, int(math.sqrt(number))+ 1):
            new_number_list.append((each)*(each))
        a_pos = 0
        b_pos = len(new_number_list) - 1
        while a_pos <= b_pos:
            a = new_number_list[a_pos]
            b = new_number_list[b_pos]
            if a + b < number:
                a_pos = a_pos + 1
            elif a + b > number:
                b_pos = b_pos - 1
            else:
                size = size + 1
                a_pos = a_pos + 1

        print size
    #print time.time() - start
main()
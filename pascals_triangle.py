import sys
import math

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def pascals_triangle(rows):
    result = [] # need something to collect our results in
    for count in range(rows): # start at 0, up to but not including rows number.
        row = [] # need a row element to collect the row in
        for element in range(count + 1):
            row.append(str(combination(count, element)))
        result.append(row)
    return result #','.join(result)

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    final_result = []
    for line in lines:
        level_size = int(line.strip())
        final_result = []
        for row in pascals_triangle(level_size):
            final_result.append(' '.join(row))
        print ' '.join(final_result)

main()


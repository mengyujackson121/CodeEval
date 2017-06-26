# This project to find the highest score in group list
# input file
# 72 64 150 | 100 18 33 | 13 250 -6
# 10 25 -30 44 | 5 16 70 8 | 13 1 31 12
# 100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143
# output
# 100 250 150
# 13 25 70 44
# 100 200 300 400 500
# Steps:
# 1. read the file by each line
# 2. break token by '|'
# 3. break by token again after break by '|'
# 4. find the Highest
# 5. join in a list.
# 6. print it out
########################
import sys

file_name = sys.argv[-1]
f = open(file_name,'r')
s = f.readlines()

for line in s:

    token = line.split('|')
    new_token = []
    for string in token:
        t = string.strip()
        a = t.split()
        list_number= [int(integer) for integer in a]
        new_token.append(list_number)

    n = []
    for numberlist in new_token[0]:
        n.append([])
    for numberlist in new_token:

        index = 0
        for number in numberlist:
            n[index].append(number)
            index = index + 1
    for something in n:
        print max(something),
    print

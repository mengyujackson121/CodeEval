import sys
import re

file_name = sys.argv[-1]
f = open(file_name,'r')
s = f.readlines()

for line in s:
    token = re.findall(r"[0-9]", line)
    list_number = [int(integer) for integer in token]

    print sum(list_number)

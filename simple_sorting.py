import sys

file_name = sys.argv[-1]
f = open(file_name,'r')
s = f.readlines()

for line in s:
    t = line.strip()
    a = t.split()
    list_number = [float(float_number) for float_number in a]
    new_list_number = sorted(list_number)
    b = ["%.3f" % string for string in new_list_number]
    result = ' '.join(b)
    print result



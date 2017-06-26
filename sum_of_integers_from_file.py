import sys
file_name = sys.argv[-1]
f = open(file_name)
s = f.readlines()

list = []
for line in s:
    t = line.strip()
    list.append(int(t))
print sum(list)
import sys
file_name = open(sys.argv[-1],'r').readlines()

list_number = []
for line in file_name:
    a = line.strip()
    w = ' '.join([piece[0].upper()+ piece[1:]  for piece in a.split()])
    print w

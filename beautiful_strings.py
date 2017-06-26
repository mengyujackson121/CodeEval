import sys

f = open(sys.argv[-1],'r').readlines()

for line in f:
    a = line.strip().lower()
    letter_set = set()
    number = []
    for char in a:
        if char.isalpha():
            letter_set.add(char)
    for letter in letter_set:
        number.append(a.count(letter))
    number.sort(reverse=True)
    beauty = 26
    all = 0
    for value in number:
        all += value * beauty
        beauty -= 1
    print all

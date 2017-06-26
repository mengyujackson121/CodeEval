# This project for clean up the words,
# example
# (--9Hello----World...--)
# Can 0$9 ---you~
# 13What213are;11you-123+138doing7
# output:
# hello world
# can you
# what are you doing
# Steps:
# 1. read input
# 2. list of the symbols and numbers or find out the only word code
# 3. switch with one ' ' space
# 4. lowercase
# 5. print out
##########################
import sys
import re

filename = sys.argv[-1]
f = open(filename,'r')
s = f.readlines()

for line in s:
    token = re.findall(r"[A-Za-z]+", line)
    sentence = ' '.join(token)
    print sentence.lower()

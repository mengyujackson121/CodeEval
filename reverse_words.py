# This project to reverse words
# example:
# Hello World
# Hello codeEval
# pirnt by
# World Hello
# CodeEval Hello
# Step
# 1. read the file or sentence.
# 2. put in list for each line
# 3. reverse word
# 4. print in loop
#####################
import sys

file_name = sys.argv[-1]
f = open(file_name,'r')
s = f.readlines()

for line in s:
    token = line.split()
    print ' '.join(reversed(token))


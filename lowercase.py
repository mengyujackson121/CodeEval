#This project for switch upper case to lower case
#Steps
#1. read file name from commond line.
#2. we need get the input data (txt file)
#3. switch uppercase to lowercase----check
#4. print result---check
######################
import sys

filename = sys.argv[-1]
f = open(filename,'r')
s = f.read()
print (s.lower())
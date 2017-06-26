# how to do this project
# 1. read all data in
# 2. break to letters.
# 3. give a number for each letter
#   1. change all letter be number
#   2. number +4
#   3. change back be letters
# 4. replace by the letter number + 4
# 5. print it out

import sys
import string
file_name = open(sys.argv[-1],'r').readlines()

def shift(letter):
    if letter.isupper():
        index = string.uppercase.index(letter)
        return string.uppercase[(index + 4) % len(string.uppercase)]
    elif letter.islower():
        index = string.lowercase.index(letter)
        return string.lowercase[(index + 4) % len(string.lowercase)]
    else:
        return letter



for line in file_name:
    print line
    a = list(line.strip())
    c = []
    for letter in a:
        b = shift(letter)
        c.append(b)
    print ''.join(c)

  #  for new_number in number:
   #     id = dict(zip(string.letters, [ord(c) % 32 for c in string.letters]))
    #    c = di[new_number]
     #   print c



#N = 0
#def is_need_replace(a):
#    for replace_letter in a[N]:
#        if N == 0:
#            return False
#        else:
#            return True
#    N = N + 1

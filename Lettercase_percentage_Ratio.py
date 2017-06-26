from __future__ import division
import sys

f = open(sys.argv[-1]).readlines()



for line in f:
    a = line.strip()
    upper_case = 0
    lower_case = 0
    for letter in a:
        if letter.isupper():
            upper_case = upper_case + 1
        elif letter.islower():
            lower_case = lower_case + 1
        else:
            pass
    sum = int(lower_case) + int(upper_case)
    lower_percentage = lower_case / sum
    upper_percentage = upper_case / sum
    print 'lowercase: '+("{0:.2f}".format(round(100 * lower_percentage,2)))+ ' uppercase: '+("{0:.2f}".format(round(100 * upper_percentage,2)))




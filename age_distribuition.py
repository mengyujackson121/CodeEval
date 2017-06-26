import sys
f = open(sys.argv[-1], 'r').readlines()

for line in f:
    a = int(line.strip())

    if 0 <= a <= 2:
        print 'Still in Mama\'s arms'
    elif 3 <= a <= 4:
        print 'Preschool Maniac'
    elif 5 <= a <= 11:
        print 'Elementary school'
    elif 12 <= a <= 14:
        print 'Middle school'
    elif 15 <= a <= 18:
        print 'High school'
    elif 19 <= a <= 22:
        print 'College'
    elif 23 <= a <= 65:
        print 'Working for the man'
    elif 66 <= a <= 100:
        print 'The Golden Years'
    else:
        print "This program is for humans"


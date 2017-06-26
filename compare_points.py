import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        O,P,Q,R = map(int,line.strip().split(' '))
        X = Q - O
        Y = R - P
        if X == 0 and Y == 0:
            print 'here'
        elif X == 0 and Y < 0:
            print "S"
        elif X == 0 and Y > 0:
            print 'N'
        elif X < 0 and Y == 0:
            print 'W'
        elif X > 0 and Y == 0:
            print "E"
        elif X > 0 and Y > 0:
            print "NE"
        elif X > 0 and Y < 0:
            print 'SE'
        elif X < 0 and Y > 0:
            print 'NW'
        elif X < 0 and Y < 0:
            print "SW"



main()
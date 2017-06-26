import sys
import math
f = open(sys.argv[-1],'r').readlines()

for line in f:
    a,b,c = line.strip().split(';')
    a, center = a.strip().split(':')
    b, radius = b.strip().split(':')
    c, point = c.strip().split(':')
    center = center[2:-1]
    x_center,y_center = map(float,center.strip().split(','))
    radius = float(radius.strip())
    point = point[2:-1]
    x_point, y_point = map(float,point.strip().split(','))
    if math.sqrt((x_center-x_point)**2 + (y_center - y_point)**2) <= radius:
        print 'true'
    else:
        print "false"
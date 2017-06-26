import sys
import calendar
from datetime import date, timedelta
from datetime import datetime, timedelta
from collections import OrderedDict

f = open(sys.argv[-1],'r').readlines()


month_dict = dict((v,k) for k,v in enumerate(calendar.month_abbr))

def main():
    for line in f:
        a = line.strip().split("; ")
        date_set = set()
        for element in a:
            start, end = element.split('-')
            start_month, start_year = start.split(' ')
            end_month, end_year = end.split(' ')
            d1 = start_year + ' ' + str(month_dict[start_month]) + " 1"
            d2 =end_year  + ' ' + str(month_dict[end_month]) + " 15"
            dates = d1,d2
            start_date, end_date = [datetime.strptime(_, "%Y %m %d") for _ in dates]
            result = set(OrderedDict(((start_date + timedelta(_)).strftime(r"%Y %m"), None) for _ in xrange((end_date - start_date).days)).keys())
            date_set |= result
        print len(date_set)/12

main()

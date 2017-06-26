import sys


def main():
    dict={int(value*100): key for key, value in
            {'PENNY': .01,
            'NICKEL': .05,
            'DIME': .10,
            'QUARTER': .25,
            'HALF DOLLAR': .50,
            'ONE': 1.00,
            'TWO': 2.00,
            'FIVE': 5.00,
            'TEN': 10.00,
            'TWENTY': 20.00,
            'FIFTY': 50.00,
            'ONE HUNDRED': 100.00}.items()}
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        first, second = map(float,line.strip().split(';'))
        if first > second:
            print 'ERROR'
        elif first == second:
            print "ZERO"
        else:
            different = int(second * 100) - int(first * 100)
            list_money = []
            while different > 0:
                next_decimal = max(d for d in dict.keys() if d <= different)
                list_money.append(dict[next_decimal])
                different -= next_decimal
            print ','.join(list_money)

main()
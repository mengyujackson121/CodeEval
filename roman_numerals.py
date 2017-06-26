import sys

def get_roman(each,value1,value5,value10):
    number_list = []
    if int(each) == 9:
        number_list.append(value1 +value10 )
    elif 9 > int(each) > 5:
        number_list.append(value5 + (int(each) - 5) * value1)
    elif int(each) == 5:
        number_list.append(value5)
    elif int(each) == 4:
        number_list.append(value1 + value5)
    elif int(each) < 4:
        number_list.append(value1 * int(each))
    result = ''.join(number_list)
    return  result


def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        number = line.strip()
        new_number = number[::-1]
        value1 = 'I'
        value5 = 'V'
        value10 = 'X'
        value50 = 'L'
        value100 = 'C'
        value500 = 'D'
        value1000 = 'M'
        n = 1
        new_number_list = []
        while n <= len(new_number):
            for each in new_number:
                if n == 1:
                    new_number_list.append(get_roman(each,value1,value5,value10))
                    value1 = value10
                    value5 = value50
                    value10 = value100
                if n == 2:
                    new_number_list.append(get_roman(each,value1,value5,value10))
                    value1 = value100
                    value5 = value500
                    value10 = value1000
                if n == 3:
                    new_number_list.append(get_roman(each,value1,value5,value10))
                if n == 4:
                    new_number_list.append(value10 * int(each))
                n += 1
            print ''.join(new_number_list[::-1])

main()
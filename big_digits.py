import sys


def number_order(number_list):
    input1 = '-**----*--***--***---*---****--**--****--**---**--'
    input2 = '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-'
    input3 = '*--*---*---**---**--****-***--***----*---**---***-'
    input4 = '*--*---*--*-------*----*----*-*--*--*---*--*----*-'
    input5 = '-**---***-****-***-----*-***---**---*----**---**--'
    input6 = '--------------------------------------------------'
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    line6 = []
    for num in number_list:
        line1.append(input1[(num * 5):(num + 1) * 5])
        line2.append(input2[(num * 5):(num + 1) * 5])
        line3.append(input3[(num * 5):(num + 1) * 5])
        line4.append(input4[(num * 5):(num + 1) * 5])
        line5.append(input5[(num * 5):(num + 1) * 5])
        line6.append(input6[(num * 5):(num + 1) * 5])
    print ''.join(line1)
    print ''.join(line2)
    print ''.join(line3)
    print ''.join(line4)
    print ''.join(line5)
    print ''.join(line6)


def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        number_list = []
        for number in line:
            if number.isdigit():
                number_list.append(int(number))
        number_order(number_list)


main()

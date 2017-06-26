import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        list_line = line.strip().split(' ')
        number, rest = int(list_line[0]),list_line[1:]
        lower_bond = 0
        upper_bond = number
        for each in rest:
            guess = (lower_bond + upper_bond + 1) / 2
            if each == "Lower":
                upper_bond = guess - 1
            elif each == "Higher":
                lower_bond = guess + 1
            else:
                print guess
main()
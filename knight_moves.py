import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        knight_list = []
        step = line.strip()
        letter, number = step[0], int(step[1])
        letter_number = ord(letter)
        if letter != 'h' and number < 7:                             #h,7
            knight_list.append(chr(letter_number + 1) + str(number + 2))
        if letter != 'h' and number > 2:                             #h,2
            knight_list.append(chr(letter_number + 1) + str(number - 2))
        if letter != 'a' and number < 7:                              #a,7
            knight_list.append(chr(letter_number - 1) + str(number + 2))
        if letter != 'a' and number > 2:                              #a,2
            knight_list.append(chr(letter_number - 1) + str(number - 2))
        if letter < 'g' and number < 8:                             #g,8
            knight_list.append(chr(letter_number + 2) + str(number + 1))
        if letter < 'g' and number > 1:                             #g,1
            knight_list.append(chr(letter_number + 2) + str(number - 1))
        if letter > 'b' and number < 8:                              #b,8
            knight_list.append(chr(letter_number - 2) + str(number + 1))
        if letter > 'b' and number > 1:                              #b,1
            knight_list.append(chr(letter_number - 2) + str(number - 1))

        print ' '.join(sorted(knight_list))
main()
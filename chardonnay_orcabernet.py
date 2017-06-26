import sys


def check_in_sentence(character, list_sentence):
    for char in character:
        num_char = character.count(char)
        for list_s in list_sentence:
            num__char_in_list_s = list_s.count(char)
            if num__char_in_list_s < num_char:
                list_sentence.remove(list_s)
    return list_sentence


def main():
    file = open(sys.argv[-1], 'r').readlines()

    for line in file:
        sentence, character = line.strip().split("| ")
        list_sentence = sentence.strip().split(' ')
        count = 1
        lenth = len(list_sentence)
        while (count <= lenth):
            list_sentence = check_in_sentence(character, list_sentence)
            count += 1

        if len(list_sentence) != 0:
            print ' '.join(list_sentence)
        else:
            print 'False'

main()

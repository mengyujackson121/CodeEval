import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()

    for line in lines:
        sentence, key_word = line.strip().split(',')
        key = 0
        if key_word in sentence:
            key += 1
        print key

main()
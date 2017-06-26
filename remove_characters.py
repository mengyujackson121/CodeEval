import sys

def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        sentence, remove = line.strip().split(',')
        for each in remove.strip():
            sentence = sentence.replace(each, '')
        print sentence

main()
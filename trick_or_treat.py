import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        something = line.strip().split(',')
        vampire = int(something[0].strip().split(': ')[1])
        zombies = int(something[1].strip().split(': ')[1])
        witches = int(something[2].strip().split(': ')[1])
        houses =  int(something[3].strip().split(': ')[1])
        result = (vampire * 3 + zombies * 4 + witches * 5) *  houses / (vampire + zombies + witches)
        print result
main()
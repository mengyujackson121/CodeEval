import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()

    for line in lines:
        integers = map(int,line.strip().split(','))
        best_score = max(integers)
        for start in range(0, len(integers) + 1):
            new_int_list = integers[start:]
            for end in range(1,len(new_int_list) + 1):
                best_score = max(best_score,sum(new_int_list[:end]))
        print best_score

        best_score = max(integers)
        for start in range(0, len(integers)):
            for end in range(start+1 ,len(integers) + 1):
                best_score = max(best_score,sum(integers[start:end]))
        print best_score

main()
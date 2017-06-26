import sys
def armstong_numbers(num):
    values = map(int, num)
    number = map(pow, values, [len(num)] * len(num))
    #[ i**len(num) for i in values]
    result = str(sum(number))
    return num == result

def main():
    f = open(sys.argv[-1], 'r').readlines()
    for line in f:
        a= line.strip()
        print armstong_numbers(a)
if __name__ == "__main__":
    main()

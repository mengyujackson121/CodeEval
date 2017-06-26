import sys



def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        num = int(line.strip())
        prime_list = []
        for number in range(2, num):
            prime = True
            for i in range(2, number):
                if (number % i == 0):
                    prime = False
            if prime:
                prime_list.append(str(number))
        print ','.join(prime_list)


main()
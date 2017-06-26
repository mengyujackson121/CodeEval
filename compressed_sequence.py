import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        number_list = line.strip().split(' ')
        result = []
        check = ''
        count = 0
        for each in number_list:
            if each != check:
                if len(check) != 0:
                    result.append(str(count))
                    result.append(check)
                check = each
                count = 1
            else:
                each == check
                count += 1
        result.append(str(count))
        result.append(check)
        print ' '.join(result)
main()
import sys
import string


def is_allowed_1(data):
    set = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',':')
    for char in data:
        if char not in set:
            return False
    return True
def is_allowed_2(data):
    return balanced(data[1:-1])

def is_allowed_3(data):
    for i in range(1,len(data)-1):
        if balanced(data[0:i]) != 'NO' and balanced(data[i:]) != 'NO':
            return True
    return False


def is_allowed_4(data):
    set = (':(',':)')
    if data not in set:
        return False
    return True


def balanced(data):
    if is_allowed_1(data):
        return "YES"

    elif data[0] == '(' and data[-1] == ')':
        return is_allowed_2(data)

    elif is_allowed_4(data):
        return "YES"

    elif is_allowed_3(data):
        return "YES"

    else:
        return "NO"


def main():
    lines = open(sys.argv[-1], 'r').readlines()
    for line in lines:
        data = line.strip()
        for char in string.ascii_lowercase:
            data = data.replace(char, '')
        if len(data)  == 0:
            print "1"
        if len(data) != 0:
            print balanced(data)



main()
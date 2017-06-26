import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        result = []
        for char in line.strip():
            if char.isalpha():
                if char.islower():
                    result.append(char.upper())
                elif char.isupper():
                    result.append(char.lower())
            else:
                result.append(char)
        print ''.join(result)
main()
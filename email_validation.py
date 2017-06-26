import sys


def main():
    lines = open(sys.argv[-1], 'r').readlines()

    for line in lines:
        email_address = line.strip()
        if '@' in email_address and '.com' in email_address and ' ' not in email_address and
            print 'true'
        else:
            print 'false'
main()
import sys
dictionary = {key: value for key, value in zip("abcdefghij","0123456789")}
def lookup(index):
    if index in dictionary.keys():
        return dictionary[index]
    elif index.isdigit():
        return index
    else:
        return ''

def main():
    f = open(sys.argv[-1], 'r').readlines()

    for line in f:
        a = line.strip()
        result = []
        for character in a:
            result.append(lookup(character))
        final =  ''.join(result)
        if len(final) == 0:
            print 'NONE'
        else:
            print final

if __name__ == "__main__":
    main()

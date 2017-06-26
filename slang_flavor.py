import sys

def main():
    file = open(sys.argv[-1], 'r').readlines()
    dic = {1: ', yeah!',
           2: ', this is crazy, I tell ya.',
           3: ', can U believe this?',
           4: ', eh?',
           5: ', aw yea.',
           6: ', yo.',
           7: '? No way!',
           8: '. Awesome!',}
    count = 0
    for line in file:
        sentence = line.strip()
        new_sentence = []
        for char in sentence:
            if char == '.' or char == '!' or char == '?':
                count = count + 1
                if count > 16:
                    count = 1
                if count % 2 == 0:
                    new_sentence.append(dic[count/2])
                else:
                    new_sentence.append(char)
            else:
                new_sentence.append(char)
        print ''.join(new_sentence)

main()
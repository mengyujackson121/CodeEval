import sys
import json


def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        if line.strip():
            value = 0
            libary = json.loads(line)
            for item in libary['menu']['items']:
                if type(item) == dict:
                    if 'label'in item.keys():
                        value = value + item['id']
            print value

main()
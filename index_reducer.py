#!/usr/bin/python
import sys

index = 0


def reducer():
    global index
    for line in sys.stdin:
        if line != '\n':
            (num, word, count) = line.split('\t')
            count = count.strip()
            val = str([index, int(count)])
            index += 1
            res = [word, val]
            sys.stdout.write('\t'.join(res) + '\n')

def main():
    reducer()


if __name__ == '__main__':
    main()

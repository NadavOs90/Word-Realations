#!/usr/bin/python
import sys


def reducer():
    current_word = ''
    total_amount=0
    other_words = {}
    for line in sys.stdin:
        (word, other, amount) = line.split('\t')
        amount = amount.strip()
        amount = int(amount)
        if current_word == '':
            current_word = word
            other_words[other] = amount
        elif current_word == word:
            if other in other_words:
                other_words[other] += amount
            else:
                other_words[other] = amount
        else:
            vec = [[k, v] for k, v in other_words.items()]
            res = [current_word, str(vec)]
            sys.stdout.write('\t'.join(res) + '\n')
            current_word = word
            other_words={}
            other_words[other] = amount
    vec = [[k, v] for k, v in other_words.items()]
    res = [current_word, str(vec)]
    sys.stdout.write('\t'.join(res) + '\n')


reducer()

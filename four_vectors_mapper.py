#!/usr/bin/python
import sys
from ast import literal_eval
from math import log
import operator as op
from rsa._compat import MAX_INT
from gc import collect

all_word_count = {}
count_of_all_words = 0
possible_pairs = 0


def ncr(n, r):
    try:
        r = min(r, n-r)
        if r == 0:
            return 1
        numer = reduce(op.mul, xrange(n, n-r, -1))
        denom = reduce(op.mul, xrange(1, r+1))
        return numer//denom
    except:
        return MAX_INT


def get_other_amount(other):
    ans = int(other[1])
    return max(ans, 1)


def index_count_pair(word):
    global all_word_count
    try:
        index_count = all_word_count[word]
        index_count = literal_eval(index_count)
    except KeyError:
        index_count = [-1, 1000]

    return index_count


def mapper():
    for line in sys.stdin:
        word, others = line.split('\t')
        line = '' # for gc
        others = literal_eval(others)
        others.sort()
        other_words = map(lambda other: other[0], others)
        others_amount = map(lambda other: get_other_amount(other), others)
        other_words = map(lambda x: index_count_pair(x), other_words)
        others = '' # for gc
        collect()
        vec1 = []
        for i in xrange(len(others_amount)):
            new_pair = other_words[i][:]
            new_pair[1] = others_amount[i]
            vec1.append(new_pair[:])
        count_of_word = float(index_count_pair(word)[1])
        vec2 = map(lambda x: round(float(x[1]) / count_of_word, 6), vec1)
        for i in xrange(len(vec2)):
            new_pair = other_words[i][:]
            new_pair[1] = vec2[i]
            vec2[i] = new_pair[:]
        others_amount = map(lambda x: round(float(x) / possible_pairs, 6), others_amount)
        vec3 = []
        vec4 = []
        den1 = count_of_word / count_of_all_words
        for i in xrange(len(others_amount)):
            den2 = float(other_words[i][1]) / count_of_all_words
            den = den1*den2
            new_pair = other_words[i][:]
            if others_amount[i] == 0:
                others_amount[i] = 0.000001
            new_pair[1] = round(log((others_amount[i]/den), 2), 6)
            vec3.append(new_pair[:])
            summ = others_amount[i] - den
            den = den ** 0.5
            new_pair[1] = round(summ / den, 6)
            vec4.append(new_pair[:])
        val = [vec1, vec2, vec3, vec4]
        res = [word, str(val)]
        #sys.stdout.write('\t'.join(res) + '\n')
        yield('\t'.join(res) + '\n')
        collect()
        #print 'vec1', vec1
        #print 'vec2', vec2
        #print 'vec3', vec3
        #print 'vec4', vec4


def main():
    global all_word_count
    global count_of_all_words
    global possible_pairs
    with open('input.txt') as file:
        for line in file:
            (key, val) = line.split('\t')
            all_word_count[key] = val
    count_of_all_words = index_count_pair('count_of_all_words')[1]
    possible_pairs = ncr(count_of_all_words, 2)
    collect()
    #for line in sys.stdin:
        #mapper(line)
    #with open('t') as f:
        #for line in f:
            #mapper(line)
    ans = mapper()
    for four_vector in ans:
        sys.stdout.write(four_vector)


if __name__ == '__main__':
    main()

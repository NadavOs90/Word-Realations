#!/usr/bin/env python

import sys

def mapper():
    count = 1
    current_word = ""
    count_of_all_words = 0
    for line in sys.stdin :
        split_line = line.split('\t')
        word = split_line[0]
        other_words = word_and_feature(split_line)
        if word.isalpha() :
            if current_word == word :
                count+=int(split_line[2])
                count_of_all_words += int(split_line[2])
                count_of_all_words=print_other_words(other_words,split_line[2],count_of_all_words)
            else:
                if  current_word is "" :
                    count = int(split_line[2])
                    current_word = word
                    count_of_all_words += int(split_line[2])
                    count_of_all_words=print_other_words(other_words, split_line[2],count_of_all_words)
                else:
                    count_of_all_words += int(split_line[2])
                    sys.stdout.write("\t".join([current_word,str(count)])+"\n")
                    count_of_all_words=print_other_words(other_words, split_line[2],count_of_all_words)
                    #file2.write("\t".join([current_word, str(count)]) + "\n")
                    count = int(split_line[2])
                    current_word = word
    sys.stdout.write("\t".join([current_word, str(count)]) + "\n")
    count_of_all_words += count
    sys.stdout.write("\t".join(["count_of_all_words", str(count_of_all_words)]) + "\n")
    #file2.write("\t".join(["count_of_all_words", str(count_of_all_words)]) + "\n")
    #file2.write("\t".join([current_word, str(count)]) + "\n")

def word_and_feature(line) :
    other_words = line[1].split(' ')
    other_words = map(lambda sngram: [sngram.split('/')[0], sngram.split('/')[2]], other_words)
    return other_words

def print_other_words(data,count,count_of_all_words):
      count_of_all_words= count_of_all_words
      for i in data:
          if i[0] == "" or i[0] == " " : i[0] = "/"
          if i[0].isalpha():
              sys.stdout.write("\t".join([i[0] + "+" + i[1], str(count)]) + "\n")
              count_of_all_words+=int(count)
      return count_of_all_words
      #file2.write("\t".join([i[0] + "-relation-" + i[1], str(count)]) + "\n")


def main ():
    mapper()

main()
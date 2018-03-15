#!/usr/bin/python
import sys

index = 0

def main():
    reducer()


def reducer():
    current_word1 = ""
    word_pairs={}
    for line in sys.stdin:
        if not line == "" and not line == '\t\n':
            word1,word2,flag,vector = line.split('\t')
            if (current_word1==""):
                current_word1=word1
                word_pairs[word2]=vector.replace("\n",'')
            elif (current_word1==word1):
                dummy=word_pairs.get(word2,"notinthemap")
                if(dummy == "notinthemap"):
                    word_pairs[word2]=vector
                else:
                    result = word1 + '\t' + word2 + '\t' + flag + '\t' + str(vector.replace("\n",'')) + '\t' + str(word_pairs[word2]) + '\n'
                    sys.stdout.write(result)
            else:
                current_word1=word1
                word_pairs={}
                word_pairs[word2]=vector.replace('\n','')


if __name__ == '__main__':
    main()
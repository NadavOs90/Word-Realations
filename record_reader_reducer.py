#!/usr/bin/env python


import sys

def reducer () :
    count = 0
    current_word = ""    
    for line in sys.stdin:
	  word,word_count= line.split('\t')
	  word_count = word_count.replace("\n","")
	  if current_word == word:
	      count += int(word_count)
	  else:
	      if current_word is "":
		  current_word = word
		  count += int(word_count)
	      else:
		  sys.stdout.write("\t".join([current_word, str(count)]) + "\n")
		  count = int(word_count)
		  current_word = word
    sys.stdout.write("\t".join([current_word, str(count)]) + "\n")

def main ():
    reducer()

main()








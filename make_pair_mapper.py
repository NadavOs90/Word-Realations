#!/usr/bin/python
import sys
import ast

data=[]

def main():
    with open ("input3.txt") as file:
        for line in file:
            if not line == "" and not line == '\t\n' :
                line=line.replace('\n','')
                data.append(line.split('\t'))

    ans = mapper()
    for answer in ans:
        sys.stdout.write(answer)


def mapper ():
    for line in sys.stdin:
        if not line == "" and not line == '\t\n' :
            word,vectors=line.split('\t')
            vectors = ast.literal_eval(vectors)
            for v in vectors:
              v.sort()
            for item in data:
                if (item[0]==word or item[1]==word):
                    if "True" in item[2] : result="True"
                    else: result="False"
                    #sys.stdout.write(item[0]+ '\t' + item[1] + '\t' + result+ '\t' + str(vectors) + '\n')
                    yield (item[0]+ '\t' + item[1] + '\t' + result+ '\t' + str(vectors) + '\n')


if __name__ == '__main__':
    main()
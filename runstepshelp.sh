#!/bin/bash
#Defining program variables
INPUT1="/home/guy/tests/abortion_yacht.txt"
OUTPUT1="/home/guy/tests/Ganswers"
INPUT2="/home/guy/tests/Ganswers/part-00000"
OUTPUT2="/home/guy/tests/Ganswers2"
INPUT3="/home/guy/tests/abortion_yacht.txt"
OUTPUT3="/home/guy/tests/Ganswers3"
INPUT4="/home/guy/tests/Ganswers3/part-00000"
OUTPUT4="/home/guy/tests/Ganswers4"
INPUT5="/home/guy/tests/Ganswers4/part-00000"
OUTPUT5="/home/guy/tests/Ganswers5"
INPUT6="/home/guy/tests/Ganswers5/part-00000"
OUTPUT6="/home/guy/tests/Ganswers6"
HADOOP_JAR_PATH="/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar"
STEP1FILES="/home/guy/tests/record_reader_mapper1.py,/home/guy/tests/record_reader_reducer.py"
STEP2FILES="/home/guy/tests/index_mapper.py,/home/guy/tests/index_reducer.py"
STEP3FILES="/home/guy/tests/word_vector_tomer_mapper.py,/home/guy/tests/word_vector_reducer.py"
STEP4FILES="/home/guy/tests/four_vectors_tomer_mapper.py"
STEP5FILES="/home/guy/tests/make_pair_mapper.py,/home/guy/tests/make_pair_reducer.py"
STEP6FILES="/home/guy/tests/similarity_mapper.py"
cachefile="/home/guy/tests/Ganswers/part-00000"
cachefile3="/home/guy/tests/minigold.txt"

$HADOOP_JAR_PATH \
-files $STEP1FILES \
-mapper "python record_reader_mapper1.py" \
-reducer "python record_reader_reducer.py" \
-input $INPUT1 \
-output $OUTPUT1

$HADOOP_JAR_PATH \
-files $STEP2FILES \
-mapper "python index_mapper.py" \
-reducer "python index_reducer.py" \
-input $INPUT2 \
-output $OUTPUT2

/usr/local/hadoop/bin/hadoop fs -put $cachefile3 input2.txt


$HADOOP_JAR_PATH \
-files $STEP3FILES \
-mapper "python word_vector_tomer_mapper.py" \
-reducer "python word_vector_reducer.py" \
-input $INPUT3 \
-output $OUTPUT3

/usr/local/hadoop/bin/hadoop fs -put $cachefile input.txt

$HADOOP_JAR_PATH \
-files $STEP4FILES \
-mapper "python four_vectors_tomer_mapper.py" \
-input $INPUT4 \
-output $OUTPUT4

/usr/local/hadoop/bin/hadoop fs -put $cachefile3 input3.txt

$HADOOP_JAR_PATH \
-files $STEP5FILES \
-mapper "python make_pair_mapper.py" \
-reducer "python make_pair_reducer.py" \
-input $INPUT5 \
-output $OUTPUT5


$HADOOP_JAR_PATH \
-files $STEP6FILES \
-mapper "python similarity_mapper.py" \
-input $INPUT6 \
-output $OUTPUT6


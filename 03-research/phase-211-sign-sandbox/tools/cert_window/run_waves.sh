#!/bin/bash
# resumable: runs parts whose output pickle is missing, W at a time
T=$1; TAU=$2; K2=$3; NP=$4; W=$5; OUT=$6
for ((i=0;i<NP;i++)); do
  f=${OUT%.pkl}_part${i}of${NP}.pkl
  [ -f "$f" ] && continue
  while [ $(pgrep -fc "build_G.py $T ") -ge $W ]; do sleep 10; done
  PART=$i NPART=$NP nohup python3 build_G.py $T $TAU 1 4 $K2 320 $OUT > log_${OUT%.pkl}_part$i.txt 2>&1 &
  sleep 2
done
wait

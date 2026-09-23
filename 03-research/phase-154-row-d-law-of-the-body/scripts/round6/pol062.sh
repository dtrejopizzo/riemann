#!/bin/bash
cd "$(dirname "$0")"
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 7200 python3 r6polish.py lp_X062from058.pkl --out P062from058 > sw_P062from058.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 7200 python3 r6polish.py lp_Q058.pkl --out P058redo > sw_P058redo.log 2>&1 &
wait

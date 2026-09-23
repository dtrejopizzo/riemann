#!/bin/bash
cd "$(dirname "$0")"
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 7200 python3 r6cg.py --T 0.58 --M 24 --out G058M24 > sw_G058M24.log 2>&1 &
wait

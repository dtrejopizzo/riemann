#!/bin/bash
cd "$(dirname "$0")"
for M in 24 32 44 64 96; do
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6ub.py --T 0.58 --M $M --h 0.02 --out T058M$M > sw_ub058M$M.log 2>&1 &
done
wait

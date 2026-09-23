#!/bin/bash
cd "$(dirname "$0")"
for M in 24 32 44 64 96; do
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 20000 \
    python3 r6lp.py --T 0.58 --M $M --h0h 0.08 --iters 60 --out C058M$M > sw_C058M$M.log 2>&1 &
done
wait

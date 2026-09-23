#!/bin/bash
cd "$(dirname "$0")"
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 20000 python3 r6lp.py --T 0.58 --M 24 --U 40 --h0h 0.08 --iters 60 --out C058M24U40 > sw_C058M24U40.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 20000 python3 r6lp.py --T 0.58 --M 24 --U 60 --h0h 0.08 --iters 60 --out C058M24U60 > sw_C058M24U60.log 2>&1 &
wait

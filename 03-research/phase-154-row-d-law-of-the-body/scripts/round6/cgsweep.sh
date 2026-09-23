#!/bin/bash
cd "$(dirname "$0")"
run(){ OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py "$@" & }
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 32  --out G058M32   > sw_G058M32.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 44  --out G058M44   > sw_G058M44.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 64  --out G058M64   > sw_G058M64.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 96  --out G058M96   > sw_G058M96.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 128 --out G058M128  > sw_G058M128.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 24 --U 40 --out G058M24U40 > sw_G058M24U40.log 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nohup timeout 14400 python3 r6cg.py --T 0.58 --M 24 --U 60 --out G058M24U60 > sw_G058M24U60.log 2>&1 &
wait

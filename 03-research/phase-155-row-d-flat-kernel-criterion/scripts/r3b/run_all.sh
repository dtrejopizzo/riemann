#!/bin/bash
# One separate single-process run per (T,M); each < 60 s.  Coverage of M <= 24:
# runs cover M in {7,9,11,13,14,15,16,17,18,19,20,21,22,23,24}; the remaining
# M in {1,2,3,4,5,6,8,10,12} are sublattices of 16, 20 or 24 and need no run.
cd "$(dirname "$0")"
for T in 0.68 log2; do
  for M in "$@"; do
    OMP_NUM_THREADS=1 timeout 115 python3 -u r3b_enclosure.py $T $M 121 6 0.2 \
      > /dev/null 2> r3b_err_${T}_M${M}.log
    python3 -c "
import json;d=json.load(open('r3b_enclosure_${T}_M${M}.json'))
print('T=%-5s M=%2d ceil_dbl=%+.4e a_hi=%+.6e |b|1=%.2e err_s=%.2e BOUND=%+.6e t=%.0fs'%(d['T_name'],d['M'],d['ceil_double'],d['a'][1],abs(d['b0'][1])+abs(d['b1'][1]),d['err_sigma'],d['ceiling_upper_bound'],d['sec_total']))"
  done
done

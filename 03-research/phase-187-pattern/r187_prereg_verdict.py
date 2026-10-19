#!/usr/bin/env python3
"""Step 3 of the preregistration: compares DATA_PREREG_4.csv against the predictions of PREREG_LAW_TEST.md and prints the
verdict table (modifies no file; paste the output into PREREG_LAW_TEST.md §7)."""
import csv, math, re
PRED = {1.128: (13, 82.57, 100.04, 80.13, 76.61, 83.90), 1.236: (18, 113.98, 122.93, 108.00, 102.13, 121.38),
        1.316: (23, 145.40, 144.79, 134.64, 124.93, 161.68), 1.447: (35, 220.80, 194.32, 194.96, 171.11, 266.63)}
BAND = (5.97, 33.2, 5.46, 1.28, 5.85); NAMES = ('L1', 'L2a', 'L2c', 'L3', 'L4')
rows = {round(float(r['T']), 3): r for r in csv.DictReader(open('DATA_PREREG_4.csv'))}
inside = {n: 0 for n in NAMES}; seen = 0
print('| T | N(T*) | y obs = -ln lamA | var. in M (nats) | nneg | ' + ' | '.join(NAMES) + ' | delta = y - 2piN |')
for T, (N, *pred) in sorted(PRED.items()):
    r = rows.get(T)
    if r is None: print(f'| {T} | {N} | (pending) |'); continue
    seen += 1; y = -math.log(float(r['lamA_float'])); yp = -math.log(float(r['lamA_prev']))
    cells = []
    for n, p, b in zip(NAMES, pred, BAND):
        ok = abs(y - p) <= b; inside[n] += ok; cells.append(f'{p} ({"inside" if ok else "OUTSIDE"}, {y-p:+.2f})')
    print(f'| {T} | {int(r["N_Tstar"])} (prereg {N}) | {y:.3f} | {abs(y-yp):.3f} ({r["converged"]}) | {r["nneg"]} {r["nneg_flag"]} | ' + ' | '.join(cells) + f' | {y-2*math.pi*N:+.2f} |')
for n in NAMES:
    out = seen - inside[n]; v = 'HOLDS' if out == 0 and seen == 4 else ('FAILS' if out >= 2 else 'indeterminate/pending')
    print(f'{n}: inside {inside[n]}/{seen} -> {v}')

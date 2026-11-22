#!/usr/bin/env python3
"""quick_refine.py - refine a list of approx zeros, writing output incrementally. Usage: quick_refine.py <idx> <in_pkl_listzeros> <target_dps> <out_pkl> [<deadline_seconds>]
The in_pkl is a pickled list of strings.
"""
import sys, time, pickle, os idx = int(sys.argv[1])
in_pkl = sys.argv[2]
target_dps = int(sys.argv[3])
out_pkl = sys.argv[4]
deadline = float(sys.argv[5]) if len(sys.argv) > 5 else 1e18 with open(in_pkl, 'rb') as f: approx = pickle.load(f) import cypari2
pari = cypari2.Pari()
pari.default("realprecision", target_dps + 5)
pari.allocatemem(2 * 10**9)
pari("L = lfunmf(mfinit([1,12],1), mfeigenbasis(mfinit([1,12],1))[1])") fmt = f"%.{target_dps}g"
refined = []
n_eval = 0
t0 = time.time()
N = len(approx)
for j, s in enumerate(approx): if time.time() - t0 > deadline: print(f"[{idx}] DEADLINE at j={j}/{N}", flush=True) break try: pari(f"t0 = {s} + 0.0") pari("t1 = t0 - 1e-30"); pari("t2 = t0 + 1e-30") for it in range(2): pari("f1 = lfunhardy(L, t1)"); pari("f2 = lfunhardy(L, t2)") pari("t3 = t2 - f2 * (t2 - t1) / (f2 - f1)") pari("t1 = t2"); pari("t2 = t3") n_eval += 2 r = str(pari(f'Strprintf("{fmt}", t2)')) except Exception as e: print(f"[{idx}] fail j={j}: {e}", flush=True) r = s refined.append(r) # incremental dump every 25 zeros if (j+1) % 25 == 0: with open(out_pkl, 'wb') as f: pickle.dump({'mode':'refine','idx':idx,'n':len(refined), 'zeros':refined,'n_eval':n_eval, 'elapsed':time.time()-t0,'completed':False}, f) print(f"[{idx}] {j+1}/{N} elapsed={time.time()-t0:.0f}s", flush=True) with open(out_pkl, 'wb') as f: pickle.dump({'mode':'refine','idx':idx,'n':len(refined), 'zeros':refined,'n_eval':n_eval, 'elapsed':time.time()-t0,'completed':True}, f)
print(f"[{idx}] DONE n={len(refined)}/{N} elapsed={time.time()-t0:.0f}s", flush=True)

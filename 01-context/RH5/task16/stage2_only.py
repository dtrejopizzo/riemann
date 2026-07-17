#!/usr/bin/env python3
"""stage2_only.py - run only the refine stage from existing search pickles."""
import os, sys, subprocess, time, pickle
import numpy as np NUM_SHARDS = 8
TARGET_DPS = 80
N_TARGET = 5000
SHARD_DIR = "ldelta_shards" here = os.path.dirname(os.path.abspath(__file__))
runner = os.path.join(here, "delta_shard_runner.py") print("=== Stage 2: refine ===", flush=True)
procs = []
refine_pkls = []
t2 = time.time()
for i in range(NUM_SHARDS): in_pkl = os.path.join(SHARD_DIR, f"ldelta_search_{i}.pkl") out_pkl = os.path.join(SHARD_DIR, f"ldelta_refine_{i}.pkl") log_path = os.path.join(SHARD_DIR, f"refine_{i}.log") refine_pkls.append(out_pkl) cmd = [sys.executable, runner, "refine", str(i), in_pkl, str(TARGET_DPS), out_pkl] print(f" shard {i}: {in_pkl}", flush=True) lf = open(log_path, "w") p = subprocess.Popen(cmd, stdout=lf, stderr=subprocess.STDOUT) procs.append((p, lf, i)) rc = []
for p, lf, i in procs: ret = p.wait(); lf.close(); rc.append(ret) print(f" refine shard {i} rc={ret} elapsed={time.time()-t2:.1f}s", flush=True)
t_stage2 = time.time() - t2 # Merge
all_zeros = []
for i, pkl in enumerate(refine_pkls): if not os.path.exists(pkl): print(f" WARNING: missing {pkl}") continue with open(pkl, "rb") as f: r = pickle.load(f) print(f" refine shard {i}: n={r['n']} elapsed={r['elapsed']:.1f}s") all_zeros.extend(r["zeros"])
print(f"\nTotal raw: {len(all_zeros)}") pairs = []
for s in all_zeros: try: v = float(s) except Exception: continue pairs.append((v, s))
pairs.sort(key=lambda x: x[0])
dedup, prev = [], None
for v, s in pairs: if prev is not None and abs(v - prev) < 1e-9: continue dedup.append((v, s)); prev = v
print(f"After dedup: {len(dedup)}") trimmed = [s for (_, s) in dedup[:N_TARGET]]
N_actual = len(trimmed)
print(f"N_actual: {N_actual}") GAMMA1_REF = ("9.22237939992110252224376719274347813552877062243200928999818642" "800192129537")
if trimmed: g1 = trimmed[0] nm = 0 for a_, b_ in zip(g1, GAMMA1_REF): if a_ == b_: nm += 1 else: break print(f"gamma_1 matches first {nm} chars of reference") out_npy = f"ldelta_zeros_N{N_actual}_dps{TARGET_DPS}.npy"
arr = np.array(trimmed, dtype="<U81")
np.save(out_npy, arr)
print(f"Saved to {out_npy} (shape={arr.shape}, dtype={arr.dtype})")
print(f"Stage 2 wall: {t_stage2:.1f}s")

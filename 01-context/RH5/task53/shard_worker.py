#!/usr/bin/env python3
"""Subprocess shard worker for L(s, chi_4 mod 5) zero finding.
Usage: shard_worker.py <tmin> <tmax> <dps> <idx> <out_path>
"""
import sys, os, time, json def main(): tmin = float(sys.argv[1]) tmax = float(sys.argv[2]) dps = int(sys.argv[3]) idx = int(sys.argv[4]) out_path = sys.argv[5] import cypari2 pari = cypari2.Pari() pari.allocatemem(10**9) pari.default("realprecision", dps) pari("G = znstar(5, 1)") pari("L = lfuncreate([G, [2]])") t0 = time.time() pari(f"zs = lfunzeros(L, [{tmin}, {tmax}])") elapsed = time.time() - t0 n = int(pari("#zs")) out = [] for i in range(1, n+1): s = pari(f'Strprintf("%.65g", zs[{i}])') out.append(str(s)) result = { "idx": idx, "tmin": tmin, "tmax": tmax, "dps": dps, "elapsed": elapsed, "n": n, "zeros": out, } tmp = out_path + ".tmp" with open(tmp, "w") as f: json.dump(result, f) os.replace(tmp, out_path) print(f"OK idx={idx} [{tmin:.2f},{tmax:.2f}] nz={n} t={elapsed:.1f}s", flush=True) if __name__ == "__main__": main()

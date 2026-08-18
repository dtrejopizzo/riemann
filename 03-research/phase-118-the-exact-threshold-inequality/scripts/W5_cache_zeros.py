"""Cache ordinates gamma_k of nontrivial zeta zeros (1/2+i*gamma_k, gamma_k>0)
via mpmath.zetazero, writing incrementally so the run can be interrupted and
resumed.  mp.zetazero is slow -- compute ONCE, reuse everywhere else in W5.

run:  python3 W5_cache_zeros.py [NMAX] [DPS]
default NMAX=1500, DPS=30.  Writes W5_zeros_cache.json incrementally
(re-run to extend an existing cache: it picks up where it left off).
"""
import json
import os
import sys
import time
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "W5_zeros_cache.json")


def load():
    if os.path.exists(OUT):
        with open(OUT) as f:
            return json.load(f)
    return {"dps": None, "gammas": []}


def save(state):
    tmp = OUT + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f)
    os.replace(tmp, OUT)


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    dps = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    mp.mp.dps = dps

    state = load()
    if state["dps"] is not None and state["dps"] != dps:
        print("cache built at different dps=%s, keeping as-is, dps arg ignored for consistency"
              % state["dps"])
        dps = state["dps"]
        mp.mp.dps = dps
    state["dps"] = dps

    have = len(state["gammas"])
    print("cache has %d zeros already; extending to %d at dps=%d" % (have, nmax, dps))
    t0 = time.time()
    for k in range(have + 1, nmax + 1):
        g = mp.im(mp.zetazero(k))
        state["gammas"].append(mp.nstr(g, dps, strip_zeros=False))
        if k % 25 == 0 or k == nmax:
            save(state)
            elapsed = time.time() - t0
            print("  k=%5d  gamma=%14.6f  elapsed=%.1fs  (%.3fs/zero avg)"
                  % (k, float(g), elapsed, elapsed / (k - have)))
    save(state)
    print("done. total cached:", len(state["gammas"]))


if __name__ == "__main__":
    main()

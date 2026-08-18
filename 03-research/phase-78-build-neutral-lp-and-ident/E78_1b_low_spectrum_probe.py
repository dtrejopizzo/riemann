#!/usr/bin/env python3
"""E78.1b - Low-spectrum / parity-resolved probe.

H_L commutes with the flip J: (Jv)_n = v_{-n}  (verified: entry(-m,-n)=entry(m,n)).
So spec(H_L) splits into even (Jv=v) and odd (Jv=-v) sectors. This probe:
  - reduces H to the even and odd sectors separately (exact block-diagonalization),
  - reports the lowest eigenvalues of each sector vs N,
  - so we can see whether the bottom of spec is a SINGLE simple eigenvalue or a
    near-degenerate even/odd pair collapsing to a common limit (multiplicity>=2).

Reuses P76.002 build_mp verbatim.
"""

import sys
import mpmath as mp

sys.path.insert(
    0,
    "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock",
)
from P76_002_mp_entry_audit import build_mp  # noqa: E402

PLANT = ("14.134725141734693790", "0.30", "5.0")


def parity_blocks(H, idx):
    """Return (H_even, H_odd) via the symmetric/antisymmetric basis of J."""
    n = len(idx)
    pos = {v: i for i, v in enumerate(idx)}
    even_vecs = []
    odd_vecs = []
    seen = set()
    for v in idx:
        if v in seen:
            continue
        seen.add(v)
        seen.add(-v)
        i = pos[v]
        j = pos[-v]
        if v == 0:
            e = mp.zeros(n, 1)
            e[i] = 1
            even_vecs.append(e)
        else:
            s = mp.zeros(n, 1)
            s[i] = 1 / mp.sqrt(2)
            s[j] = 1 / mp.sqrt(2)
            even_vecs.append(s)
            a = mp.zeros(n, 1)
            a[i] = 1 / mp.sqrt(2)
            a[j] = -1 / mp.sqrt(2)
            odd_vecs.append(a)

    def compress(vecs):
        k = len(vecs)
        M = mp.zeros(k)
        for p in range(k):
            Hv = H * vecs[p]
            for q in range(p, k):
                val = (vecs[q].T * Hv)[0]
                M[p, q] = val
                M[q, p] = val
        return M

    return compress(even_vecs), compress(odd_vecs)


def low(vals, k):
    xs = sorted(vals[i] for i in range(vals.rows))
    return xs[:k]


def run():
    dps = 90
    mp.mp.dps = dps
    for build_name, planted in (("zeta", None), ("plant", PLANT)):
        print(f"===== build={build_name}  dps={dps} =====")
        for n_modes in (6, 8, 10, 12, 14):
            H, idx, L = build_mp(6, n_modes, dps, planted=planted)
            He, Ho = parity_blocks(H, idx)
            ve, _ = mp.eigsy(He)
            vo, _ = mp.eigsy(Ho)
            le = low(ve, 3)
            lo = low(vo, 3)
            print(f"N={n_modes:2d}")
            print("   even:", " ".join(mp.nstr(x, 8) for x in le))
            print("   odd :", " ".join(mp.nstr(x, 8) for x in lo))


if __name__ == "__main__":
    run()

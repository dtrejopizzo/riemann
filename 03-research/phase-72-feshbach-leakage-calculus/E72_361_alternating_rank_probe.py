#!/usr/bin/env python3
import numpy as np


def alt_matrix(s, k, v):
    return v @ (np.outer(s, k) - np.outer(k, s)) @ v.T


def run():
    rng = np.random.default_rng(361)
    print("E72.361 alternating-rank CFIR probe")
    print("A=V(sk^T-ks^T)V^T vanishes iff s,k are collinear.")
    print("  N kind          altNorm      minSing[s,k]    condV")
    for n in [2, 3, 5, 8]:
        v = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        while abs(np.linalg.det(v)) < 1e-8:
            v = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        k = rng.normal(size=n) + 1j * rng.normal(size=n)
        lam = 1.7 - 0.4j
        cases = {
            "collinear": -lam * k,
            "perturbed": -lam * k + 0.1 * (rng.normal(size=n) + 1j * rng.normal(size=n)),
        }
        for kind, s in cases.items():
            a = alt_matrix(s, k, v)
            mat = np.column_stack([s, k])
            sig = np.linalg.svd(mat, compute_uv=False)
            print(
                f"{n:3d} {kind:>10s} {np.linalg.norm(a):12.5e} "
                f"{sig[-1]:14.5e} {np.linalg.cond(v):10.4e}"
            )


if __name__ == "__main__":
    run()

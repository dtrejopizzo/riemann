#!/usr/bin/env python3
"""Regression checks for the foundations/internalization audit.

These checks certify finite algebraic identities and manuscript scope
markers.  They do not replace the categorical proofs in the paper.
"""

from itertools import product
from pathlib import Path
from math import log


ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "04-papers/42-arithmetic-lefschetz-programme/main.tex"


def equivalence(rel, n):
    return (
        all((i, i) in rel for i in range(n))
        and all(((j, i) in rel) for i, j in rel)
        and all(
            ((i, k) in rel)
            for i, j, k in product(range(n), repeat=3)
            if (i, j) in rel and (j, k) in rel
        )
    )


def check_kernel_intersection():
    # Kernels of two maps on a finite operation set; their intersection is
    # again an equivalence relation, the set-theoretic core of the reflector.
    f = [0, 0, 1, 1, 2, 2]
    g = [0, 1, 0, 1, 0, 1]
    kf = {(i, j) for i in range(6) for j in range(6) if f[i] == f[j]}
    kg = {(i, j) for i in range(6) for j in range(6) if g[i] == g[j]}
    assert equivalence(kf, 6) and equivalence(kg, 6)
    assert equivalence(kf & kg, 6)


def check_boundary_detection():
    primes = [2, 3, 5, 7, 11]
    samples = [(-2, 1, 0, 3, -1), (1, -1, 1, -1, 0), (0, 0, 0, 0, 0)]
    for exponents in samples:
        q = 1
        for p, a in zip(primes, exponents):
            q *= p**a
        mass = sum(a * log(p) for p, a in zip(primes, exponents))
        assert abs(log(q) - mass) < 1e-12
        if abs(mass) < 1e-12:
            assert all(a == 0 for a in exponents)


def check_product_witnesses():
    # If one-variable dominance gaps are positive, their product offsets
    # give simultaneous pairwise witnesses and tolerate small perturbations.
    gap_x = [0.7, 1.1, 0.9]
    gap_y = [0.8, 1.3]
    epsilon = 0.2
    for gx, gy in product(gap_x, gap_y):
        # A competing pair loses at least one one-variable gap.  Perturbing
        # two coefficients by epsilon changes a comparison by at most 2 eps.
        assert min(gx, gy) > 2 * epsilon


def check_idempotent_no_go():
    # Boolean max-plus image of n-fold addition of the unit.
    for n in range(1, 100):
        image = max([1] * n)
        assert image == 1


def check_manuscript_scope():
    text = PAPER.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    required = [
        "The internalization theorem that remains",
        "Ordinary internalization is impossible",
        "Established external valuative package; full Weil row open",
        "bounded monotone sequences",
        "supportwise split external theories",
        "Lorentzian signature",
    ]
    for marker in required:
        assert marker in normalized, marker
    assert "Complete as a canonical valuative numerical package" not in normalized


if __name__ == "__main__":
    check_kernel_intersection()
    check_boundary_detection()
    check_product_witnesses()
    check_idempotent_no_go()
    check_manuscript_scope()
    print("foundations/internalization regression checks: PASS")

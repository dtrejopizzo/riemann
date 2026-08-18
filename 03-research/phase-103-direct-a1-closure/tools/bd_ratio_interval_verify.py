#!/usr/bin/env python3
"""Exact-rational interval check of the first B_D ratio obstruction.

The interval inputs and arithmetic are imported from the certified finite
verifier used by phase 102, document 217.  No binary floating-point
arithmetic enters the sign decision.
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


VERIFIER = (
    Path(__file__).resolve().parents[2]
    / "phase-102-omega7-closure-campaign"
    / "RH-MASTER-CONTEXT"
    / "tools"
    / "omega7_point4_interval_verify.py"
)
SPEC = spec_from_file_location("phase102_interval_verifier", VERIFIER)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {VERIFIER}")
V = module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def strong_margin(n):
    """Return D_n = 2 lambda_n - lambda_n^arch as a rational interval."""
    arch = V.lambda_arch(n)
    prime = V.lambda_prime(n)
    return arch + 2 * prime


def main():
    # If log B_D(z) = sum D_n z^n/n and B_D=sum b_n z^n, then
    # n b_n = sum_{k=1}^n D_k b_{n-k}.
    d = [V.I(0)] + [strong_margin(n) for n in range(1, 8)]
    b = [V.I(1)]
    for n in range(1, 8):
        total = V.I(0)
        for k in range(1, n + 1):
            total = total + d[k] * b[n - k]
        b.append(total / n)

    # Nondecreasing b_n/b_{n-1} at n=3 is equivalent (all b_j>0) to
    # b_1 b_3 - b_2^2 >= 0.
    minor = b[1] * b[3] - b[2] * b[2]
    # A still weaker attempted route writes 1/B_D=1-sum q_n z^n and
    # asks only q_n >= 0.  Compute those coefficients exactly as intervals.
    q = [V.I(0) for _ in range(8)]
    for n in range(1, 8):
        q[n] = b[n]
        for j in range(1, n):
            q[n] = q[n] - q[j] * b[n - j]

    for n in range(1, 4):
        print(f"D_{n}", d[n].dec(24))
        print(f"b_{n}", b[n].dec(24))
    print("b1*b3-b2^2", minor.dec(24))
    print("q_7", q[7].dec(24))

    if not all(x.lo > 0 for x in b[1:]):
        raise SystemExit("failed to certify b_1,b_2,b_3 > 0")
    if not minor.hi < 0:
        raise SystemExit("failed to certify the decreasing ratio at n=3")
    if not q[7].hi < 0:
        raise SystemExit("failed to certify q_7 < 0")
    print("CERTIFIED: b3/b2 < b2/b1; criterion (14) fails at n=3")
    print("CERTIFIED: q_7 < 0; reciprocal-coefficient positivity also fails")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact-rational small sign gate for the Jordan cocycle pullback.

The interval data are the certified Stieltjes/zeta enclosures used by the
Phase-102 finite verifier.  No binary floating-point arithmetic enters a
sign decision.

For

    H_u(s) = ((s-u-1) zeta(s-u))/((s-1) zeta(s))

and s = 1 + z/(1-z), the first Cayley--Laguerre jet satisfies

    (1-z)^(-1) partial_u H_u|_{u=0} = sum C_n z^n,
    C_n = lambda_n^prime - lambda_{n+1}^prime.

The script certifies that this coefficient sequence already has both signs.
It also checks the mixed signs of the regular boundary jets

    partial_u^k H_u(1)|_{u=0} = -k gamma_{k-1}.
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


def cayley_first_jet(n):
    """Return C_n = P_n-P_{n+1}, P_n=lambda_n^prime."""
    return V.lambda_prime(n) - V.lambda_prime(n + 1)


def boundary_jet(k):
    """Return partial_u^k H_u(1)|_0 = -k gamma_{k-1}."""
    return -k * V.gamma[k - 1]


def main():
    c1 = cayley_first_jet(1)
    c6 = cayley_first_jet(6)

    print("C_1", c1.dec(24))
    print("C_6", c6.dec(24))
    if not c1.hi < 0:
        raise SystemExit("failed to certify C_1 < 0")
    if not c6.lo > 0:
        raise SystemExit("failed to certify C_6 > 0")

    expected = (-1, 1, 1, -1)
    for k, sign in enumerate(expected, start=1):
        q = boundary_jet(k)
        print(f"boundary_jet_{k}", q.dec(24))
        if sign < 0 and not q.hi < 0:
            raise SystemExit(f"failed to certify boundary jet {k} < 0")
        if sign > 0 and not q.lo > 0:
            raise SystemExit(f"failed to certify boundary jet {k} > 0")

    print("CERTIFIED: the first Cayley jet has both signs (C_1<0<C_6)")
    print("CERTIFIED: the first four boundary jets have signs -,+,+,-")


if __name__ == "__main__":
    main()

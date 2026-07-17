#!/usr/bin/env python3
import numpy as np

from E72_254_homogeneous_lm8_interval_certificate import certify
from E72_252_homogeneous_lm8_extended_stress import R0_DEG8, R1_DEG8


BUFFER = 5.0e-6


def run():
    print("E72.255 buffered homogeneous LM8 interval certificate")
    print(f"Adds BUFFER*u^2 with BUFFER={BUFFER:.1e}; equivalently R(0)+=BUFFER.")
    r0 = R0_DEG8.copy()
    r1 = R1_DEG8.copy()
    r0[0] += BUFFER
    r1[0] += BUFFER
    ok0 = certify("K0 buffered homogeneous Pdeg10", r0, 0.70)
    ok1 = certify("K1 buffered homogeneous Pdeg10", r1, 0.60)
    print(f"overall {'PASS' if ok0 and ok1 else 'FAIL'}")


if __name__ == "__main__":
    run()

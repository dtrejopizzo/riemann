#!/usr/bin/env python3
import numpy as np


def logder_residue_value(coeff, multiplicity):
    # Z=z^m, Z'/Z=m/z.  For holomorphic F=sum c_k z^k,
    # Res F Z'/Z = m*c_0.
    return multiplicity * coeff[0]


def principal_part_block(coeff, multiplicity):
    # 1/Z principal part sees c_0,...,c_{m-1}.
    return coeff[:multiplicity]


def run():
    print("E72.360 log-derivative multiplicity audit")
    print("Z=z^m: holomorphic Z'/Z tests see only F(0), while 1/Z sees all Hermite slots.")
    print("  m  case       logderRes        ppNorm       ppBlock")
    for m in [1, 2, 3, 4]:
        f = np.zeros(m + 2, dtype=complex)
        g = np.zeros(m + 2, dtype=complex)
        f[0] = 1.0
        g[0] = 1.0
        if m > 1:
            g[1] = 3.0 - 0.5j
        if m > 2:
            g[2] = -1.0 + 2.0j
        for name, coeff in [("F", f), ("G", g), ("G-F", g - f)]:
            res = logder_residue_value(coeff, m)
            pp = principal_part_block(coeff, m)
            print(
                f"{m:3d} {name:>5s} {abs(res):14.6e} {np.linalg.norm(pp):13.6e} "
                f"{np.array2string(pp, precision=2)}"
            )


if __name__ == "__main__":
    run()

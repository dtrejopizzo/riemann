#!/usr/bin/env python3
import cmath
import math
import numpy as np


def confluent_matrix(a, m):
    mat = np.zeros((m, m), dtype=complex)
    for q in range(m):
        for p in range(m):
            mat[q, p] = ((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1))
    return mat


def qjet_coeff(a, k, m):
    return np.array([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)], dtype=complex)


def solve_coeffs(a, k, m):
    return np.linalg.solve(confluent_matrix(a, m), qjet_coeff(a, k, m))


def closed_coeffs(a, k, m):
    # Let z=s-a.  We match
    #   1/(s+k)=1/(a+k+z)
    # by H(s)=sum_p h_p/(s+a)^(p+1)=sum_p h_p/(2a+z)^(p+1)
    # modulo z^m.  With r=(2a+z)^(-1), z=1/r-2a, and the target becomes
    #   r/(1+(k-a)r).
    # Truncating in powers of r at degree m gives:
    #   h_p = (-1)^p (k-a)^p, p=0..m-1,
    # plus a correction because truncation in r is not the same as truncation in z.
    # The exact coefficients are obtained by polynomial division modulo z^m.
    z_poly = np.polynomial.Polynomial
    z = z_poly([0, 1])
    denom = z_poly([a + k, 1])
    basis = []
    for p in range(m):
        # Taylor coefficients through z^(m-1) of (2a+z)^(-p-1).
        coeff = []
        for q in range(m):
            coeff.append(((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1)))
        basis.append(coeff)
    rhs = [((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)]
    return np.linalg.solve(np.array(basis, dtype=complex).T, np.array(rhs, dtype=complex))


def hermite_norm(coeffs):
    return sum(abs(c) / math.factorial(i) for i, c in enumerate(coeffs))


def run():
    print("E73.027 confluent formula probe")
    print("Compares linear-solve coefficients with closed Taylor-system coefficients.")
    print(" sigma      t    m       |h|_H      maxErr")
    for sigma in [0.05, 0.10, 0.20, 0.40]:
        for t in [5.0, 15.0, 50.0]:
            a = sigma + 1j * t
            k = 1j * (t + 3.0)
            for m in [1, 2, 3, 4, 6, 8]:
                h1 = solve_coeffs(a, k, m)
                h2 = closed_coeffs(a, k, m)
                err = np.max(np.abs(h1 - h2))
                print(f"{sigma:6.2f} {t:6.1f} {m:4d} {hermite_norm(h1):11.3e} {err:11.3e}")


if __name__ == "__main__":
    run()

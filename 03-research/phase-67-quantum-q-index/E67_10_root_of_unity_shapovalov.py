"""
E67.10 -- root-of-unity Shapovalov form: the intrinsic signed certificate.

Everything in Phase 67 up to E67.8 used 0<q<1 -> POSITIVE contravariant form ->
positive certificates -> blind to phase cancellation -> S_abs. E67.9 showed the right
object is the SIGNED index ind_-(A_N - P_lambda).

Quantum algebra supplies a signed (indefinite) form in exactly one regime NOT yet used:
q at a root of unity. For the U_q(su(1,1)) positive discrete series D_y^+ with
  E e_n = sqrt([n+1][n+2y]) e_{n+1},  F e_n = sqrt([n][n+2y-1]) e_{n-1},  E*=F,
the contravariant (Shapovalov) norms are

  r_0 = 1,   r_n = prod_{j=1}^{n} [j]_q [j+2y-1]_q,   [m]_q = (q^m - q^{-m})/(q-q^{-1}).

At 0<q<1: all [m]_q>0 -> r_n>0 -> DEFINITE (no signed index).
At q=e^{i pi/ell}: [m]_q = sin(m pi/ell)/sin(pi/ell) changes sign -> r_n changes sign
-> the form is INDEFINITE and ind_-(n) = #{j<=n : r_j<0} is an intrinsic integer index
(the Jantzen negative-layer count).

This script demonstrates the mechanism is REAL: the signed certificate is native to the
q-algebra at a root of unity, tunable by (ell, y). It does NOT yet claim ind_- of this
form equals ind_-(A_N - P_lambda); that map (weight <- prime jet) is the open construction.
"""
import numpy as np

def qnum(m, q):
    # [m]_q = (q^m - q^{-m})/(q - q^{-1}); q may be complex on the unit circle
    if abs(q - 1) < 1e-14:
        return float(m)
    return (q**m - q**(-m)) / (q - q**(-1))

def shapovalov_norms(n_max, y, q):
    """r_n and per-step factors; returns arrays r[0..n_max] and signs."""
    r = np.zeros(n_max+1, dtype=complex)
    r[0] = 1.0
    for n in range(1, n_max+1):
        fac = qnum(n, q) * qnum(n + 2*y - 1, q)
        r[n] = r[n-1] * fac
    return r

def ind_minus(r, tol=1e-9):
    return int(np.sum(r.real < -tol))

def main():
    n_max = 24
    print("Root-of-unity Shapovalov signed index for U_q(su(1,1)) discrete series D_y^+")
    print("="*78)
    print("(1) baseline 0<q<1 : form is DEFINITE (ind_-=0), the old positive regime\n")
    for q in (0.5, 0.8, 0.95):
        for y in (0.5, 1.0, 2.0):
            r = shapovalov_norms(n_max, y, q)
            print(f"  q={q:<5} y={y:<4} ind_-(n<= {n_max}) = {ind_minus(r)}  (min real norm {r.real.min():+.2e})")
    print("\n(2) q = exp(i*pi/ell) root of unity : form is INDEFINITE, signed index appears\n")
    for ell in (5, 7, 11, 13):
        q = np.exp(1j*np.pi/ell)
        row = []
        for y in (0.5, 1.0, 2.0, 3.0):
            r = shapovalov_norms(n_max, y, q)
            row.append(f"y={y}:ind_-={ind_minus(r):2d}")
        print(f"  ell={ell:2d}  q=e^(i*pi/{ell})   " + "   ".join(row))
    print("\n(3) how the negative layers accumulate with the window n (ell=7, y=1):")
    q = np.exp(1j*np.pi/7); r = shapovalov_norms(n_max, 1.0, q)
    acc = [int(np.sum(r[:k+1].real < -1e-9)) for k in range(n_max+1)]
    print("   n     :", " ".join(f"{k:2d}" for k in range(0, n_max+1, 2)))
    print("   ind_- :", " ".join(f"{acc[k]:2d}" for k in range(0, n_max+1, 2)))
    print("\nStructural fact: ind_- of the root-of-unity Shapovalov form is a genuine integer")
    print("signed index (Jantzen negative-layer count), intrinsic to the q-algebra -- the")
    print("type of certificate E67.9 showed Omega_7 needs, and that no 0<q<1 / positive")
    print("mechanism (Haar/CP/q-dim) could supply.")
    print("\nOPEN CONSTRUCTION (next real step): a canonical map (prime jet P_lambda) -> (weight/")
    print("twist of D_y^+) such that ind_-(twisted Shapovalov) = ind_-(A_N - P_lambda). That")
    print("identification -- not a literature lookup -- is what would carry Omega_7.")

if __name__ == "__main__":
    main()

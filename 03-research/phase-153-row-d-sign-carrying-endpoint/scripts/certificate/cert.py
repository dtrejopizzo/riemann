"""R153 CERTIFICATE.  Rigorous interval-arithmetic proof that the Xi_a Weil form
is negative on P_T^{(a)} at T = log 2.   Usage:  python3 cert.py [a] [J]
All arithmetic in mpmath.iv (python-flint absent)."""
import sys, math
import mpmath as mp
from mpmath import iv
from polyalg import peval, pder, pmul, padd, pscal
from assemble import matrices

def _l2sq(P, T):
    Q = pmul(P, P, iv); s = iv.mpf(0)
    for k, x in enumerate(Q):
        if k % 2 == 0: s = s + 2*x*T**(k+1)/(k+1)
    return s

iv.prec = 400

GVEC = {'0.45': ['0.0168', '0', '-0.0494', '0', '-0.0899', '0', '0.5822', '0', '-1', '0', '0.6515'],
        '0.30': ['0.0179', '0', '-0.0518', '0', '-0.0828', '0', '0.5702', '0', '-1', '0', '0.6572']}

def run(astr, J):
    a = iv.mpf(astr); T = iv.log(iv.mpf(2)); L = 2*T
    g = [iv.mpf(x) for x in GVEC[astr]]
    m = len(g)-1
    Q, NM, C, Fs, m0a = matrices(T, a, m, J, iv, True)
    # quadratic forms in g
    q = iv.mpf(0); N2 = iv.mpf(0)
    for i in range(m+1):
        for k in range(m+1):
            if g[i] == 0 or g[k] == 0: continue
            q  = q  + g[i]*g[k]*Q[i][k]
            N2 = N2 + g[i]*g[k]*NM[i][k]
    # autocorrelation of F = sum g_i F_i  (polynomial in r on [0,L])
    c = [iv.mpf(0)]
    for i in range(m+1):
        for k in range(m+1):
            if g[i] == 0 or g[k] == 0: continue
            c = padd(c, pscal(C[i][k], g[i]*g[k], iv), iv)
    # ---- sharp constants for the archimedean tail ------------------------
    # F = sum g_i F_i  as a polynomial on [-T,T]
    F = [iv.mpf(0)]
    for i in range(m+1):
        if g[i] == 0: continue
        F = padd(F, pscal(Fs[i], g[i], iv), iv)
    F1 = pder(F, iv); F2 = pder(F1, iv)
    # Legendre/Nikolskii:  ||P||_inf <= (deg+1)/sqrt(2) * ||P||_{L2(-T,T)} / sqrt(T)
    def supn(P):
        d = len(P)-1
        return (d+1)/iv.sqrt(iv.mpf(2))*iv.sqrt(_l2sq(P, T))/iv.sqrt(T)
    FT, FmT = peval(F, T, iv), peval(F, -T, iv)
    A = (FT**2 + FmT**2)/2                       # = |c'(0+)|  (exact identity)
    B = (2*supn(F)*supn(F1) + iv.sqrt(_l2sq(F, T))*iv.sqrt(_l2sq(F2, T)))/2
    tail = A/J + B/(2*J**2)                      # upper bound for sum_{j>J,pm} E_b
    qup = q + tail
    print(f"--- a = {astr},  T = log 2,  J = {J},  basis dim {m+1} ---")
    print(f"  ||F||^2            = {N2}")
    print(f"  m0a                = {m0a}")
    print(f"  partial form q_J   = {q}")
    print(f"  A=|c'(0)|          = {A}")
    print(f"  B                  = {B}")
    print(f"  arch tail bound    = {tail}")
    print(f"  q_a(F) <=          = {qup}")
    print(f"  Rayleigh <=        = {qup/N2}")
    print(f"  NEGATIVE CERTIFIED : {qup.b < 0}")
    return qup, N2

if __name__ == '__main__':
    astr = sys.argv[1] if len(sys.argv) > 1 else '0.45'
    J = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    run(astr, J)

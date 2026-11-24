"""Numerical observations of Paper 14.

Part 1: sine-kernel Gram of K consecutive zeta zeros above height T0,
        normalized x_i = gamma_i * log(T0/(2 pi)) / (2 pi).
Part 2: moment identity b(k) = (-1)^k a(k) = 2^{2k+3} m_{2k}/(2k)! checked against
        Taylor coefficients of Xi(t) = xi(1/2+it); Turan inequalities and
        Hermite forms of the Jensen polynomials J^{d,n}(X)=sum binom(d,j) gamma(n+j) X^j,
        gamma(k) = k! b(k).
Run: python3 gram.py > output.txt
"""
import numpy as np
import mpmath as mp

K = 25
TS = [100, 1000, 3000, 10000]

def first_index_above(T):
    n = max(1, int(mp.nzeros(T)))
    while float(mp.zetazero(n).imag) <= T:
        n += 1
    return n

print("Part 1: K=%d consecutive zeros above T0, x_i = gamma_i log(T0/2pi)/(2pi)" % K)
print("%6s %10s %10s %12s %10s %8s" % ("T0", "lam_min", "beta_min", "1-sinc(b)", "ratio", "bound"))
for T in TS:
    n0 = first_index_above(T)
    g = np.array([float(mp.zetazero(n0 + i).imag) for i in range(K)])
    x = g * np.log(T / (2 * np.pi)) / (2 * np.pi)
    G = np.sinc(x[:, None] - x[None, :])        # numpy sinc(y) = sin(pi y)/(pi y)
    lam = np.linalg.eigvalsh(G)[0]
    b = np.min(np.diff(x))
    ub = 1 - np.sinc(b)
    print("%6d %10.4f %10.4f %12.4f %10.3f %8s" % (T, lam, b, ub, lam / b**2, "ok" if lam <= ub + 1e-12 else "FAIL"))

mp.mp.dps = 30
print("\nPart 2: moments of Phi")
def Phi(u):
    return mp.fsum((2*mp.pi**2*n**4*mp.e**(9*u) - 3*mp.pi*n**2*mp.e**(5*u))*mp.e**(-mp.pi*n**2*mp.e**(4*u)) for n in range(1, 12))
def m(k):
    return mp.quad(lambda u: u**(2*k)*Phi(u), [0, 0.25, 0.5, 1, 1.5])
def Xi(t):
    s = mp.mpf(1)/2 + 1j*t
    return mp.re(s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s))
NK = 9
b = [2**(2*k+3)*m(k)/mp.factorial(2*k) for k in range(NK)]
tay = mp.taylor(Xi, 0, 8)
for k in range(5):
    print("k=%d  2^(2k+3) m_2k/(2k)! = %s   (-1)^k a(k) from Taylor = %s" % (k, mp.nstr(b[k], 12), mp.nstr((-1)**k*tay[2*k], 12)))
print("Turan b(k)^2 > b(k-1)b(k+1), k=1..%d:" % (NK-2), all(b[k]**2 > b[k-1]*b[k+1] for k in range(1, NK-1)))
gam = [mp.factorial(k)*b[k] for k in range(NK)]
def hermite_min(c):  # c[j] coefficient of X^j
    d = len(c)-1
    e = [(-1)**i * c[d-i]/c[d] for i in range(d+1)]  # elementary symmetric
    p = [mp.mpf(d)]
    for k in range(1, 2*d-1):
        s = (-1)**(k-1)*k*e[k] if k <= d else 0
        for i in range(1, k):
            if i <= d:
                s += (-1)**(i-1)*e[i]*p[k-i]
        p.append(s)
    H = mp.matrix(d, d)
    for i in range(d):
        for j in range(d):
            H[i, j] = p[i+j]
    return min(mp.eigsy(H)[0])
print("Hermite form min eigenvalue of J^{d,n} (normalized by leading coeff):")
for d in range(2, 5):
    for n in range(0, 3):
        c = [mp.binomial(d, j)*gam[n+j] for j in range(d+1)]
        print("  d=%d n=%d  %s" % (d, n, mp.nstr(hermite_min(c), 6)))

"""R156_001: elementary upper bound U(T) >= A_inf(F_T), F_T(t) = t on (-T,T) (odd), and its root.
U(T) = (2T^3/3)(C0 + log coth(T/2) + pi - 2 arctan e^T) + 2T^3(3T+7)/9 - 2 s(T)^2,
s(T) = 4T cosh(T/2) - 8 sinh(T/2).  Derivation: R156_001 Thm 3.1.  Also the mpmath value of A_inf(F_T)."""
import mpmath as mp
mp.mp.dps = 30
C0 = -mp.euler - mp.pi/2 - 3*mp.log(2) - mp.log(mp.pi)
K = lambda x: 1/(2*mp.sinh(x/2)) + 1/(2*mp.cosh(x/2))
tail = lambda T: mp.log(mp.coth(T/2)) + mp.pi - 2*mp.atan(mp.exp(T))
s = lambda T: 4*T*mp.cosh(T/2) - 8*mp.sinh(T/2)
n2 = lambda T: 2*T**3/3
U = lambda T: n2(T)*(C0 + tail(T)) + 2*T**3*(3*T+7)/9 - 2*s(T)**2
V = lambda T: n2(T)*(C0 + tail(T)) + mp.quad(lambda u: u*(6*T**2-u**2)/6*K(u), [0, T, 2*T]) - 2*s(T)**2
print("U(1/2 log 3) =", mp.nstr(U(mp.log(3)/2), 12), "  exact A_inf(F) =", mp.nstr(V(mp.log(3)/2), 12))
rU = mp.findroot(U, 0.5); rV = mp.findroot(V, 0.45)
print("root of U (elementary, PROVED bound on the witness):", mp.nstr(rU, 10))
print("root of exact A_inf(F_T) (mpmath):", mp.nstr(rV, 10))
for T in [0.40, 0.45, 0.50, 0.52, 0.54]:
    print(f"T={T}: U={mp.nstr(U(T),8)}  exact={mp.nstr(V(T),8)}")

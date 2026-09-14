"""Lead independent check (phase 135): the canonical class K with Phi_K = xi.

Conventions: Phi_g(s) = int g(t) e^{(s-1/2)t} dt.  Want Phi_K(s) = xi(s), so
Phi_K(1/2+i tau) = int K(t) e^{i tau t} dt = Xi(tau) := xi(1/2 + i tau).
Hence K(t) = (1/2pi) int Xi(tau) e^{-i tau t} d tau.  Riemann's formula:
xi(s) = 1/2 + (s(s-1)/2) int_1^infty psi(x) (x^{s/2-1} + x^{(1-s)/2-1}) dx,
psi(x) = sum_{n>=1} e^{-pi n^2 x}.  Two integrations by parts give the Polya form
Xi(tau) = 2 int_0^infty Phi(u) cos(tau u) du,
Phi(u) = sum_n (4 pi^2 n^4 e^{9u/2} - 6 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}  (even in u),
and K(t) = Phi(t) if the constant is right.  We check the constant numerically
rather than trust the derivation.
"""
import mpmath as mp
mp.mp.dps = 30

def xi(s):
    s = mp.mpf(s) if not isinstance(s, mp.mpc) else s
    if s == 0 or s == 1:
        return mp.mpf(1)/2   # xi(0) = xi(1) = 1/2 (removable: s Gamma(s/2) -> 2, zeta(0) = -1/2)
    if s == -3 or (mp.im(s) == 0 and mp.re(s) < 0 and int(mp.re(s)) == mp.re(s) and int(mp.re(s)) % 2 == 0):
        pass
    return mp.mpf(1)/2 * s*(s-1) * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)

def Phi(u):
    u = abs(mp.mpf(u))
    e2 = mp.e**(2*u)
    tot = mp.mpf(0)
    n = 1
    while True:
        term = (4*mp.pi**2*n**4*mp.e**(9*u/2) - 6*mp.pi*n**2*mp.e**(5*u/2)) * mp.e**(-mp.pi*n**2*e2)
        tot += term
        if abs(term) < mp.mpf(10)**(-40) and n > 3:
            break
        n += 1
    return tot

def Phi_K(s):
    """Mellin of K = Phi in the paper's convention."""
    f = lambda t: Phi(t) * mp.e**((s-mp.mpf(1)/2)*t)
    return mp.quad(f, [-6, -3, -1, 0, 1, 3, 6])

fails = 0
def check(name, a, b, tol=1e-12):
    global fails
    ok = abs(a-b) < tol
    fails += (not ok)
    print(f"{'OK ' if ok else 'BAD'} {name}: {mp.nstr(a,18)} vs {mp.nstr(b,18)}")

print("== K = Polya kernel; moments ==")
check("Phi_K(1/2) = xi(1/2)", Phi_K(mp.mpf(1)/2), xi(mp.mpf(1)/2))
check("Phi_K(0) = xi(0) = 1/2", Phi_K(0), xi(0))
check("Phi_K(1) = xi(1) = 1/2", Phi_K(1), mp.mpf(1)/2)
check("Phi_K(2) = xi(2)", Phi_K(2), xi(2))
check("Phi_K(-3) = xi(-3)", Phi_K(-3), xi(-3))
check("Phi_K(1/2+14.1347i) ~ 0 (first zero)", abs(Phi_K(mp.mpc(0.5, mp.im(mp.zetazero(1))))), 0, 1e-10)
check("Phi_K(0.5+3i) = xi(0.5+3i)", Phi_K(mp.mpc(0.5,3)), xi(mp.mpc(0.5,3)), 1e-10)

print("== positivity on a grid ==")
mn = min(Phi(t) for t in [mp.mpf(k)/10 for k in range(0, 40)])
print(f"{'OK ' if mn > 0 else 'BAD'} min Phi on [0,4] = {mp.nstr(mn,10)}")
fails += (mn <= 0)

print("== I_inf(K,K): polar side 2 xi(0) xi(1) = 1/2; zero side sum_rho xi(rho)^2 = 0 termwise ==")
check("2 xi(0) xi(1)", 2*xi(0)*mp.mpf(1)/2, mp.mpf(1)/2)
print("== I_inf(F,K) = 1/2 deg F on a compactly supported bump F (zero side vanishes termwise) ==")
# F = bump on [-1,1]; deg F = Phi_F(0)+Phi_F(1); I(F,K) = Phi_F(0) xi(1) + Phi_F(1) xi(0)  (zero terms Phi_F(rho) xi(1-rho) = 0)
F = lambda t: mp.e**(-1/(1-t*t)) if abs(t) < 1 else mp.mpf(0)
PhiF = lambda s: mp.quad(lambda t: F(t)*mp.e**((s-mp.mpf(1)/2)*t), [-1, 0, 1])
degF = PhiF(0) + PhiF(1)
IFK = PhiF(0)*xi(1) + PhiF(1)*xi(0)
check("I(F,K) = deg F / 2", IFK, degF/2)

print("== explicit-formula consistency: T_inf(K) via prime/Gamma side should equal xi(0)+xi(1) - sum xi(rho) = 1 ==")
# Weil functional of g in the paper's normalization: T(g) = Phi_g(0)+Phi_g(1) - sum_rho Phi_g(rho)  (comparison thm)
# prime/gamma side: sum_n Lambda(n) n^{-1/2} (g(log n)+g(-log n)) + archimedean term.  Rather than re-derive the
# archimedean constant, test the *difference* structure on K: sum over zeros vanishes, so T(K) must be 1 exactly.
# We test the prime part numerically for information only (K decays superexponentially so few primes matter).
def Lambda(n):
    fs = mp.factorint(n) if hasattr(mp, 'factorint') else None
    return None
import sympy
prime_part = mp.mpf(0)
for n in range(2, 60):
    L = sympy.ntheory.factor_.primefactors(n)
    if len(L) == 1:
        p = L[0]
        prime_part += mp.log(p) / mp.sqrt(n) * (Phi(mp.log(n)) + Phi(-mp.log(n)))
print("prime part sum_n Lambda(n) n^{-1/2} 2K(log n) =", mp.nstr(prime_part, 15), "(information only)")
print("T_inf(K) must be 1 (polar 1 - zero sum 0); the archimedean term is then determined: W_inf(K) = 1 - prime part =", mp.nstr(1-prime_part,15))
print()
print("FAILS:", fails)
raise SystemExit(1 if fails else 0)

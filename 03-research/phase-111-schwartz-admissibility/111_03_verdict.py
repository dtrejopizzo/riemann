#!/usr/bin/env python3
"""Verifier for 111.03 -- verdict on d1."""
import sys
import mpmath as mp
mp.mp.dps = 25
PASS, FAIL = [], []
def check(n, ok, d=""):
    (PASS if ok else FAIL).append(n); print("[%s] %s  %s" % ("PASS" if ok else "FAIL", n, d))

def xi(s): return (s*(s-1)/2)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
ghat = lambda w: mp.sqrt(mp.pi)*mp.e**(w**2/4)
fhat = lambda w: xi(w)*ghat(w)

def mangoldt(N):
    out, sieve = {}, [True]*(N+1)
    for p in range(2, N+1):
        if sieve[p]:
            for m in range(p*p, N+1, p): sieve[m] = False
            q = p
            while q <= N: out[q] = mp.log(p); q *= p
    return out

print("=== Prop 2.1: the prime sum converges for Schwartz h ===")
L = mangoldt(200000)
h = lambda r: mp.e**(-(mp.log(r))**2)
sums = []
for N in (100, 1000, 10000, 50000, 200000):
    S = mp.fsum(L[n]*h(mp.mpf(n))/mp.sqrt(n) for n in L if n <= N)
    sums.append(S); print("   N=%-7d S=%s" % (N, mp.nstr(S, 14)))
incs = [abs(sums[i+1]-sums[i]) for i in range(len(sums)-1)]
check("prime sum converges (increments collapse under refinement)",
      all(incs[i] >= incs[i+1] for i in range(len(incs)-1)) and incs[-1] < mp.mpf('1e-18'),
      "increments=%s" % [mp.nstr(v, 3) for v in incs])
# control: a non-Schwartz h must DIVERGE, else the test is vacuous
d = [mp.fsum(L[n]/mp.sqrt(n) for n in L if n <= N) for N in (100, 1000, 10000, 200000)]
check("control: with h=1 (not Schwartz) the same sum diverges (test not vacuous)",
      all(d[i] < d[i+1] for i in range(len(d)-1)) and d[-1] > 500,
      "partial sums=%s" % [mp.nstr(v, 6) for v in d])

print()
print("=== Prop 1.1: the xi-divisible probe decays on the critical line ===")
vals = [abs(fhat(mp.mpc('0.5', t))) for t in (1, 10, 50, 200)]
for t, v in zip((1, 10, 50, 200), vals):
    print("   t=%-5d |fhat| = %s" % (t, mp.nstr(v, 8)))
check("probe decays faster than exp(-t^2/4)",
      all(vals[i] > vals[i+1] for i in range(len(vals)-1))
      and vals[-1] < mp.e**(-mp.mpf(200)**2/4))

print()
print("=== Prop 1.2: xi(0)=xi(1)=1/2, so extra conditions are needed ===")
e = mp.mpf('1e-15'); x0, x1 = xi(e), xi(1+e)
check("xi(0)=xi(1)=1/2 (value test), and NOT 0 -- so fhat(0),fhat(1) survive",
      abs(x0-mp.mpf('0.5')) < mp.mpf('1e-12') and abs(x1-mp.mpf('0.5')) < mp.mpf('1e-12')
      and abs(x0) > mp.mpf('0.1'),
      "xi(0)=%s xi(1)=%s" % (mp.nstr(x0, 10), mp.nstr(x1, 10)))

print("\nSummary: %d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL); print("VERDICT: FAILURES PRESENT"); sys.exit(1)
print("VERDICT: ALL CHECKS PASS"); sys.exit(0)

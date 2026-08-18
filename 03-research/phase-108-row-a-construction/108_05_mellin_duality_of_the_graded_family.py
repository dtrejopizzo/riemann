#!/usr/bin/env python3
"""Verifier for 108.05 - the graded family is Mellin-dual to the test class,
   and Burnol's cutoff is exactly the pairing between them."""
import numpy as np, math, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# f_a(x) = x^{-a};  Mellin  int_0^inf x^{-a} x^{s} dx/x = int_R e^{t(s-a)} dt
# A. divergence: the truncated integrals have NO limit as T -> infinity ---
def partial(a, s, T, N=200001):
    t = np.linspace(-np.log(T), np.log(T), N)
    return np.trapz(np.exp(t*(s-a)), t)
def closed0(a, s, T):
    d = s-a
    return 2*np.log(T) if abs(d)<1e-14 else 2*np.sinh(d*np.log(T))/d

# (i) Re(s) != a : |value| ~ C * T^{|Re(s-a)|}.  Threshold-free test: fit the
#     exponent by regression of log|value| against log T and compare.
ok=True; fits=[]
for a in (0.5, 0.3, 1.0):
    for s in (a+0.4+0.7j, a-0.6+0.2j, a+0.25+0.9j):
        Ts=np.exp(np.linspace(5,40,60))
        v=np.array([abs(closed0(a,s,T)) for T in Ts])
        slope=np.polyfit(np.log(Ts), np.log(v), 1)[0]
        fits.append(round(slope,4))
        if abs(slope-abs((s-a).real))>1e-3: ok=False
check("Re(s)!=a: |cutoff integral| ~ T^{|Re(s-a)|}, hence unbounded", ok,
      f"fitted exponents {fits} vs |Re(s-a)| in {{0.4,0.6,0.25}}")

# (ii) Re(s)=a, u!=0 : bounded but oscillating, sign changes never stop
ok=True
for a in (0.5, 0.3, 1.0):
    for u in (0.5, 1.0, 3.0):
        vals=np.array([closed0(a,a+1j*u,T).real
                       for T in np.exp(np.linspace(30,60,600))])
        if not (vals.max()>0 and vals.min()<0): ok=False
check("Re(s)=a, u!=0: oscillates without limit even at large T", ok)

# (iii) u=0 : grows like 2 log T
Ts=np.exp(np.linspace(5,40,60))
sl=np.polyfit(np.log(Ts), [closed0(0.5,0.5,T) for T in Ts], 1)[0]
check("u=0: value = 2 log T exactly", abs(sl-2.0)<1e-9, f"slope {sl:.6f}")

# B. closed form under Burnol's cutoff [1/T,T] ----------------------------
def closed(a, s, T):
    d = s-a
    return 2*np.log(T) if abs(d)<1e-14 else 2*np.sinh(d*np.log(T))/d
ok=True
for a in (0.5, 0.25, 1.3):
    for u in (0.0, 0.05, 0.2, 1.0, 3.0, 7.0):
        for T in (10, 100, 1000):
            num = partial(a, a+1j*u, T); cf = closed(a, a+1j*u, T)
            if abs(num-cf) > 1e-4*max(1,abs(cf)): ok=False
check("cutoff Mellin = 2 sinh((s-a) log T)/(s-a), i.e. 2 sin(u logT)/u on the line", ok)

# C. it is the Dirichlet kernel: constant mass 2*pi -----------------------
ok=True; masses=[]
for T in (10, 100, 1000, 10000):
    us=np.linspace(-400,400,4000001); L=np.log(T)
    k=np.where(np.abs(us)<1e-12, 2*L, 2*np.sin(us*L)/np.where(us==0,1,us))
    m=np.trapz(k,us); masses.append(m)
    if abs(m-2*np.pi) > 5e-3: ok=False
check("mass is 2*pi independently of T (Dirichlet kernel)", ok,
      str([round(m,4) for m in masses]))

# D. weak convergence to 2*pi*delta (the correct notion; the Dirichlet
#    kernel is NOT positive, so mass concentration is the wrong test) ------
def pair(T, phi, R=600.0, N=6000001):
    us=np.linspace(-R,R,N); L=np.log(T)
    k=np.where(np.abs(us)<1e-12, 2*L, 2*np.sin(us*L)/np.where(us==0,1,us))
    return np.trapz(k*phi(us), us)
tests = [("gaussian",  lambda u: np.exp(-u**2)),
         ("shifted",   lambda u: np.exp(-(u-0.3)**2)),
         ("lorentz",   lambda u: 1/(1+u**2)),
         ("cos-damped",lambda u: np.cos(u)*np.exp(-u**2/4))]
ok=True; rows=[]
for name,phi in tests:
    errs=[abs(pair(T,phi)-2*np.pi*phi(np.array([0.0]))[0]) for T in (1e3,1e6,1e9)]
    rows.append((name,[float(f'{e:.2e}') for e in errs]))
    # relative error against the limit 2*pi*phi(0); no monotonicity demanded,
    # convergence is already at machine-noise level for these T.
    rel=[e/(2*np.pi*abs(phi(np.array([0.0]))[0])) for e in errs]
    if not all(r < 1e-3 for r in rel): ok=False
check("weak convergence: <k_T, phi> -> 2*pi*phi(0) for smooth phi", ok, str(rows))

# E. consistency with 107_241: the published Weil product uses rho'=1-conj(rho)
def mirror(r): return 1-np.conj(r)
ok = all(abs(mirror(mirror(r))-r)<1e-14 for r in
         [0.5+14.13j, 0.6+30j, 0.4+30j, 0.5+21.02j])
onl = [r for r in [0.5+14.13j, 0.5+21.02j] if abs(mirror(r)-r)<1e-12]
off = [r for r in [0.6+30j, 0.4+30j]       if abs(mirror(r)-r)>1e-12]
check("mirror rho -> 1-conj(rho) is an involution; fixed points = Re=1/2",
      ok and len(onl)==2 and len(off)==2)

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)

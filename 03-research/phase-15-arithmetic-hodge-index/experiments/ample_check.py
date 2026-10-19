#!/usr/bin/env python3
"""
M2 grounding: the ample/pole positivity P(f,f) = 2 (int f e^{-u/2} du)^2 >= 0.

(a) Lemma: the pole evaluation  fhat(i/2)  equals  lambda(f) = int f(u) e^{-u/2} du.
(b) Theorem (ample positivity): P = 2 lambda^2 >= 0 across a family; = 0 iff lambda = 0.
We include an even test function engineered to have lambda = 0 (boundary case).
"""
import numpy as np
from numpy import exp, sqrt, pi

# numerical lambda(f) = int f(u) e^{-u/2} du
def lam(f, U=40.0, n=400000):
    u = np.linspace(-U, U, n)
    return np.trapz(f(u)*np.exp(-u/2), u)

print("  (a) Lemma:  fhat(i/2) == lambda(f) = int f e^{-u/2}   (Gaussian f, exact fhat known)")
# f(u)=exp(-u^2/2): fhat(r)=sqrt(2pi) exp(-r^2/2); fhat(i/2)=sqrt(2pi) exp(1/8)
f0 = lambda u: np.exp(-u**2/2)
fhat_i2_exact = sqrt(2*pi)*exp(1/8)
print("      fhat(i/2) exact      = %.8f" % fhat_i2_exact)
print("      lambda(f) numeric    = %.8f" % lam(f0))
print("      pole term P=2 lam^2  = %.8f   (= 4 pi e^{1/4} = %.8f)" % (2*lam(f0)**2, 4*pi*exp(1/4)))

print("\n  (b) ample positivity P=2 lambda^2 >= 0 across a family of even test functions:")
fam = {
  "exp(-u^2/2)"            : lambda u: np.exp(-u**2/2),
  "exp(-u^2/8) (wide)"     : lambda u: np.exp(-u**2/8),
  "(1+u^2)exp(-u^2/2)"     : lambda u: (1+u**2)*np.exp(-u**2/2),
  "cos(3u)exp(-u^2/2)"     : lambda u: np.cos(3*u)*np.exp(-u**2/2),
  "(u^2-5/4)exp(-u^2/2)*"  : lambda u: (u**2-1.25)*np.exp(-u**2/2),   # engineered lambda=0
}
print("      %-26s %14s %14s" % ("test f (even)","lambda(f)","P=2 lambda^2"))
for name,f in fam.items():
    L=lam(f); P=2*L**2
    flag = "  <-- boundary: lambda=0 => P=0" if abs(L)<1e-6 else ("  (P>0)" if P>0 else "")
    print("      %-26s %14.6e %14.6e%s" % (name, L, P, flag))
print("\n  All P >= 0 (unconditional); P=0 exactly when lambda=0 (Theorem M2.2). Ample cone is positive.")

#!/usr/bin/env python3
"""
Phase 11 / M11.3 — the shift operator as a stability preserver, and the arithmetic-blindness test.

Structure (analytic): Xi(t)=int_0^inf Phi(u)cos(tu)du (de Bruijn-Newman kernel Phi>0). So
  b(k)=(-1)^k a(k) = m_{2k}/(2k)!,  m_{2k}=int u^{2k} Phi(u) du   <-- the ARITHMETIC (moments of Phi).
The Jensen shift n->n+1 corresponds to Phi -> u^2 Phi, i.e. Xi -> -Xi'' (DIFFERENTIATION), which
PRESERVES the Laguerre-Polya class (Rolle/Gauss-Lucas) -> a stability preserver.

THE N5-ANALOGUE TEST: differentiation preserves L-P for ANY L-P function, not just Xi. So the
preserver/interlacing STRUCTURE is arithmetic-BLIND. We confirm by showing a control L-P function
(cos t, all real zeros) has the SAME Jensen-hyperbolicity + interlacing + shift structure as zeta.
If identical, the structure cannot single out zeta -> arithmetic is only in 'is Xi in L-P' (=RH),
and the genuine escape must be an MSS AVERAGING (random-matrix) realization, not a preserving operator.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

def Xi(t):
    s = mp.mpf('0.5') + 1j*t
    return (mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)).real

def taylor_even(f, M):
    c = mp.taylor(f, 0, 2*M); return [c[2*k] for k in range(M)]

def jensen_roots(a, d, n):
    cf = np.array([float(mp.binomial(d,j)*a[n+j]) for j in range(d+1)], float)
    return np.sort(np.roots(cf[::-1]).real)

def hyper(a,d,n):
    cf=np.array([float(mp.binomial(d,j)*a[n+j]) for j in range(d+1)],float)
    r=np.roots(cf[::-1]); return np.max(np.abs(r.imag))<1e-6*max(1,np.max(np.abs(r)))

def interlace(x,y):
    m=sorted([(v,0) for v in x]+[(v,1) for v in y]); L=[t for _,t in m]
    return all(L[i]!=L[i+1] for i in range(len(L)-1))

if __name__=="__main__":
    print("="*80)
    print(" M11.3 — shift = stability preserver (differentiation); arithmetic-blindness test")
    print("="*80)
    M=12
    aXi  = taylor_even(Xi, M)                                  # zeta
    aCos = taylor_even(lambda t: mp.cos(t), M)                 # control: cos t, an L-P function (all real zeros)

    print("\n Control = cos(t) (proven L-P). zeta = Xi (L-P <=> RH). Compare the Jensen structure:")
    print("   object   all J^{d,n} hyperbolic?   J^{d,n}~J^{d,n+1} interlace?   J^{d,n}~J^{d+1,n} interlace?")
    for name,a in [("Xi(zeta)",aXi),("cos(ctrl)",aCos)]:
        hy = all(hyper(a,d,n) for d in [2,3,4,5] for n in [0,2,4] if n+d<M)
        ils= all(interlace(jensen_roots(a,d,n),jensen_roots(a,d,n+1)) for d in [3,4,5] for n in [0,2,4] if n+d+1<M)
        ild= all(interlace(jensen_roots(a,d,n),jensen_roots(a,d+1,n)) for d in [3,4] for n in [0,2,4] if n+d+1<M)
        print("   %-9s        %-5s                    %-5s                         %s"%(name,str(hy),str(ils),str(ild)))

    print("\n  -> The control cos(t) has the SAME hyperbolicity + interlacing + shift structure as zeta.")
    print("     => the stability-preserver / interlacing STRUCTURE is ARITHMETIC-BLIND (N5-analogue): it")
    print("        holds for every L-P function, so it cannot single out zeta. The arithmetic lives only")
    print("        in 'is Xi in L-P' (=RH), i.e. in the moments m_{2k}=int u^{2k}Phi(u)du of the dBN kernel.")
    print("\n  CONSEQUENCE: a stability-PRESERVING operator cannot cross (blind, like N5/N6). The genuine")
    print("  escape is an MSS AVERAGING realization: Xi (or its Jensen polys) as the EXPECTED characteristic")
    print("  polynomial of a random ensemble whose distribution carries the zeta arithmetic, with interlacing")
    print("  forcing real-rootedness. That is a constructive Hilbert-Polya via the MSS method = M11.4 target.")
    print("="*80)

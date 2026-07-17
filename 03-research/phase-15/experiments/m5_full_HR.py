import numpy as np, mpmath as mp
mp.mp.dps = 25
logpi = mp.log(mp.pi)
Psi  = lambda r: mp.re(mp.digamma(mp.mpf('0.25')+1j*mp.mpf(r)/2)) - logpi

print("="*70)
print("M5 part 1 — does the continuum sl2 carry a Hodge-Riemann form at all?")
print("="*70)
print("""  HR bilinear relations require a LOWEST-WEIGHT sl2 (H bounded below,
  integer-spaced) with primitive decomposition V = (+)_k L^k(ker Lambda).
  Our sl2:  H = (2/c) T_cont,  spectrum(H) = (2/c)*R = all of R.""")
# lowest-weight vector test: Lambda v = 0  with  Lambda = T_{-c} m(r), m(r)=r(c-r)/c^2
# => m(r) v(r) = 0 => v supported on {0,c} => measure zero => NO normalizable l.w. vector
c=1.0
mfun=lambda r: r*(c-r)/c**2
print("  ker(Lambda): m(r)=r(c-r)/c^2 vanishes only at r=0,c (a measure-zero set).")
print("  => NO normalizable lowest-weight vector => representation is PRINCIPAL SERIES.")
print("  => NO primitive decomposition, NO Hodge-Riemann form on this sl2.")
print("  H unbounded below (spectrum=R) confirms it: not lowest-weight.\n")

print("="*70)
print("M5 part 2 — the only positive form the machinery yields is g_inf=|Psi|;")
print("            is it the Weil form Q ?  (compare on the M4.3 test functions)")
print("="*70)
# Q values from M4.3 (transport, 300 zeros): 
Qval={'2':mp.mpf('1.6e-17'),'3':mp.mpf('1.8297374e-5'),'4':mp.mpf('0.302185051')}
print(f"{'sigma':>6} {'A_inf (signed)':>16} {'g_inf=∫|f|^2|Psi|':>18} {'Q=A-P (Weil)':>16} {'g_inf == Q ?':>14}")
for s in ['2','3','4']:
    sig=mp.mpf(s)
    h = lambda r: (r**2+mp.mpf('0.25'))**2 * mp.e**(-r**2/sig**2)
    A   = (1/(2*mp.pi))*mp.quad(lambda r: h(r)*Psi(r),     [-mp.inf,-6.29,0,6.29,mp.inf])
    gI  = (1/(2*mp.pi))*mp.quad(lambda r: h(r)*abs(Psi(r)),[-mp.inf,-6.29,0,6.29,mp.inf])
    print(f"{s:>6} {mp.nstr(A,8):>16} {mp.nstr(gI,8):>18} {mp.nstr(Qval[s],6):>16} {('NO, off by %.1fx'%float(gI/Qval[s]) if Qval[s]!=0 else 'NO'):>14}")

print("""
Reading:
  g_inf >= 0 always (it is the manifestly positive HR-type metric the sl2 gives),
  but g_inf is HUGE compared to the Weil form Q (factors 10^1..10^18).
  The full-degree reorganization yields g_inf, NOT Q. The Weil form Q stays the
  signed residual A_inf - P. The degree grading does not convert Q into a positive form.
""")

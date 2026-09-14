# Certifies the constant s = sup_u |sin(g1 u)| / cosh(u/2)  (g1 = first zero ordinate)
# and the resulting degree threshold d0 = 1/(1-s^2) for the witness of R142.001.
from mpmath import mp, mpf, sin, cosh, findroot, cos, sinh
mp.dps = 40
g1 = mpf('14.134725141734693790457251983562470270784257115699')

def h(u): return abs(sin(g1*u))/cosh(u/2)

# global sup: |sin|<=1 so h(u) <= 1/cosh(u/2) < 0.99 for |u|>0.283; scan [0,0.4] finely
best, bu = mpf(0), mpf(0)
N = 400000
for i in range(N+1):
    u = mpf(i)*mpf('0.4')/N
    v = h(u)
    if v > best: best, bu = v, u
# refine by Newton on derivative of sin(g1 u)/cosh(u/2)
f = lambda u: g1*cos(g1*u)*cosh(u/2) - mpf('0.5')*sin(g1*u)*sinh(u/2)
ustar = findroot(f, bu)
s = sin(g1*ustar)/cosh(ustar/2)
print("argmax u* =", mp.nstr(ustar, 20))
print("s          =", mp.nstr(s, 25))
print("1 - s      =", mp.nstr(1-s, 12))
print("1 - s^2    =", mp.nstr(1-s**2, 12))
print("d0=1/(1-s^2)=", mp.nstr(1/(1-s**2), 12))
# tail check: for |u| >= 0.4, h <= 1/cosh(0.2)
print("bound for |u|>=0.4 :", mp.nstr(1/cosh(mpf('0.2')), 12))
# witness numbers for d = 400, chi = 0 : need s^2 d^2/2 < t^2 W < d^2/2 - d/2
for d in [330, 400, 1000]:
    lo = s**2*mpf(d)**2/2; hi = mpf(d)**2/2 - mpf(d)/2
    print("d=%5d  lo=%s  hi=%s  nonempty=%s"%(d, mp.nstr(lo,12), mp.nstr(hi,12), lo<hi))

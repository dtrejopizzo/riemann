"""NUMERICO: argument-principle count of zeros of Z_Q in the rectangle [s0,1.6]x[t0,t1] (winding of Z_Q along the boundary,
adaptive step so that consecutive phase increments are < 0.5 rad)."""
import mpmath as mp, sys
from zeros_epstein import Z
mp.mp.dps = 20
def wind(s0, s1, t0, t1):
    pts = [mp.mpc(s0, t0), mp.mpc(s1, t0), mp.mpc(s1, t1), mp.mpc(s0, t1), mp.mpc(s0, t0)]
    tot = 0
    for a, b in zip(pts, pts[1:]):
        h = 0.02; x = 0; za = Z(a); L = abs(b - a)
        while x < 1:
            st = min(h / L, 1 - x); zb = Z(a + (b - a) * (x + st)); d = mp.im(mp.log(zb / za))
            if abs(d) > 0.5 and st * L > 1e-6: h /= 2; continue
            tot += d; za = zb; x += st; h = min(h * 1.5, 0.05)
    return tot / (2 * mp.pi)
for (s0, t0, t1) in [(0.52, 0.1, 15.0), (0.52, 15.0, 16.5), (0.52, 16.5, 30.0)]:
    print('zeros of Z_Q in [%g,1.6]x[%g,%g]:' % (s0, t0, t1), mp.nstr(wind(s0, 1.6, t0, t1), 6), flush=True)

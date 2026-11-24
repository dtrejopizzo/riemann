"""Backward-collision times of windows of zeta zeros under the zero flow.

Flow (gamma variable, gamma_j = ordinates of zeros 1/2 + i gamma_j):
    d gamma_j / dt = 2 * sum_{k != j} 1 / (gamma_j - gamma_k),
restricted to a window of N consecutive zeros (zeros outside the window are
omitted).  In the variable z = 2*gamma of H_t the same configuration collides
at time 4*t_c.  Integrator: classical RK4 backward in t with adaptive step
dt = 1e-3 * (min gap)^2; stop when the min gap falls below 1e-3, then
extrapolate t_c linearly in gap^2.  Mean spacing s = 2*pi/log(T/(2*pi)).
"""
import numpy as np, mpmath as mp

def field(g):
    d = g[:, None] - g[None, :]
    np.fill_diagonal(d, np.inf)
    return 2.0 * (1.0 / d).sum(axis=1)

def collide(g):
    g = np.array(g, float); t = 0.0
    while True:
        gaps = np.diff(g); m = gaps.min()
        if m < 1e-3:
            return t - m**2 / 8.0
        h = -1e-3 * m**2
        k1 = field(g); k2 = field(g + h/2*k1); k3 = field(g + h/2*k2); k4 = field(g + h*k3)
        g = g + h/6*(k1 + 2*k2 + 2*k3 + k4); t += h

N = 20
for first in (20, 600, 2500):   # index of first zero in the window
    g = [float(mp.zetazero(n).imag) for n in range(first, first + N)]
    gaps = np.diff(g); i = gaps.argmin()
    T = 0.5 * (g[i] + g[i+1]); s = 2*np.pi/np.log(T/(2*np.pi))
    tc = collide(g)
    print(f"zeros {first}-{first+N-1}: T={T:.1f} mingap={gaps[i]:.3f} s={s:.3f} "
          f"t_c={tc:.4f} two-body={-gaps[i]**2/8:.4f} t_c/s^2={tc/s**2:.4f}")

# Exact check of the strip bound: p_t = exp(-t D^2) p_0, p_0 = (z^2+1/4)(z^2-a^2)
for a in (0.3, 1.0, 3.0):
    p0 = np.poly1d([1, 0, 0.25, 0, 0]) - a**2*np.poly1d([1, 0, 0.25])
    def pt(t): return p0 - t*p0.deriv(2) + t**2/2*p0.deriv(4)
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo+hi)/2
        r = pt(mid).r
        if np.max(np.abs(r.imag)) > 1e-7: lo = mid
        else: hi = mid
    print(f"a={a}: all-real time {hi:.4f} (de Bruijn bound y0^2/2 = 0.125)")

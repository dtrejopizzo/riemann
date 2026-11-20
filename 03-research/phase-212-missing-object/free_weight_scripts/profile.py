"""profile of a saved minimizer: L2 mass by region, dominant frequency (FFT of F sampled), parity."""
import sys, numpy as np
from hp import Basis
f = np.load(sys.argv[1]); T = float(sys.argv[2]); x, p, c = f['x'], int(f['p']), f['c']
B = Basis(x, p); cc = c.reshape(B.E, p)
t = np.linspace(-T, T, 200001)[1:-1]; e = np.searchsorted(x, t) - 1
F = np.array([B.ev(ei, np.array([ti]))[0] @ cc[ei] for ei, ti in zip(e[::10], t[::10])]); ts = t[::10]
dt = ts[1]-ts[0]; m = F**2*dt
print("lam", f['lam'][:3], "arch", float(f['arch']), "arith", float(f['arith']))
for a, b in [(0, 0.01), (0.01, 0.1), (0.1, 0.5), (0.5, 1.5), (1.5, T)]:
    sel = (T-np.abs(ts) >= a) & (T-np.abs(ts) < b); print(f"dist to edge in [{a},{b}): mass {m[sel].sum():.4f}")
Fr = F[::-1]; print("parity: even part mass", (((F+Fr)/2)**2*dt).sum(), "odd", (((F-Fr)/2)**2*dt).sum())
sel = np.abs(ts) < T-0.3; G = np.fft.rfft(F[sel]*np.hanning(sel.sum())); fr = np.fft.rfftfreq(sel.sum(), dt)*2*np.pi
print("interior dominant angular freq", fr[np.argsort(-np.abs(G))[:5]])
np.savetxt(sys.argv[1].replace('.npz', '_profile.txt'), np.c_[ts[::20], F[::20]], fmt='%.6e')

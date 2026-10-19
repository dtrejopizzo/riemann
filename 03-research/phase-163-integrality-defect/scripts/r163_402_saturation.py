"""Small-delta saturation check (uncertified float)."""
import numpy as np, r163_402_light_cone as L
g0 = 0.5*(L.g[300]+L.g[301]); rho = np.log(g0/2/np.pi)/(2*np.pi)
for d in [0.1, 0.01, 0.001]:
    L.ZEROS = None; a = L.Tstar(g0, d)
    L.ZEROS = g0 + (np.arange(-400, 400)+0.5)/rho; b = L.Tstar(g0, d)
    print(f"delta={d}: T*_zeta={a:.3f}  T*_lattice={b:.3f}  pi*rho={np.pi*rho:.3f}")

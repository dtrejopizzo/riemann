"""R156_001 DIAGNOSTIC: one-contact family at T=(1/2)log3, comb weight theta*v_2 (theta=1 is zeta, theta=0 the
prime-free model). Prints Galerkin lamA per parity and the channel constants g_+ = kappa_+ + 2, g_- = kappa_- - 2.
Galerkin values are upper bounds on infima. Usage: python3 r156_theta_family.py N"""
import sys, numpy as np
from r156_green_matrix import build, bordered_kappa, restricted_min
N = int(sys.argv[1]) if len(sys.argv) > 1 else 16
T = 0.5 * np.log(3)
a0, W0, A, B = build(T, N, primes=False)
a1, W1, _, _ = build(T, N, primes=True)
P = a1 - a0                                   # the prime form -v_2 c_F(log 2)
c = 0.5*(A+B); s = 0.5*(A-B); ev = np.arange(0, N, 2); od = np.arange(1, N, 2)
ths = [float(x) for x in sys.argv[2:]] or [0.0, 0.25, 0.5, 0.75, 0.9, 0.95, 1.0, 1.05, 1.1, 1.25]
for th in ths:
    a = a0 + th*P
    ae, ao = a[np.ix_(ev, ev)], a[np.ix_(od, od)]
    le = restricted_min(ae, c[ev][None, :]); lo = restricted_min(ao, s[od][None, :])
    gp = bordered_kappa(ae, c[ev]) + 2; gm = bordered_kappa(ao, s[od]) - 2
    print(f"theta={th:.7f}  lamA ev {le:+.3e} od {lo:+.3e} | g+ {gp:+.3e}  g- {gm:+.3e}")

"""R156_001 DIAGNOSTIC: prime-free model (v=0). Scan T: Galerkin bottoms of A_inf on L2 per parity,
of A_inf on P_T per parity, and the channel constants g_+ = kappa_+ + 2, g_- = kappa_- - 2.
Galerkin values are upper bounds on the infima. Usage: python3 r156_scan_noprimes.py N"""
import sys, numpy as np
from r156_green_matrix import build, bordered_kappa, restricted_min
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
for T in [0.25, 0.30, 0.3466, 0.36, 0.37, 0.38, 0.40, 0.45, 0.50, 0.5493, 0.58]:
    a, Wm, A, B = build(T, N, primes=False)
    ev = np.arange(0, N, 2); od = np.arange(1, N, 2); c = 0.5*(A+B); s = 0.5*(A-B)
    ae, ao = a[np.ix_(ev, ev)], a[np.ix_(od, od)]
    lwe = np.linalg.eigvalsh(Wm[np.ix_(ev, ev)])[0]; lwo = np.linalg.eigvalsh(Wm[np.ix_(od, od)])[0]
    lpe = restricted_min(ae, c[ev][None, :]); lpo = restricted_min(ao, s[od][None, :])
    gp = bordered_kappa(ae, c[ev]) + 2; gm = bordered_kappa(ao, s[od]) - 2
    print(f"T={T:.4f}  lamW ev {lwe:+.4f} od {lwo:+.4f} | lamP ev {lpe:+.4f} od {lpo:+.4f} | g+ {gp:+.4f} g- {gm:+.4f}")

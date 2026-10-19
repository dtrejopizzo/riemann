import mpmath as mp
from zeros_epstein import Z
mp.mp.dps = 25
for t in [x * 0.25 for x in range(66, 120)]:
    for sg in (0.6, 0.8, 1.0, 1.2):
        try: r = mp.findroot(Z, mp.mpc(sg, t))
        except Exception: continue
        if r.real > 0.501 and 16.5 < r.imag < 30: print(mp.nstr(r, 15)); raise SystemExit

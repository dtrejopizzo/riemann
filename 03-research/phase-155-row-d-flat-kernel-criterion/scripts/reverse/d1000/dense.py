"""dense.py NAME [DELTA] -- honest lem:bern enclosure: prime side on a DENSE grid of the
whole LP interval, pad = B2*DELTA^2/8 (no localisation).  DIAGNOSTIC."""
import numpy as np, json, sys, time
import dlib as D, primeside as P
NAME = sys.argv[1]; dl = float(sys.argv[2]) if len(sys.argv) > 2 else 1e-3
d = json.load(open(f"d_{NAME}.json")); T = d["T"]
win = D.Win(T, M=d["M"]); y = np.array(d["y"]); x = np.array(d["x"])
bet = np.array(d.get("beta", [0.0, 0.0])); t0 = time.time()
def ghat(tt):
    xs, ws = np.polynomial.legendre.leggauss(600)
    u = T*(xs+1.0); wq = T*ws; C = np.cos(np.outer(u, np.asarray(tt, float)))
    return np.vstack([2*(wq*np.cosh(u/2)) @ C, 2*(wq*u*np.sinh(u/2)) @ C])
ns, lam = P.prime_table(win.Umax)
tau = np.arange(0.0, d["taumax"]+1e-12, dl)
fp = np.empty(len(tau))
for a in range(0, len(tau), 4000):
    b = min(a+4000, len(tau))
    fp[a:b] = P.f_prime_fast(win, y, x, tau[a:b], ns, lam) + bet @ ghat(tau[a:b])
pad = d["B2"]*dl*dl/8.0
o = dict(name=NAME, delta=dl, npts=len(tau), min_prime_dense=float(fp.min()),
         argmin=float(tau[np.argmin(fp)]), B2=d["B2"], pad=pad,
         certified=float(fp.min()-pad), t=time.time()-t0)
print(json.dumps(o)); json.dump(o, open(f"dense_{NAME}.json", "w"))

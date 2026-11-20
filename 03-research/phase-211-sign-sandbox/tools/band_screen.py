"""Low-frequency screen of the band margin (phase 211, ROUND_017_B).  NUMERICAL tool.
lambda_max of the leading K' x K' block of A_tau (dense, closed form of tools/band_lanczos.py) for K' <= K.
By nesting (Rayleigh-Ritz) lambda_{K'} <= lambda_K, so the screen margin is an UPPER bound for the band margin;
the gap is measured separately by full Lanczos on candidates and on a coarse control grid.
usage: band_screen.py T eta Kp tau_lo tau_hi step out.npz [nproc]"""
import sys, math, numpy as np
from multiprocessing import Pool
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import comb, m_sym

def setup(T, Kp):
    C = comb(T); ln = np.array([math.log(n) for n, _, _ in C]); v = np.array([x for _, _, x in C])
    h = math.pi / (2 * T); j = np.arange(1, Kp + 1); a = h * j; e = (-1.0) ** j
    D = a[:, None] - a[None, :]; np.fill_diagonal(D, 1.0); Cm = 1 / D; np.fill_diagonal(Cm, 0.0)
    Hm = 1 / (a[:, None] + a[None, :])
    return dict(T=T, ln=ln, v=v, SC=np.sin(np.outer(a, ln)), CC=np.cos(np.outer(a, ln)) * (2 * T - ln)[None, :],
                C=Cm, H=Hm, e=e, EE=np.outer(e, e))

def lam(S, tau):
    c = S['v'] * np.cos(tau * S['ln']); s = S['SC'] @ c; d = S['CC'] @ c
    C, H, EE = S['C'], S['H'], S['EE']
    E = C * s[None, :] - EE * C * s[:, None] + EE * H * s[:, None] + H * s[None, :]
    E[np.diag_indices_from(E)] += d
    return float(np.linalg.eigvalsh(0.5 * (E + E.T) / (2 * S['T']))[-1])

def work(args):
    T, Kp, taus = args; S = setup(T, Kp)
    return [(t, float(m_sym(t)) - lam(S, t)) for t in taus]

if __name__ == '__main__':
    T, eta = float(sys.argv[1]), float(sys.argv[2]); Kp = int(sys.argv[3]); lo, hi, step = map(float, sys.argv[4:7])
    fn = sys.argv[7]; npr = int(sys.argv[8]) if len(sys.argv) > 8 else 20
    taus = np.arange(lo, hi + step / 2, step)
    assert int(2 * T * eta * lo / math.pi) >= Kp
    with Pool(npr) as p:
        r = [x for c in p.map(work, [(T, Kp, c) for c in np.array_split(taus, npr * 4)]) for x in c]
    a = np.array(r); np.savez(fn, tau=a[:, 0], margin=a[:, 1]); i = int(np.argmin(a[:, 1]))
    print(f"screen T={T} K'={Kp} n={len(a)} min={a[i,1]:.6f} at tau={a[i,0]:.4f} (tau-lo={a[i,0]-lo:.2f})")

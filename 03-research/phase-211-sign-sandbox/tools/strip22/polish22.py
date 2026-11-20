"""Polish the n lowest local minima of a strip scan (phase 211, ROUND_022_B).  NUMERICAL tool.
Each cell: tools/align_band.cell with ALIGN_WIN = 0.2 (scan +-0.2 step 0.02, bounded Brent xatol 2e-5; eta = 1/4 at the minimiser).
usage: polish22.py scan.npz T n out.npy nproc"""
import sys, os, numpy as np
os.environ.setdefault('ALIGN_WIN', '0.2')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
import align_band as A
from multiprocessing import Pool
if __name__ == '__main__':
    f, T, n, fn, npr = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
    d = np.load(f); t, m = d['tau'], d['margin']
    i = np.where((m[1:-1] < m[:-2]) & (m[1:-1] < m[2:]))[0] + 1; i = i[np.argsort(m[i])][:n]
    done = list(np.load(fn, allow_pickle=True)) if os.path.exists(fn) else []
    dk = {round(r[2], 4) for r in done}
    jobs = [(T, float(t[k]), 'strip', float(m[k])) for k in i if round(float(t[k]), 4) not in dk]
    print(len(jobs), 'cells', flush=True)
    with Pool(npr) as p:
        for r in p.imap_unordered(A.cell, jobs):
            done.append(r); np.save(fn, np.array(done, dtype=object), allow_pickle=True)
            print(r[2], r[4], r[5], r[6], r[7], r[9], flush=True)

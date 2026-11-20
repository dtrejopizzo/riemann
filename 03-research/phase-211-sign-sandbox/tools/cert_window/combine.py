"""Sum the partial Gram data of build_G.py (PART/NPART runs). usage: combine.py out.pkl part0.pkl part1.pkl ..."""
import sys, pickle
from flint import arb, ctx
ctx.prec = 340
out, parts = sys.argv[1], sys.argv[2:]
acc = None
def unser(t):
    m, r = t
    return arb(m, r * 1.0001 + 1e-110 * (1 + abs(float(m))))
def ser(v): return (v.mid().str(110, radius=False), float(v.rad().upper().str(6, radius=False)) * (1 + 1e-5))
for p in parts:
    d = pickle.load(open(p, 'rb'))
    if acc is None:
        acc = d; G = {par: [[unser(t) for t in row] for row in d['G'][par]] for par in (0, 1)}; D = [unser(t) for t in d['D']]
    else:
        for par in (0, 1):
            for a, row in enumerate(d['G'][par]):
                Ga = G[par][a]
                for b, t in enumerate(row): Ga[b] = Ga[b] + unser(t)
        D = [x + unser(t) for x, t in zip(D, d['D'])]
    print('added', p, flush=True)
acc['G'] = {par: [[ser(v) for v in row] for row in G[par]] for par in (0, 1)}
acc['D'] = [ser(v) for v in D]
pickle.dump(acc, open(out, 'wb'))
print('saved', out)

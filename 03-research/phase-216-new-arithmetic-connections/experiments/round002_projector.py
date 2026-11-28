"""Exact rational check of diagonal idempotents; no floating arithmetic."""
from fractions import Fraction as Q
from itertools import product
from math import lcm


def mul(a, b, r, relation):
    out = {}
    for x, u in a.items():
        for y, v in b.items():
            terms = {(0,) * r: u * v}
            for k in range(r):
                power = x[k] + y[k]
                local = [(power, Q(1))] if power < 2 else [(0, Q(relation[0])), (1, Q(relation[1]))]
                nxt = {}
                for z, t in terms.items():
                    for p, q in local:
                        zz = list(z)
                        zz[k] = p
                        zz = tuple(zz)
                        nxt[zz] = nxt.get(zz, 0) + t * q
                terms = nxt
            for z, t in terms.items():
                out[z] = out.get(z, 0) + t
    return {k: v for k, v in out.items() if v}


for name, relation, inverse_gram, expected in [
    ('Q(i)', (-1, 0), [[Q(1, 2), 0], [0, Q(-1, 2)]], [2, 4, 8, 16]),
    ('Q(sqrt5)', (1, 1), [[Q(3, 5), Q(-1, 5)], [Q(-1, 5), Q(2, 5)]], [5, 5, 25, 25]),
]:
    for r in range(2, 6):
        e = {(0,) * r: Q(1)}
        for j in range(1, r):
            pair = {}
            for a, b in product(range(2), repeat=2):
                z = [0] * r
                z[0], z[j] = a, b
                if inverse_gram[a][b]:
                    pair[tuple(z)] = inverse_gram[a][b]
            e = mul(e, pair, r, relation)
        assert mul(e, e, r, relation) == e
        denominator = lcm(*(x.denominator for x in e.values()))
        assert denominator == expected[r - 2]
        print(f'{name}: r={r}, exact scalar denominator={denominator}, idempotent=True')

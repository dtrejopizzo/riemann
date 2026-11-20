"""Fixed rectangle certificate for D_{2*pi}, not for A. No parameter search.

192-bit Arb; 32768 panels per integral, eight theta modes; uniform total
omission bounded by 2^-210 (proof in POWER_GLOBAL_ROUTE_REVIEW.md).
"""
from flint import arb, ctx

ctx.prec = 192
PANELS = 32768
PI = arb.pi()
V = 2 * PI
ERROR = arb(2) ** (-210)


def phi8(t):
    t = abs(t)  # Phi is even; the finite theta prefix itself is not.
    y = PI * (2 * t).exp()
    pref = PI * (arb(5) * t / 2).exp()
    return pref * sum((n*n * (2*n*n*y - 3) * (-n*n*y).exp()
                       for n in range(1, 9)), arb(0))


def integral(lower, delta):
    width = (arb(4) - lower) / PANELS
    halfwidth = width / 2
    total = arb(0)
    for j in range(PANELS):
        mid = lower + (arb(j) + arb(1)/2) * width
        s = mid + arb(0, halfwidth.upper())
        weight = (-V * (-2*s).exp()).exp() - (-V * (2*s).exp()).exp()
        total += phi8(s + delta) * phi8(s - delta) * weight * width
    return total + arb(0, ERROR.upper())


if __name__ == '__main__':
    values = {}
    for name, lower, delta in [('d0', arb(0), arb(0)),
                               ('d1', arb(1), arb(0)),
                               ('c', arb(1)/2, arb(1)/2),
                               ('e', arb(0), arb(1))]:
        values[name] = integral(lower, delta)
        print(name, values[name], flush=True)
    d0, d1, c, e = (values[k] for k in ('d0', 'd1', 'c', 'e'))
    determinant = (d1 + e)*d0 - 2*c*c
    print('even_block_determinant', determinant, flush=True)
    assert d0 > 0 and d1 > 0 and c > 0 and e > 0
    assert determinant < 0, 'INCONCLUSIVE: fixed enclosure did not prove negativity'
    print('FULL PASS: D_(2*pi) is not PSD on {-1,0,1}; no claim about A.', flush=True)

"""Independent quadrature of the exact transfer; diagnostic, not certificate."""
import json
import mpmath as mp

mp.mp.dps = 45


def xlogx(x):
    return x * mp.log(x) if x else mp.mpf(0)


def primitive(x):
    return xlogx(x) - x


def b_matrix(n):
    h = mp.mpf(1) / n
    b = mp.matrix(n)
    for i in range(n):
        for j in range(i):
            d = i - j
            b[i, j] = b[j, i] = -(xlogx(d + 1) + xlogx(d - 1) - 2 * xlogx(d)) / 2
    for i in range(n):
        l, r = i * h, (i + 1) * h
        b[i, i] = -sum(b[i, j] for j in range(n)) - (
            primitive(r) - primitive(l) + primitive(1 - l) - primitive(1 - r)) / (2 * h)
    return b


def kernel(u):
    return 2 * mp.exp(-u / 2) / (-mp.expm1(-2 * u))


def q(u):
    # Avoid subtracting two large reciprocals near the diagonal.
    if abs(u) < mp.mpf('1e-12'):
        return mp.mpf('0.5') - u / 24 - u**2 / 16 + 7 * u**3 / 5760
    return kernel(u) - 1 / u


def check(length, coefficients):
    length = mp.mpf(length)
    f = [mp.mpc(z) for z in coefficients]
    n = len(f)
    norm = sum(abs(z)**2 for z in f)
    knots = [mp.mpf(i) / n for i in range(n + 1)]
    # Re c(v), piecewise affine on these knots, for normalized cell indicators.
    values = [mp.re(sum(f[j + k] * mp.conj(f[j]) for j in range(n - k)))
              for k in range(n + 1)]
    arch_integral = mp.mpf(0)
    remainder = mp.mpf(0)
    for k in range(n):
        l, r = knots[k], knots[k + 1]
        def corr(v):
            return values[k] + (v - l) * n * (values[k + 1] - values[k])
        def increment(v):
            # Stable at v=0, rather than norm-corr(v) cancellation.
            return norm - values[k] - (v - l) * n * (values[k + 1] - values[k])
        arch_integral += mp.quad(lambda v: length * kernel(length * v) * increment(v), [l, r])
        remainder += mp.quad(lambda v: length * q(length * v) * corr(v), [l, r])
    tail = -mp.log(mp.tanh(length / 4)) + mp.pi - 2 * mp.atan(mp.exp(length / 2))
    original = (mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi) + tail) * norm + arch_integral
    b = b_matrix(n)
    bvalue = mp.re(sum(mp.conj(f[i]) * b[i, j] * f[j] for i in range(n) for j in range(n)))
    transported = bvalue - (mp.euler + mp.log(2 * mp.pi * length)) * norm - remainder
    error = abs(original - transported)
    assert error < mp.mpf('1e-35'), error
    return dict(length=str(length), coefficients=[str(z) for z in f],
                original=mp.nstr(original, 18), transported=mp.nstr(transported, 18),
                absolute_error=mp.nstr(error, 6), certification=False)


if __name__ == '__main__':
    print(json.dumps([check(length, coefficients)
                      for length in ['0.5', '1.6094379124341003746', '4', '12']
                      for coefficients in [[1, 1, 1, 1], [1, -1, 1j, 2 - 1j]]], indent=2))

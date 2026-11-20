"""Bound the high-space projector by the polynomial-tail projector.

Only transfer constants are certified; no residual matrix is evaluated.
"""
from math import factorial
from pathlib import Path
import json
import mpmath as mm


def main():
    c = mm.iv
    c.dps = 70
    T = c.mpf(4)/5
    # Taylor remainder through degree 95 bounds the orthogonal tail of h.
    tail_squared = T*c.exp(T)*(T/2)**192/factorial(96)**2
    sinh = (c.exp(T)-c.exp(-T))/2
    records = []
    for parity in ('even','odd'):
        norm_squared = (sinh+(T if parity=='even' else -T))/2
        epsilon = tail_squared/norm_squared
        projector_error = c.sqrt(epsilon)
        assert projector_error.b < c.mpf('1e-187').a
        records.append(dict(parity=parity,
                            epsilon_upper=str(epsilon.b),
                            projector_error_upper=str(projector_error.b)))
    factor = (c.mpf(1783)/500)*(1+c.mpf('1e-20'))
    assert factor.b < 4
    report = dict(status='PASS', scope='projector transfer only; no matrix sign certificate',
                  T='4/5', low_polynomial_degree=95,
                  projector_norm_error_bound='1e-187',
                  criterion_source_gram_cost_bound='4e-187', records=records)
    Path(__file__).with_name('projection_transfer_certificate.json').write_text(
        json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()

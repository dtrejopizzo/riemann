"""Freeze the existing corrector as exact rationals and rebuild primitive U.

The saved floating matrices P,K,D,S are NOT reused as certified matrices.
Only Z, interpreted as the exact coefficient matrix X, is used.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import numpy as np
import mpmath as mm
from polynomial_source import rational
from regional_bases import stable_split

FOLDER = Path(__file__).parent


def freeze(parity,order=160):
    path = FOLDER/f'blocks_{parity}_{order}.npz'
    with np.load(path) as data:
        X = data['Z']
        N = int(data['N'])
        degree = int(data['degree'])
        assert N == 95 and X.shape == (degree-N,N)
        assert np.isfinite(X).all()
        rows = [[str(Fraction(*float(x).as_integer_ratio())) for x in row] for row in X]
    record = dict(parity=parity,T='4/5',N=N,degree=degree,
                  source=path.name,source_sha256=sha256(path.read_bytes()).hexdigest(),
                  interpretation='X is this exact rational matrix; no exact solve is assumed',X=rows)
    target = FOLDER/f'frozen_corrector_{parity}_{order}.json'
    text = json.dumps(record,indent=2)+'\n'
    if target.exists() and target.read_text() != text:
        raise RuntimeError('Frozen corrector already exists with different contents')
    target.write_text(text)
    return record


def legendre_polynomials(ctx,T,degree):
    """Exact rational shifted Legendre coefficients, then interval normalization."""
    # P_n(2x/T-1)=sum_j (-1)^(n+j) binom(n,j)binom(n+j,j)(x/T)^j.
    from math import comb
    return [[ctx.sqrt((2*n+1)/T)*((-1)**(n+j)*comb(n,j)*comb(n+j,j))/T**j
             for j in range(n+1)] for n in range(degree+1)]


def reconstruct(ctx,record,terms=160,physical=True,selected=None):
    T = rational(ctx,record['T'])
    N,degree = record['N'],record['degree']
    alpha,E,W = stable_split(ctx,T,N,record['parity'],high_count=degree-N,
                              interval=True,terms=terms)
    X = [[rational(ctx,x) for x in row] for row in record['X']]
    indices = list(range(N)) if selected is None else list(selected)
    assert all(isinstance(i,int) and 0 <= i < N for i in indices)
    U = []
    for column in indices:
        u = [E[column].get(k,ctx.mpf(0)) for k in range(degree+1)]
        for j,w in enumerate(W):
            for k,value in w.items(): u[k] -= value*X[j][column]
        U.append(u)
    polynomials = None
    if physical:
        basis = legendre_polynomials(ctx,T,degree)
        polynomials = [[sum((u[n]*basis[n][k] for n in range(k,degree+1)),ctx.mpf(0))
                        for k in range(degree+1)] for u in U]
    return dict(alpha=alpha,E=E,W=W,X=X,U_legendre=U,U_physical=polynomials,indices=indices)


def main():
    ctx = mm.iv
    ctx.dps = 400
    records = []
    for parity in ('even','odd'):
        print('Rebuilding',parity,flush=True)
        record = freeze(parity)
        built = reconstruct(ctx,record)
        widths = []
        for u in built['U_legendre']:
            moment = sum((a*b for a,b in zip(built['alpha'],u)),ctx.mpf(0))
            assert moment.a <= 0 and moment.b >= 0
            widths.append(moment.b-moment.a)
        max_moment = max(widths)
        max_coefficient_width = max(v.b-v.a for p in built['U_physical'] for v in p)
        assert max_moment < ctx.mpf('1e-390')
        assert max_coefficient_width < ctx.mpf('1e-290')
        records.append(dict(parity=parity,columns=len(built['U_legendre']),degree=record['degree'],
                            source_sha256=record['source_sha256'],
                            moment_width_bound=str(max_moment),
                            physical_coefficient_width_bound=str(max_coefficient_width)))
    report = dict(status='PASS',scope='exact frozen correctors and interval primitive columns; no Gram or sign certificate',
                  interval_dps=400,moment_series_terms=160,records=records)
    (FOLDER/'frozen_corrector_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()

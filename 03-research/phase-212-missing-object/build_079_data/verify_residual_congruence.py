"""Independent interval SPD verification via an exact dyadic congruence.

The approximate Cholesky only proposes R. The proof is strict diagonal
dominance of the enclosed R M R^t for the intended real symmetric M.
No source integration or LDL recurrence is reused.
"""
import argparse
import json
from hashlib import sha256
from pathlib import Path
import mpmath as mm
from flint import arb,arb_mat,ctx


def verify(path):
    path = Path(path)
    record = json.loads(path.read_text())
    strings = record['criterion']
    n = len(strings)
    assert n and all(len(row)==n for row in strings)
    assert all(strings[i][j] == strings[j][i] for i in range(n) for j in range(n))
    ctx.dps = 500
    M = arb_mat([[arb(s) for s in row] for row in strings])
    assert all(M[i,j].is_finite() for i in range(n) for j in range(n))
    mm.mp.dps = 80
    midpoint = mm.matrix([[mm.mpf(M[i,j].mid().str(100,radius=False))
                           for j in range(n)] for i in range(n)])
    base = dict(matrix_file=path.name,matrix_sha256=sha256(path.read_bytes()).hexdigest(),
                dimension=n,decimal_digits=500,heuristic_digits=80,
                method='exact dyadic congruence and strict diagonal dominance',
                scope='SPD of the supplied real symmetric criterion matrix, not global positivity')
    try:
        L = mm.cholesky(midpoint)
    except (ValueError,ZeroDivisionError) as exc:
        return dict(base,status='INDETERMINATE',reason='heuristic Cholesky failed: '+str(exc))
    R = mm.matrix(n,n)
    for j in range(n):
        for i in range(j,n):
            R[i,j] = ((1 if i==j else 0)-sum(L[i,k]*R[k,j] for k in range(j,i)))/L[i,i]
    encoded = []
    entries = []
    for i in range(n):
        row,balls = [],[]
        for j in range(n):
            assert mm.isfinite(R[i,j])
            sign,mantissa,exponent,bits = R[i,j]._mpf_
            assert bits <= ctx.prec
            exact = ((-1)**sign*mantissa,exponent)
            value = arb(exact)
            assert value.rad() == 0
            row.append(list(exact));balls.append(value)
        encoded.append(row);entries.append(balls)
    exact_R = arb_mat(entries)
    B = exact_R*M*exact_R.transpose()
    margins = [(B[i,i].lower()-sum((B[i,j].abs_upper() for j in range(n) if i!=j),arb(0))).lower()
               for i in range(n)]
    positive = all(m > 0 for m in margins)
    return dict(base,status='PASS_CONGRUENCE' if positive else 'INDETERMINATE',
                preconditioner_dyadic=encoded,margins=[str(m) for m in margins],
                margin_lower_bound=str(min(margins)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('matrix',type=Path)
    args = parser.parse_args()
    report = verify(args.matrix)
    target = args.matrix.with_name(args.matrix.stem+'_congruence.json')
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('preconditioner_dyadic','margins')},indent=2))


if __name__ == '__main__': main()

"""Design108: preserve the common lambda in the complete origin determinant.

No theta is evaluated on import. Both modules107 are hash-checked, unchanged.
The ONLY changed representation is the origin polynomial determinant; all
precision, domain, subdivision and remaining-branch budgets are unchanged.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import sys
from flint import arb, arb_poly, ctx

EXPECTED = {
    'power_mixed_four_origin_branch_107.py':
        '15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553',
    'power_mixed_four_compact_107_verify.py':
        '2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054',
}


def run_correlated_origin(origin):
    ctx.prec, ctx.cap = origin.PREC, origin.CAP
    assert (origin.PREC, origin.CAP, origin.MODES, origin.DEGREE) == (1024,1025,128,512)
    assert (origin.INITIAL_CELLS, origin.MAX_DEPTH, origin.MAX_EVALS) == (16,10,8192)
    a = origin.certified_a()
    K, J, phi = origin.build_origin_polynomials(a)
    variable = arb_poly([0,1])
    qpoly = -phi[0]-2*variable*phi[1]
    qder = [qpoly]
    for _ in range(3):
        qder.append(qder[-1].derivative())
    matrix = [[K[j],J[j],phi[j],qder[j]] for j in range(4)]
    determinant = arb_poly([0])
    for perm in permutations(range(4)):
        inversions = sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = arb_poly([-1 if inversions%2 else 1])
        for row in range(4):
            term *= matrix[row][perm[row]]
        determinant += term
    assert len(determinant) <= 2049
    assert all(c.is_finite() for c in determinant.coeffs())
    assert 96*Q(1,2**400)*(2**62+1)**3 < Q(1,2**200)
    print('108 complete origin determinant polynomial degree',determinant.degree(),flush=True)

    def evaluate(left,right):
        mid,half = (left+right)/2,(right-left)/2
        # Exact polynomial composition, with outward coefficient arithmetic.
        # No coefficient or high degree term is dropped from the finite sum.
        shifted = determinant(arb_poly([origin.ball(mid),arb(1)]))
        assert len(shifted) <= 2049
        coefficients = shifted.coeffs()
        assert coefficients and all(c.is_finite() for c in coefficients)
        h = origin.ball(half)
        radius = origin.ball(Q(1,2**200))
        power = arb(1)
        for coefficient in coefficients[1:]:
            power *= h
            radius += abs(coefficient).upper()*power
        return coefficients[0]+arb(0,radius.upper())

    pending = [(Q(k,64),Q(k+1,64),0)
               for k in reversed(range(origin.INITIAL_CELLS))]
    evaluations = accepted = 0
    covered = Q(0)
    while pending:
        if evaluations >= origin.MAX_EVALS:
            return {'status':'INCONCLUSIVE','branch':'origin108','a':a,
                    'reason':'fixed evaluation budget','evaluations':evaluations,
                    'accepted':accepted,'pending':len(pending),'covered':str(covered)}
        left,right,depth = pending.pop()
        value = evaluate(left,right)
        evaluations += 1
        if value > 0:
            accepted += 1
            covered += right-left
        elif value < 0:
            print('NEGATIVE108 origin interval',left,right,value,flush=True)
            return {'status':'NEGATIVE','branch':'origin108','a':a,
                    'interval':(str(left),str(right)),'evaluations':evaluations}
        elif depth >= origin.MAX_DEPTH:
            print('INCONCLUSIVE108 origin depth',left,right,value,flush=True)
            return {'status':'INCONCLUSIVE','branch':'origin108','a':a,
                    'reason':'fixed depth','interval':(str(left),str(right)),
                    'evaluations':evaluations,'accepted':accepted,'covered':str(covered)}
        else:
            mid = (left+right)/2
            pending.append((mid,right,depth+1))
            pending.append((left,mid,depth+1))
        if evaluations % 64 == 0:
            print('108 origin progress',evaluations,'accepted',accepted,
                  'pending',len(pending),'covered',str(covered),flush=True)
    assert covered == Q(1,4)
    result = {'status':'PASS','branch':'origin108','a':a,
              'evaluations':evaluations,'accepted':accepted,'covered':str(covered)}
    print('PASS108 origin COMPLETE lambda[0,1/4]',evaluations,
          'evaluations',accepted,'accepted leaves',flush=True)
    return result


def main():
    here = Path(__file__).resolve().parent
    print('DRIVER108 SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
    for name,expected in EXPECTED.items():
        actual = sha256((here/name).read_bytes()).hexdigest()
        assert actual == expected,(name,actual,expected)
        print('UNCHANGED107 SHA256',name,actual,flush=True)
    import power_mixed_four_origin_branch_107 as origin
    import power_mixed_four_compact_107_verify as remaining
    result = run_correlated_origin(origin)
    if result['status'] != 'PASS':
        print('NO FULLPASS108: ORIGIN',result,flush=True)
        return 1 if result['status']=='NEGATIVE' else 2
    rest = remaining.certify_rest(result['a'])
    if rest['status'] != 'PASS':
        print('NO FULLPASS108: REST',rest,flush=True)
        return 1 if rest['status']=='NEGATIVE' else 2
    print('FULLPASS108: origin and unchanged107 rest',result,rest,flush=True)
    return 0


if __name__=='__main__':
    sys.exit(main())

"""Fixed origin branch of design107. Importing this module evaluates no theta."""
from fractions import Fraction as Q
from itertools import permutations
from hashlib import sha256
from pathlib import Path
from flint import arb, arb_series, arb_poly, ctx

PREC, CAP, MODES, DEGREE = 1024, 1025, 128, 512
INITIAL_CELLS, MAX_DEPTH, MAX_EVALS = 16, 10, 8192


def ball(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator


def symmetric_error(q):
    return arb(0, ball(q).upper())


def certified_a():
    # The same complete regularized E and fixed origin jet used in099.
    u = arb_series([arb(0), arb(1)], prec=3)
    A = u + arb(1) / 2
    regular = 1 + (A - 1) * A.zeta(deflate=True)
    E = A * regular * (A / 2).gamma() * (-A * arb.pi().log() / 2).exp()
    assert E.prec >= 3 and all(E[k].is_finite() for k in range(3))
    assert E[0] > 0 and E[1].contains(arb(0))
    a = 2 * E[2] / E[0]
    old_center = Q('0.0462099862308379415778676')
    old_radius = Q(374, 10**28)
    old = ball(old_center-old_radius).union(ball(old_center+old_radius))
    assert old.contains(a) and a > ball(Q(1, 25)) and a < 1
    print('PASS107 fixed complete a origin jet', a, flush=True)
    return a


def derivative_polynomials(coefficients, order):
    result = [arb_poly(coefficients)]
    for _ in range(order):
        result.append(result[-1].derivative())
    return result


def build_origin_polynomials(a):
    assert 1548 * 24 * Q(83, 3)**5 < 2**40
    assert 129**4 < 2**29 and Q(3*129**2, 80) > 624
    assert 2 * 1548 * 129**4 < 2**41
    assert 513**4 < 2**37
    t = arb_series([arb(0), arb(1)], prec=CAP)
    pi = arb.pi()
    y = pi * (2*t).exp()
    total = arb_series([arb(0)], prec=CAP)
    for m in range(1, MODES+1):
        total += m*m * (2*m*m*y-3) * (-m*m*y).exp()
        if m % 32 == 0:
            print('107 origin fixed theta modes', m, 'of', MODES, flush=True)
    phi_t = pi * (5*t/2).exp() * total
    assert phi_t.prec >= CAP
    # Only even coefficients are extracted; the finite theta sum need not
    # itself be even. Cauchy encloses the omitted modes BEFORE recurrences.
    phi = [phi_t[2*k] + symmetric_error(Q(2)**(k-583))
           for k in range(DEGREE+1)]
    assert all(c.is_finite() for c in phi)
    I1 = ball(Q('0.02152870762556652324898962')) + symmetric_error(Q(396,10**29))
    I3 = ball(Q('0.00191588830192231322996545')) + symmetric_error(Q(490,10**29))
    K0 = a*I1-I3/2
    assert 0 < I1 < 1 and 0 < K0 < 1
    J = [I1]
    K = [K0]
    for k in range(1, DEGREE+1):
        J.append(-phi[k-1]/(2*k))
        K.append((a*phi[k-1]-J[k-1])/(2*k*(2*k-1)))
    return (derivative_polynomials(K,3),
            derivative_polynomials(J,3),
            derivative_polynomials(phi,4))


def determinant4(matrix):
    result = arb(0)
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
        term = arb(-1 if inversions % 2 else 1)
        for row in range(4):
            term *= matrix[row][perm[row]]
        result += term
    return result


def run_origin():
    ctx.prec, ctx.cap = PREC, CAP
    a = certified_a()
    K, J, phi = build_origin_polynomials(a)
    entry_tail = symmetric_error(Q(1,2**400))

    def evaluate(lo, hi):
        mid, half = (lo+hi)/2, (hi-lo)/2
        lam = ball(mid) + symmetric_error(half)
        pd = [poly(lam) for poly in phi]
        matrix = []
        for j in range(4):
            qj = -(2*j+1)*pd[j]-2*lam*pd[j+1]
            matrix.append([K[j](lam)+entry_tail, J[j](lam)+entry_tail,
                           pd[j]+entry_tail, qj+entry_tail])
        assert all(value.is_finite() for row in matrix for value in row)
        return determinant4(matrix)

    pending = [(Q(k,64), Q(k+1,64), 0)
               for k in reversed(range(INITIAL_CELLS))]
    evaluations = accepted = 0
    covered = Q(0)
    while pending:
        if evaluations >= MAX_EVALS:
            return {'status':'INCONCLUSIVE', 'branch':'origin', 'a':a,
                    'reason':'fixed evaluation budget', 'evaluations':evaluations,
                    'accepted':accepted, 'pending':len(pending), 'covered':str(covered)}
        lo, hi, depth = pending.pop()
        value = evaluate(lo, hi)
        evaluations += 1
        if value > 0:
            accepted += 1
            covered += hi-lo
        elif value < 0:
            print('NEGATIVE107 origin interval',lo,hi,value,flush=True)
            return {'status':'NEGATIVE', 'branch':'origin', 'a':a,
                    'interval':(str(lo),str(hi)), 'evaluations':evaluations}
        elif depth >= MAX_DEPTH:
            print('INCONCLUSIVE107 origin depth',lo,hi,value,flush=True)
            return {'status':'INCONCLUSIVE', 'branch':'origin', 'a':a,
                    'reason':'fixed depth', 'interval':(str(lo),str(hi)),
                    'evaluations':evaluations, 'accepted':accepted}
        else:
            mid = (lo+hi)/2
            pending.append((mid,hi,depth+1))
            pending.append((lo,mid,depth+1))
        if evaluations % 128 == 0:
            print('107 origin progress',evaluations,'accepted',accepted,
                  'pending',len(pending),'covered',str(covered),flush=True)
    assert covered == Q(1,4)
    print('PASS107 origin COMPLETE lambda[0,1/4]',evaluations,'evaluations',
          accepted,'accepted leaves',flush=True)
    print('ORIGIN MODULE SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
    return {'status':'PASS', 'branch':'origin', 'a':a,
            'evaluations':evaluations, 'accepted':accepted, 'covered':str(covered)}

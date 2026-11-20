"""Native validated Gram and polynomial moments using Hankel convolutions."""
from flint import arb,arb_mat,arb_poly
from arb_moment_convolution import functional


def pairings(local,tests,moments):
    """Return polynomial-test pairings and source Gram on (0,1), no remainders.

    The caller supplies the physical Jacobian and the existing error budgets.
    """
    assert local and tests
    coefficients = [[p.coeffs() for p in column] for column in local]
    test_coefficients = [p.coeffs() for p in tests]
    test_width = max(1,max(map(len,test_coefficients)))
    sizes = [max(len(column[s]) for column in coefficients) for s in range(3)]
    sizes[0] = max(sizes[0],test_width)
    rows = [(s,k) for s in range(3) for k in range(sizes[s])]
    C = arb_mat([[column[s][k] if k<len(column[s]) else arb(0)
                  for column in coefficients] for s,k in rows])
    actions = []
    for s,(left,right) in enumerate(((0,0),(1,0),(0,1))):
        if sizes[s]:
            actions.append([functional(column,moments,sizes[s]-1,left,right) for column in local])
        else:
            actions.append([[] for _ in local])
    Y_rows = [[actions[s][j][k] for j in range(len(local))] for s,k in rows]
    Y = arb_mat(Y_rows)
    G = C.transpose()*Y
    P = arb_mat([[p[k] if k<len(p) else arb(0) for k in range(test_width)]
                 for p in test_coefficients])
    B = P*arb_mat(Y_rows[:test_width])
    return B,G


def check():
    from flint import ctx
    from arb_source_integral import Moments
    ctx.dps = 80
    one,zero = arb_poly([1]),arb_poly()
    local = [[one,zero,zero],[zero,one,zero],[zero,zero,one]]
    B,G = pairings(local,[one,arb_poly([0,1])],Moments())
    crossed = 2-arb.pi()**2/6
    expectedG = [[arb(1),arb(-1),arb(-1)],[-arb(1),arb(2),crossed],[-arb(1),crossed,arb(2)]]
    expectedB = [[arb(1),-arb(1),-arb(1)],[arb(1)/2,-arb(1)/4,-arb(3)/4]]
    for result,expected in ((G,expectedG),(B,expectedB)):
        for i,row in enumerate(expected):
            for j,target in enumerate(row):
                assert result[i,j].overlaps(target)
                assert result[i,j].rad() < arb('1e-70')
    print('PASS: native 3x3 logarithmic Gram and 2x3 polynomial pairings')


if __name__ == '__main__': check()

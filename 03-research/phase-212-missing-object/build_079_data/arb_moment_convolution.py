"""Validated Hankel moment action by reversed-polynomial convolution."""
from flint import arb,arb_poly


def functional(local,moments,maximum,log_left=0,log_right=0):
    result = [arb(0) for _ in range(maximum+1)]
    for polynomial,(left,right) in zip(local,((0,0),(1,0),(0,1))):
        coefficients = polynomial.coeffs()
        if not coefficients: continue
        degree = len(coefficients)-1
        reverse = arb_poly(list(reversed(coefficients)))
        table = arb_poly([moments.get(n,left+log_left,right+log_right)
                          for n in range(degree+maximum+1)])
        product = reverse*table
        for k in range(maximum+1): result[k] += product[degree+k]
    return result


def check():
    from flint import ctx
    from arb_source_integral import Moments
    ctx.dps = 80
    local = [arb_poly([1,-2,3]),arb_poly([0,1]),arb_poly([-1,2])]
    values = functional(local,Moments(),16)
    for k,value in enumerate(values):
        h = sum((arb(1)/j for j in range(1,k+2)),arb(0))
        hnext = h+arb(1)/(k+2)
        exact = arb(1)/(k+1)-arb(2)/(k+2)+arb(3)/(k+3)-arb(1)/(k+2)**2+h/(k+1)-2*hnext/(k+2)
        assert value.overlaps(exact)
        assert value.rad() < arb('1e-70')
    assert all(x == 0 for x in functional([arb_poly()]*3,Moments(),3))
    print('PASS: 17 analytic polynomial/log moments and zero components')


if __name__ == '__main__': check()

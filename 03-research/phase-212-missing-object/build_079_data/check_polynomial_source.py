"""Independent numerical quadrature check of the algebraic A_K source.

This checks implementation; quadrature agreement is not a sign certificate.
"""
from pathlib import Path
import json
import mpmath as mm
from certify_kernel_polynomial import coefficients
from polynomial_source import rational, evaluate, pieces, source_value


def direct(ctx,f,kernel,T,x,sigma):
    F = lambda y: evaluate(f,y)
    r = lambda u: evaluate(kernel,u)
    tail = lambda u: -sum(c*u**(j+1)/(j+1) for j,c in enumerate(kernel))
    z = x/T
    value = (-ctx.euler-ctx.log(2*ctx.pi*T)-ctx.log(1-z*z)/2
             +tail(T-x)+tail(T+x))*F(x)
    value += ctx.quad(lambda y: (F(x)-F(y))/(2*abs(x-y)) if y!=x else 0,[0,x,T])
    value += ctx.quad(lambda y: r(abs(x-y))*(F(x)-F(y)),[0,x,T])
    value += ctx.quad(lambda y: (ctx.mpf(1)/(2*(x+y))+r(x+y))
                     *(F(x)-sigma*F(y)),[0,T])
    def zero(y): return F(y) if 0 < y < T else 0
    for n,p in ((2,2),(3,3),(4,2)):
        length = ctx.log(n)
        value -= ctx.log(p)/ctx.sqrt(n)*(zero(x+length)+zero(x-length)+sigma*zero(length-x))
    return value


def main():
    mm.mp.dps = 100
    mm.iv.dps = 60
    coeff = coefficients(8)
    f_exact = ['2/3','-7/5','11/4','-2','1/7']
    fp = [rational(mm.mp,x) for x in f_exact]
    fi = [rational(mm.iv,x) for x in f_exact]
    kp = [rational(mm.mp,x) for x in coeff]
    ki = [rational(mm.iv,x) for x in coeff]
    T = mm.mp.mpf(4)/5
    records = []
    for sigma in (1,-1):
        pp = pieces(mm.mp,fp,kp,sigma)
        pi = pieces(mm.iv,fi,ki,sigma)
        errors = []
        for (a,b,source),(_,_,enclosure) in zip(pp,pi):
            x = (a+b)/2
            expected = direct(mm.mp,fp,kp,T,x,sigma)
            assembled = source_value(mm.mp,source,x,T)
            error = abs(expected-assembled)
            assert error < mm.mp.mpf('1e-85')
            # High precision numerical reference is enclosed in the interval
            # evaluation; this is a diagnostic, not a certified quadrature.
            ix = mm.iv.mpf(mm.mp.nstr(x,100))
            bound = source_value(mm.iv,enclosure,ix,mm.iv.mpf(4)/5)
            reference = mm.iv.mpf(mm.mp.nstr(expected,100))
            assert bound.a <= reference.a and bound.b >= reference.b
            errors.append(error)
        records.append(dict(sigma=sigma,pieces=len(pp),max_absolute_discrepancy=str(max(errors))))
    report = dict(status='PASS_IMPLEMENTATION_CHECK',kernel_degree=8,input_degree=4,
                  scope='numerical quadrature cross-check and interval evaluation; not a sign certificate',
                  records=records)
    Path(__file__).with_name('polynomial_source_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()

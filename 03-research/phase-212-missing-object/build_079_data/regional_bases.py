"""Stable moment-exact low/high bases for the regional residual calculation.

Intervals enclose exact coefficients defined by positive moment series.
No subtraction of nearly equal functions, quadrature, or small-moment division.
"""
from math import factorial
import json
from pathlib import Path
import mpmath as mm

def moment_coeff(ctx,T,n,parity,terms=32,interval=True):
    assert parity in ('even','odd') and n>=0 and terms>0
    a = T/2
    r0 = (n+(parity=='odd'))%2
    def term(r):
        return a**r*ctx.mpf(factorial(n+r))/(factorial(r)*factorial(2*n+r+1))
    value = sum(term(r0+2*k) for k in range(terms))
    r = r0+2*terms
    tail = term(r)/(1-a*a/((r+1)*(r+2)))
    assert (a*a/((r+1)*(r+2))).b<1 if interval else a*a/((r+1)*(r+2))<1
    enclosed = value+(ctx.mpf([0,1])*tail if interval else tail/2)
    return ctx.sqrt(T*(2*n+1))*a**n*enclosed

def stable_split(ctx,T,N,parity,high_count=4,interval=True,terms=32):
    alpha = [moment_coeff(ctx,T,n,parity,terms=terms,interval=interval) for n in range(N+high_count+1)]
    low_norm = sum(x*x for x in alpha[:N+1])
    low = [{0:-alpha[n]/alpha[0], n:ctx.mpf(1)} for n in range(1,N+1)]
    high = []
    for k in range(N+1,N+high_count+1):
        v = {i:-alpha[k]*alpha[i]/low_norm for i in range(N+1)}
        v[k] = ctx.mpf(1)
        high.append(v)
    return alpha,low,high

def certify():
    ctx = mm.iv
    ctx.dps = 70
    T = ctx.mpf(4)/5
    N = 95
    error = T*ctx.exp(T)*(T/2)**(2*N+2)/factorial(N+1)**2
    H = sum(ctx.mpf(1)/k for k in range(1,N+2))
    C0 = -ctx.euler-ctx.pi/2-3*ctx.log(2)-ctx.log(ctx.pi)
    u = ctx.exp(-T/2)
    I = ctx.log((1+u)/(1-u))/2+ctx.atan2(u,ctx.mpf(1))
    inner = ctx.log(2)/ctx.sqrt(2)
    weights = inner+ctx.log(3)/ctx.sqrt(3)+ctx.log(2)/2
    constant = C0+2*I-2*inner-weights
    records = []
    for parity in ('even','odd'):
        sinh = (ctx.exp(T)-ctx.exp(-T))/2
        hnorm = (sinh+T)/2 if parity=='even' else (sinh-T)/2
        epsilon = error/hnorm
        assert epsilon.b<ctx.mpf('1e-374').a
        alpha,low,high = stable_split(ctx,T,N,parity)
        condition = hnorm/alpha[0]**2
        assert condition.b<(ctx.mpf(27)/20).a
        high_excess = epsilon/(1-epsilon)
        assert high_excess.b<ctx.mpf('1e-370').a
        gamma = H*(1-epsilon)+constant
        assert gamma.a>(ctx.mpf(1)/8).b
        def encloses_zero(x): return x.a<=0 and x.b>=0
        for v in low+high:
            assert encloses_zero(sum(c*alpha[k] for k,c in v.items()))
        for v in low:
            for w in high:
                assert encloses_zero(sum(c*w.get(k,ctx.mpf(0)) for k,c in v.items()))
        records.append(dict(parity=parity,tail_ratio_upper=str(epsilon.b),
                            low_gram_condition_upper=str(condition.b),
                            high_gram_excess_upper=str(high_excess.b),
                            gamma=str(gamma),low_columns=len(low),checked_high_columns=len(high)))
    report = dict(status='PASS',T='4/5',degree=N,low_dimension=95,
                  moment_series_terms=32,interval_dps=ctx.dps,records=records)
    (Path(__file__).parent/'regional_bases_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    certify()

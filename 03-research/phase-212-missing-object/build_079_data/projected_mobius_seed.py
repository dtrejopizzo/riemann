"""First projected Mobius seed, numerical coefficients at T=4/5.

This does not compute H w or a residual gain. Formulas are exact; mpmath
coefficient values and checks are not interval certificates.
"""
import json
from pathlib import Path
import mpmath as mp
from regional_bases import moment_coeff


def build(parity,N=95):
    T=mp.mpf(4)/5
    sigma=1 if parity=='even' else -1
    steps=[]
    for n,mu in ((1,1),(2,-1),(3,-1),(4,0)):
        if not mu: continue
        length=mp.log(n)
        coefficient=mu/(2*mp.sqrt(T*n))
        a=max(mp.mpf(0),length-T)
        if a<T: steps.append((a,T,coefficient))
        b=min(T,T-length)
        if b>0: steps.append((mp.mpf(0),b,sigma*coefficient))
    def integral_p(n,a,b):
        if n==0: return (b-a)/mp.sqrt(T)
        def primitive(x):
            z=2*x/T-1
            return mp.sqrt(T)/(2*mp.sqrt(2*n+1))*(mp.legendre(n+1,z)-mp.legendre(n-1,z))
        return primitive(b)-primitive(a)
    v=[sum(c*integral_p(n,a,b) for a,b,c in steps) for n in range(N+1)]
    alpha=[moment_coeff(mp.mp,T,n,parity,terms=160,interval=False) for n in range(N+1)]
    h_integral=(lambda a,b:2*(mp.sinh(b/2)-mp.sinh(a/2))) if sigma==1 else (lambda a,b:2*(mp.cosh(b/2)-mp.cosh(a/2)))
    hg=sum(c*h_integral(a,b) for a,b,c in steps)
    hnorm=(mp.sinh(T)+sigma*T)/2
    low_norm=sum(a*a for a in alpha)
    t=sum(a*b for a,b in zip(alpha,v))/low_norm
    coefficients=[-b+t*a for a,b in zip(alpha,v)]
    h_coefficient=-hg/hnorm
    moment=hg+sum(a*c for a,c in zip(alpha,coefficients))+h_coefficient*hnorm
    projected_moments=[v[n]+coefficients[n]+h_coefficient*alpha[n] for n in range(N+1)]
    orthogonality=[projected_moments[n]-alpha[n]/alpha[0]*projected_moments[0] for n in range(1,N+1)]
    error=max([abs(moment)]+[abs(x) for x in orthogonality])
    assert error<mp.mpf('1e-80')
    # Independent quadrature of low Legendre moments of the unprojected steps.
    quadrature_error=max(abs(v[n]-sum(c*mp.quad(lambda x:mp.sqrt((2*n+1)/T)*mp.legendre(n,2*x/T-1),[a,b]) for a,b,c in steps)) for n in range(4))
    assert quadrature_error<mp.mpf('1e-80')
    return dict(parity=parity,T='4/5',N=N,steps=[[str(x) for x in row] for row in steps],
                legendre_coefficients=[str(x) for x in coefficients],h_coefficient=str(h_coefficient),
                moment_and_low_orthogonality_error=str(error),low_moment_quadrature_error=str(quadrature_error))


if __name__=='__main__':
    mp.mp.dps=100
    report=dict(status='PASS_NUMERICAL_PROJECTION_CHECK',decimal_digits=100,
                scope='first projected seed coefficients only; no source Gram or gain certificate',
                sectors=[build(p) for p in ('even','odd')])
    Path(__file__).with_name('projected_mobius_seed.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({**report,'sectors':[{k:v for k,v in s.items() if k not in ('steps','legendre_coefficients')} for s in report['sectors']]},indent=2))

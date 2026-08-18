#!/usr/bin/env python3
"""Checks the exact algebra behind D.171."""
import mpmath as mp
mp.mp.dps=70

def H(s,x):
    return mp.e**(-x/2)*mp.lerchphi(mp.e**(-2*x),s,mp.mpf('0.25'))/2**s

for x in (mp.mpf('1e-8'),mp.mpf('.03'),mp.mpf('.7')):
    y=mp.e**(-x/2)
    assert abs(H(1,x)-(mp.atanh(y)+mp.atan(y)))<mp.mpf('1e-60')

def q(z):
    return z*mp.e**(z/2)/(2*mp.sinh(z)) if z else mp.mpf('.5')

def r1(x):
    if not x:
        return mp.log(2)+mp.pi/4
    y=mp.e**(-x/2)
    return mp.log(x*(1+y)/(1-y))/2+mp.atan(y)

assert abs(q(mp.mpf('1e-20'))-mp.mpf('.5'))<mp.mpf('1e-20')
assert abs(r1(mp.mpf('1e-20'))-(mp.log(2)+mp.pi/4))<mp.mpf('1e-18')

def dd_horner(c,t,s):
    p=c[-1];d=mp.mpf(0)
    for ck in reversed(c[:-1]):
        d=p+s*d;p=ck+t*p
    return d

c=[mp.mpf(3),mp.mpf(-2),mp.mpf(5),mp.mpf(7)]
for t,s in ((mp.mpf('.2'),mp.mpf('-.3')),(mp.mpf('.7'),mp.mpf('.1'))):
    f=lambda x:sum(c[k]*x**k for k in range(len(c)))
    assert abs(dd_horner(c,t,s)-(f(t)-f(s))/(t-s))<mp.mpf('1e-65')

# The coefficient of x^r log(x) propagated by H_{r+1}'=-H_r.
for r in range(8):
    c=(-1)**(r+1)/(2*mp.factorial(r))
    if r:
        previous=(-1)**r/(2*mp.factorial(r-1))
        # derivative coefficient r*c equals -previous.
        assert abs(r*c+previous)<mp.mpf('1e-65')

# Verify the beta-derivative log-square formula independently.
T=mp.log(5)/2;L=mp.log(T*T)
for k in range(6):
    a=mp.mpf(k)+mp.mpf('.5')
    formula=(L*L+2*L*(mp.digamma(1)-mp.digamma(a+1))
             +(mp.digamma(1)-mp.digamma(a+1))**2
             +mp.polygamma(1,1)-mp.polygamma(1,a+1))/a
    direct=mp.quad(lambda u:u**(2*k)*mp.log(T*T*(1-u*u))**2,[-1,0,1])
    assert abs(formula-direct)<mp.mpf('1e-55')

    aa=mp.mpf(k+1)
    harmonic=mp.fsum(1/mp.mpf(j) for j in range(1,k+2))
    harmonic2=mp.fsum(1/mp.mpf(j)**2 for j in range(1,k+2))
    mixed=harmonic/aa**2-(mp.zeta(2)-harmonic2)/aa
    direct_mixed=mp.quad(lambda x:x**k*mp.log(x)*mp.log(1-x),[0,1])
    assert abs(mixed-direct_mixed)<mp.mpf('1e-55')

print('D171 endpoint-log extraction identities: PASS')

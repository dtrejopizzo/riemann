#!/usr/bin/env python3
"""Numerical normalization regression, not certified interval quadrature."""
import mpmath as mp

mp.mp.dps = 50
fourier_test = lambda x: (1/(2*mp.pi)-x*x)*mp.exp(-mp.pi*x*x)
pairing = 2*mp.quad(lambda x:mp.log(x)*fourier_test(x),[0,1,mp.inf])
assert abs(pairing+1/(2*mp.pi)) < mp.mpf('1e-45')
assert abs(pairing+1/mp.pi) > mp.mpf('0.1')
print('PASS Gaussian test distinguishes the half coefficient from the unhalved coefficient')

kernel = lambda t:mp.exp(-t/2)/(-mp.expm1(-2*t))
for tau in (0,1,4):
    integrand = lambda t:kernel(t)*(mp.cos(tau*t)-mp.exp(-t/2))
    integral = mp.fsum(mp.quad(integrand,[j,j+1]) for j in range(128))
    actual = mp.euler+mp.log(4*mp.pi)+2*integral
    expected = mp.log(mp.pi)-mp.re(mp.digamma(mp.mpf('0.25')+mp.j*tau/2))
    # Analytic tail is < 10 exp(-64); quadrature itself is not interval-certified.
    assert abs(actual-expected) < mp.mpf('1e-24'), (tau,actual-expected)
    print(f'PASS Gamma multiplier at tau={tau}; discrepancy {mp.nstr(actual-expected,5)}')
print('SCOPE: floating-point regression; analytic proof is P123.035, no RH or carrier comparison')

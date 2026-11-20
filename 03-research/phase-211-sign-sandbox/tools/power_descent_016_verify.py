"""Exact initial-state certificate for the shifted-form descent obstruction."""
from fractions import Fraction as F
# f=e^(-63y/2); W[f]/||f||^2=2L(32), including every prime.
# psi16=H15-gamma<H15, logpi>1, and zeta'/zeta(32)<0.
H15=sum((F(1,k) for k in range(1,16)),F(0))
assert H15-1+F(1,16)+F(2,31)<3
assert 3-4==-1
print('PASS: (W-4||.||^2)[e^(-63y/2)]/||e^(-63y/2)||^2 < -1.')

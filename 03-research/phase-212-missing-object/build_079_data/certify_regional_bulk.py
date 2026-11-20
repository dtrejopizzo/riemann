"""Certify the constant in the analytic regional high-Legendre bound.

This checks constants only. The infinite-dimensional inequality and its
domain justification are proved in BUILD083, equations (38)-(42).
"""
import json
from pathlib import Path
import mpmath as mm

c = mm.iv
c.dps = 70
T = c.mpf(4)/5
assert c.log(2).b<T.a and T.b<c.log(3).a
assert c.log(4).b<(2*T).a and (2*T).b<c.log(5).a
C0 = -c.euler-c.pi/2-3*c.log(2)-c.log(c.pi)
u = c.exp(-T/2)
I = c.log((1+u)/(1-u))/2+c.atan2(u,c.mpf(1))
inner = c.log(2)/c.sqrt(2)
all_weights = inner+c.log(3)/c.sqrt(3)+c.log(2)/2
constant = C0+2*I-2*inner-all_weights
N = 96
harmonic = sum(c.mpf(1)/k for k in range(1,N+1))
gamma = harmonic+constant
assert gamma.a>(c.mpf(1)/8).b
report = dict(status='PASS',T='4/5',N=N,kappa='1',lower_bound='1/8',
              constant=str(constant),harmonic=str(harmonic),gamma=str(gamma),
              scope='regional q on the complement of Legendre degrees 0..95')
(Path(__file__).parent/'regional_bulk_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

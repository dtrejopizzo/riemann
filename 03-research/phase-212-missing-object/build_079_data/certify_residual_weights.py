"""Interval constants for the mode-sensitive residual inequality only."""
import json
from pathlib import Path
import mpmath as mm

c=mm.iv
c.dps=70
T=c.mpf(4)/5
eta=c.mpf('1e-370')  # Certified upper bound from regional_bases_certificate.
u=c.exp(-T/2)
I=c.log((1+u)/(1-u))/2+c.atan2(u,c.mpf(1))
C0=-c.euler-c.pi/2-3*c.log(2)-c.log(c.pi)
inside=c.log(2)/c.sqrt(2)
weights=inside+c.log(3)/c.sqrt(3)+c.log(2)/2
constant=C0+2*I-2*inside-weights
def d(n):
    return sum(c.mpf(1)/k for k in range(1,n+1))+constant-abs(constant)*eta
assert d(96).a>(c.mpf(1)/8).b
records=[]
for M,num,den in [(111,1783,500),(159,1573,1000)]:
    coefficient=(1+eta)/d(M+1)
    rational=c.mpf(num)/den
    assert coefficient.b<rational.a
    records.append(dict(M=M,high_modes=M-95,rho_rational=f'{num}/{den}',
                        coefficient=str(coefficient),solve_defect_coefficient='8'))
report=dict(status='PASS',scope='residual inequality constants; not a sign certificate',
            eta_upper='1e-370',records=records)
(Path(__file__).parent/'residual_weights_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

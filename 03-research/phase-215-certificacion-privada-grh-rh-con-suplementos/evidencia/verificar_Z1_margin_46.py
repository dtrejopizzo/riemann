"""Independent ball checks for Z1 and constants in the upper-margin proof."""
import json
from pathlib import Path
from flint import arb,acb,ctx
ctx.prec=256
rho=acb.zeta_zero(1)
N=arb(21).zeta_nzeros()
assert N==1 and rho.real==arb('0.5')
assert rho.imag>arb('14.13') and rho.imag<arb('14.14')
e=arb(1).exp();pi=arb.pi();g=arb('14.13')
def eps(k,T):
    Y=T*g/arb(2).sqrt()
    return arb(k)**(2*k)*Y**(1-2*k)/(pi*(2*k-1))
C=e*g/(21*arb(2).sqrt())
assert C>arb(9)/8
assert eps(8,arb(1))<arb('.01567')
assert eps(9,8*e/21)<arb('.016')
Yexact=(8*e/21)*rho.imag/arb(2).sqrt()
assert arb(9)**18*Yexact**(-17)/(17*pi)<arb('.01567')
assert 42/e>arb('15.4494') and 2*e/21<arb('.259')
coeff=arb(8)/(7*2*pi)*(arb(21).log()+arb(1)/7)
assert coeff<arb('.5798')
assert (1+arb(1)/(4*21**2))**2<arb('1.0012')
ratio=10*e*(arb(21)/arb('3e12'))**arb('6.449')
assert ratio<arb('1e-70')
constant=2*arb('1.0012')*arb('.5798')*21**9*arb('.259').exp()/((g**4/64)*arb('.484'))*(1+arb('1e-70'))
assert constant<arb('3.97e9')
result={'N21':str(N),'rho1':rho.str(70),'epsilon8_upper':eps(8,arb(1)).str(30),'epsilon9_left_upper':eps(9,8*e/21).str(30),'margin_constant':constant.str(30),'status':'all rigorous predicates passed'}
print(json.dumps(result,indent=2))
Path(__file__).with_name('Z1_margin_46_arb.json').write_text(json.dumps(result,indent=2))

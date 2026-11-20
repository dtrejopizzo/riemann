import sys, math; from falsifier_cert import *
from flint import arb
case=sys.argv[1]; N=int(sys.argv[2])
v=lambda p,n: 2*arb(p).log()/arb(n).sqrt()
if case=='1.1L': Tf=1.0; Tex=arb(1)
else: Tf=0.5*math.log(5)+1e-4; Tex=arb(5).log()/2+arb('0.0001')
ex={'a3':[(arb(3).log(),v(3,3)),(arb(5).log(),v(5,5))],
    'beur':[(arb(2).log(),v(2,2)),(arb('3.2').log(),v(3,3)),(arb(4).log(),v(2,4)),(arb(5).log(),v(5,5))],
    '1.1L':[(arb(n).log(),arb('1.1')*v(p,n)) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]]}[case]
lam,a,_=num_min(Tf,combs(Tf)[case],N); print('galerkin',lam); print('vec',a/np.max(np.abs(a)))
certify(Tex,ex,a,case)

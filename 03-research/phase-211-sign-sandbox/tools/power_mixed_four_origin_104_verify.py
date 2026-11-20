"""One fixed mixed-four origin gate, round104.

Reuse the unchanged rational origin certificate087 and the already printed
complete moment enclosures103. No new theta parameters or moment quadrature.
Either sign of the fixed determinant is accepted.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from itertools import permutations
import runpy

old=Path(__file__).resolve().parent/'power_theta_density_origin_087_verify.py'
assert sha256(old.read_bytes()).hexdigest()==(
    'f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7')
data=runpy.run_path(str(old))
I,S=data['I'],data['S']
assert S==10**70

# Certified decimal OUTWARD enclosures from the completed run103.
# Each center and radius is an exact rational, not a binary floating point.
inputs=[('0.12428019454707852747819343',F(689,10**29)),
        ('0.02152870762556652324898962',F(396,10**29)),
        ('0.00574298607878635938381247',F(284,10**29)),
        ('0.00191588830192231322996545',F(490,10**29))]
moments=[I(F(center)-radius,F(center)+radius) for center,radius in inputs]
I0,I1,I2,I3=moments
Phi0=data['Phi'][0]
z1,z2,z3=data['a'][1:4]
assert Phi0.l>0 and all(z.l>0 for z in moments)
a=I2/I0
assert 25*a.l>S and a.h<S
tau=I1/Phi0
kappa=(a*I1-I3/2)/Phi0
assert kappa.l>0

matrix=[
    [kappa,tau,I(1),I(-1)],
    [(a-tau)/2,I(F(-1,2)),z1,-3*z1],
    [(a*z1+F(1,2))/6,-z1/2,2*z2,-10*z2],
    [(a*z2+z1/4)/5,-z2,6*z3,-42*z3],
]
D=I(0)
for pp in permutations(range(4)):
    sign=(-1)**sum(pp[i]>pp[j] for i in range(4) for j in range(i+1,4))
    term=I(sign)
    for i in range(4):term=term*matrix[i][pp[i]]
    D=D+term
assert D.l>0 or D.h<0,('INCONCLUSIVE fixed mixed origin gate',F(D.l,S),F(D.h,S))
print('PASS104: mixed-four origin sign',
      'POSITIVE' if D.l>0 else 'NEGATIVE',flush=True)
print('Dmix lower exact:',F(D.l,S),flush=True)
print('Dmix upper exact:',F(D.h,S),flush=True)
# Persist recoverable jet enclosures in the output, unlike the old run087.
for name,z in [('Phi0',Phi0),('z1',z1),('z2',z2),('z3',z3)]:
    print('RECOVERED087',name,'lower',F(z.l,S),'upper',F(z.h,S),flush=True)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)

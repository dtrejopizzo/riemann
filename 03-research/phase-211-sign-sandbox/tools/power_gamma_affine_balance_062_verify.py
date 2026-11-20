"""Only the same historical gamma129: affine comparator and FULL residual042.
Reuses the complete intervalJ1 of024 and complete ERR/ARCHsharp of061.
No new truncation, dimension, or prime search.
"""
from fractions import Fraction as F
import power_cell_test_024_verify as CELL
import power_gamma_129_decision_061_verify as DEC
C=DEC.C
J1=C.I(CELL.endpoint1.lo-CELL.tailP,CELL.endpoint1.hi+CELL.tailP)
kappa=(C.log2+C.logpi-1)/2
beta=2*kappa-C.gamma
AFF=DEC.SHARP+2*C.gamma-beta*J1
R=(DEC.ERR+2*C.gamma-beta*J1)/2
assert -F(1,5)<AFF.lo<AFF.hi<-F(1,100)
assert -F(1,10)<R.lo<R.hi<-F(1,200)
assert R.hi-R.lo<F(1,10**10)
# AFF-2R=W is the symbolic identity, with shared J1/gamma/beta.
# DO NOT subtract independently enclosed AFF/R to recertify the tiny W margin.
def out(name,x):
 den=10**12
 print(name,'[',(x.lo*den).__floor__(),',',(x.hi*den).__ceil__(),']/10^12')
out('J129(1) complete',J1)
out('AFF129',AFF)
out('R129 FULL renormalized',R)
out('correction -2R129',-2*R)
print('PASS: affine comparator is strictly negative; full renormalized residual is favorable and essential for this same129')
print('PASS: no use of ABS-TAIL042 (requires N>=2^80); no separate attribution to periodic B1 alone')

"""R153 Q2(ii) -- lambda_min(A_T|P_T) at T=log2 with the shift log3 replaced by b
(weight w_3 unchanged), fine scan.  DIAGNOSTIC-NUMERIC.  Run: python3 r153_q2b_shift_scan.py"""
import math,sys,os
import numpy as np
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),
    "../../phase-118-the-exact-threshold-inequality/scripts")))
import rowd_assembly as RA
from r153_q1_xi_a import moments, constrained_min
T=math.log(2)
for refine in (128,256):
    D=RA.assemble(T,refine=refine); c,d,Gram=D['c'],D['d'],D['Gram']
    Arch=D['G']-RA.M0*Gram
    lam=RA.von_mangoldt(4); w2=lam[2]/math.sqrt(2); w3=lam[3]/math.sqrt(3)
    S2=RA.shift_form(c,d,math.log(2)); base=Arch-w2*(S2+S2.T)
    C2=moments(c,d,[-0.5,0.5])
    print(f"refine={refine} cells={len(c)}")
    for b in [1.00,1.05,1.07,1.08,1.09,1.0986123,1.11,1.12,1.15,1.20,1.30,1.38]:
        S=RA.shift_form(c,d,b); M=base-w3*(S+S.T)
        w,_=constrained_min(M,Gram,C2)
        tag="  <-- b = log 3" if abs(b-math.log(3))<1e-6 else ""
        print(f"   b={b:.7f}  lambda_min={w[0]: .6e}{tag}")

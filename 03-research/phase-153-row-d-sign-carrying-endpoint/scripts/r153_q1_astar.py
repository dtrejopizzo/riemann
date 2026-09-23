"""R153 Q1 -- a*(T): smallest a in (0,1/2) at which the Galerkin lambda_min of
A_T^{(a)} on P_T^{(a)} turns negative.  DIAGNOSTIC-NUMERIC (the discretisation
over-estimates lambda_min, so a* printed here is an UPPER bound for the true a*).
Run: python3 r153_q1_astar.py"""
import math,sys,os,numpy as np
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),
    "../../phase-118-the-exact-threshold-inequality/scripts")))
import rowd_assembly as RA
from r153_q1_xi_a import moments, constrained_min, cell_avg_exp
def lam_a(D,a):
    c,d,A,Gram=D['c'],D['d'],D['A'],D['Gram']
    ch=0.5*(cell_avg_exp(c,d,a)+cell_avg_exp(c,d,-a)); sh=0.5*(cell_avg_exp(c,d,a)-cell_avg_exp(c,d,-a))
    Du,Dw=np.diag(ch),np.diag(sh)
    M=2.0*(Du@A@Du-Dw@A@Dw)
    w,_=constrained_min(M,Gram,moments(c,d,[-0.5-a,-0.5+a,0.5-a,0.5+a]))
    return w[0]
for refine in (64,128,256):
  print(f"--- refine={refine}")
  for T in (0.30,0.40,0.50,0.5*math.log(3),0.60,math.log(2)):
    D=RA.assemble(T,refine=refine)
    w0,_=constrained_min(D['A'],D['Gram'],moments(D['c'],D['d'],[-0.5,0.5]))
    lo,hi=0.0,0.499
    if lam_a(D,hi)>0: astar=None
    else:
        for _ in range(22):
            mid=0.5*(lo+hi)
            if lam_a(D,mid)<0: hi=mid
            else: lo=mid
        astar=hi
    print(f"   T={T:.6f} cells={len(D['c'])} lam_min(A_T|P_T)={w0[0]: .4e} "
          f"a*={'none in (0,0.499]' if astar is None else f'{astar:.4f}'}  lam(a=0.45)={lam_a(D,0.45): .4e}")

import math,sys
from r153_tstar import tstar
for a in [0.001,0.002,0.005,0.01,0.02,0.03,0.04,0.05,0.45,0.50]:
    v=tstar(a,160,lo=0.30,hi=3.0)
    print(f"a={a:<6} T*={v:.5f}"); sys.stdout.flush()

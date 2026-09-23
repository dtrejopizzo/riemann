import numpy as np, sys
from math import pi
sys.path.insert(0,'.'); from weil import TestF
rng=np.random.default_rng(11)
print("random F (12 per support), h=F*F~, ||F||=1.  W = pole + gamma + prime  (prime side; oracle = 1000 zeros, validated 6 digits)")
print("  U     min W     pole(mean)  gamma(mean)  prime(min..max)   cancellation |pole+gamma|/pole   worst margin W/pole")
for U in (0.30,0.40,0.50,0.55,0.60,0.65,0.70):
    rows=[]
    for k in range(12):
        f=TestF(U,rng.standard_normal(3),rng.uniform(0,8,3),rng.uniform(0,2*pi,3),n=601)
        po,ga,pr=f.parts(); rows.append((po,ga,pr,po+ga+pr))
    r=np.array(rows); i=r[:,3].argmin()
    print(" %.2f  %+.5f   %+.4f     %+.4f     %+.4f..%+.4f      %.3f                  %.4f"%(U,r[:,3].min(),r[:,0].mean(),r[:,1].mean(),r[:,2].min(),r[:,2].max(),abs(r[:,0]+r[:,1]).mean()/abs(r[:,0]).mean(), (r[i,3]/r[i,0]) if r[i,0]>0 else float('nan')))

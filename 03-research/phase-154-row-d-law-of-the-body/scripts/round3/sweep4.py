import math, numpy as np, pickle
from lattice4 import solve
T3 = 0.5*math.log(3)
best=None
res={}
for k in (5,6,7,8,10):
    for tm in (200.0, 400.0):
        for U in (40.0, 80.0):
            r = solve(T3, k=k, U=U, taumax=tm, dtau=0.005, dper=0.003)
            if r is not None:
                res[(k,tm,U)] = {kk:r[kk] for kk in ('a','us','b0','b1','rho','lp','taumax','P','k','d','U')}
pickle.dump(res, open('sweep4.pkl','wb'))

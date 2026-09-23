import math, pickle
from lattice3 import solve
T3 = 0.5*math.log(3); res={}
for M in (8,12,16,19,24):
    r = solve(T3, M=M, U=40.0, taumax=200.0, dtau=0.005, dper=0.02)
    if r: res[M]=r; pickle.dump(res, open('sweepM.pkl','wb'))

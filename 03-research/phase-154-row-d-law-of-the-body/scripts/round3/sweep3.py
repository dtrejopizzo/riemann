import math, sys, numpy as np
from lattice3 import solve
T3 = 0.5*math.log(3)
for M in (10,12,16,20):
    for tm in (120.0, 250.0, 500.0):
        try: solve(T3, M=M, U=40.0, taumax=tm, dtau=0.004, dper=0.002)
        except MemoryError: print("mem", M, tm, flush=True)

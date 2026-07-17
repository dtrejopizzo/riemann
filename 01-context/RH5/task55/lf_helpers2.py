
import mpmath as mp
import numpy as np mp.mp.dps = 18
chi5_vals = [0, 1, -1, -1, 1] # Kronecker symbol mod 5
kappa = (mp.sqrt(10 - 2*mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1) def abs_lchi5_at(t): return abs(complex(mp.dirichlet(mp.mpc(0.5, t), chi5_vals))) def batch_lchi5(ts): return [abs_lchi5_at(t) for t in ts]

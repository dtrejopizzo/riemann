
import mpmath as mp
import numpy as np mp.mp.dps = 20
chi5_vals = [0, 1, 1j, -1j, -1]
kappa = (mp.sqrt(10 - 2*mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1) def abs_zeta_at(t): return abs(float(mp.siegelz(t))) def abs_lchi5_at(t): return abs(complex(mp.dirichlet(mp.mpc(0.5, t), chi5_vals))) def abs_ldh_at(t): s = mp.mpc(0.5, t) v = mp.zeta(s, mp.mpf(1)/5) + kappa*mp.zeta(s, mp.mpf(2)/5) - kappa*mp.zeta(s, mp.mpf(3)/5) - mp.zeta(s, mp.mpf(4)/5) return abs(complex(v)) def batch_zeta(ts): return [abs_zeta_at(t) for t in ts] def batch_lchi5(ts): return [abs_lchi5_at(t) for t in ts] def batch_ldh(ts): return [abs_ldh_at(t) for t in ts]

#!/usr/bin/env python3
"""
HR stability dichotomy (Theorem: uniform HR <=> strictly definite limit).

We model a Hodge-Riemann tower by symmetric bilinear forms Q_m on a fixed space,
converging to a limit Q_inf, and track the HR gap delta_m = smallest eigenvalue
on the primitive subspace (here all of R^4).  Two families:
  (a) definite limit  Q_inf = diag(0.5,1,1.5,2),  delta_inf = 0.5 > 0  -> uniform HR
  (b) degenerate limit Q_inf = diag(0,  1,1.5,2),  delta_inf = 0       -> uniform HR fails
The convergence Q_m -> Q_inf is at rate 1/sqrt(m) (a) and 1/m (b).
"""
import numpy as np

def gap(Q):
    return float(np.linalg.eigvalsh((Q + Q.T) / 2)[0])

# fixed perturbation direction (a generic symmetric tridiagonal, scaled to converge to 0)
R = np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]], float)
R = R / np.linalg.norm(R, 2)   # normalize operator norm to 1

Qinf_def = np.diag([0.5, 1.0, 1.5, 2.0])   # delta_inf = 0.5
Qinf_deg = np.diag([0.0, 1.0, 1.5, 2.0])   # delta_inf = 0

ms = [2, 8, 32, 128, 512]

print(" definite limit (delta_inf>0):  expect delta_m -> 0.5 (uniform HR holds)")
for m in ms:
    Q = Qinf_def + (1.0/np.sqrt(m)) * R          # rate 1/sqrt(m)
    print(f"   m={m:4d}: delta={gap(Q):.4f}")

print(" degenerate limit (delta_inf=0):  expect delta_m -> 0 (uniform HR fails)")
for m in ms:
    Q = Qinf_deg + (1.0/m) * np.eye(4)           # smallest eigenvalue = 1/m
    print(f"   m={m:4d}: delta={gap(Q):.4f}")

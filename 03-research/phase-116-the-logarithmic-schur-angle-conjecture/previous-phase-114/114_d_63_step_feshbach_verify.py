#!/usr/bin/env python3
"""Reproduce the midpoint and analytic residuals of the D.63 certificate.

The proof's finite sign is obtained by outward-rounded interval LDL.  This
portable script recomputes its midpoint matrix from closed entries and
checks all deliberately rounded analytic constants.
"""
import math
import numpy as np

T = 0.4
a = math.log(2.0)
c = a / math.sqrt(2.0)
m0 = math.log(math.pi) + 0.5772156649015329 + math.pi/2 + 3*a
mb, mm = 36, 196

edges = []
for left, right, count in ((-T, T-a, mb), (T-a, a-T, mm), (a-T, T, mb)):
    part = np.linspace(left, right, count+1)
    if edges:
        part = part[1:]
    edges.extend(part.tolist())
edges = np.asarray(edges)
left, right = edges[:-1], edges[1:]
length = right-left
n = len(length)
assert n == 268 and length.max() < 0.002992

bvals = 2*np.arange(20, dtype=float) + 0.5
C = np.sum(2/bvals)-m0
A = C*np.eye(n)
A[:mb, -mb:] -= c*np.eye(mb)
A[-mb:, :mb] -= c*np.eye(mb)

K = np.zeros((n, n))
for b in bvals:
    K[np.diag_indices(n)] += 2*(length/b-(1-np.exp(-b*length))/b**2)/length
    for i in range(n-1):
        j = np.arange(i+1, n)
        value = (
            np.exp(-b*(left[j]-right[i]))
            - np.exp(-b*(right[j]-right[i]))
            - np.exp(-b*(left[j]-left[i]))
            + np.exp(-b*(right[j]-left[i]))
        )/(b*b*np.sqrt(length[i]*length[j]))
        K[i, j] += value
        K[j, i] += value

moments = np.column_stack((
    2*(np.exp(right/2)-np.exp(left/2))/np.sqrt(length),
    2*(np.exp(-left/2)-np.exp(-right/2))/np.sqrt(length),
))
R = A-K+10*moments@moments.T
lambda_min_mid = np.linalg.eigvalsh(R)[0]
assert lambda_min_mid > 0.15545

I19 = 4*T*sum(
    bi*bj*(1-math.exp(-2*T*(bi+bj)))/(bi+bj)
    for bi in bvals for bj in bvals
)
eps_K = 2*length.max()/math.pi*math.sqrt(I19)
h_norm = math.sqrt(2*math.sinh(T))
eps_H = 10*4*h_norm*(length.max()/math.pi)*(h_norm/2)
assert math.sqrt(I19) < 71.020
assert eps_K < 0.13525
assert eps_H < 0.01565
assert 0.15530-0.13525-0.01565 > 0.00439

print("PASS finite dimension", n)
print("PASS midpoint lambda_min", lambda_min_mid)
print("PASS kernel residual", eps_K)
print("PASS moment residual", eps_H)
print("PASS midpoint/residual diagnostic; run the python-flint interval verifier for the directed certificate")

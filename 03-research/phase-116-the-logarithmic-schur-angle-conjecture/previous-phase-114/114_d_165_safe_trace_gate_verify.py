#!/usr/bin/env python3
"""Finite-dimensional verification of the D.165 safe trace gate."""
import numpy as np
rng=np.random.default_rng(165);n=37;r=5;delta=.218
z=rng.normal(size=(n,n));K=z.T@z+.4*np.eye(n)
q=rng.normal(size=(19,n));G=q.T@q
# Scale to a nontrivial theta below one.
X=np.linalg.solve(np.linalg.cholesky(K),G)
X=np.linalg.solve(np.linalg.cholesky(K),X.T).T
G*=.63*delta/np.trace(X)
X=np.linalg.solve(np.linalg.cholesky(K),G)
X=np.linalg.solve(np.linalg.cholesky(K),X.T).T
theta=np.trace(X)/delta
Lss=K-G/delta
assert theta<1 and np.linalg.eigvalsh(Lss-(1-theta)*K)[0]>-2e-11
Lds=rng.normal(size=(r,n))*.01
Ldd=Lds@np.linalg.solve(Lss,Lds.T)+.02*np.eye(r)
lower=Ldd-Lds@np.linalg.solve(Lss,Lds.T)
coarse=Ldd-Lds@np.linalg.solve(K,Lds.T)/(1-theta)
assert np.linalg.eigvalsh(lower-coarse)[0]>-2e-11
print('D165 safe trace gate: PASS')
print('theta =',theta,'final coarse minimum =',np.linalg.eigvalsh(coarse)[0])

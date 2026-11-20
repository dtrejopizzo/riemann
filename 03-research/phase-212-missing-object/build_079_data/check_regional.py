"""Exploratory Galerkin spectrum of BUILD083 q_T, even primitive sector.

The isometric even embedding is F(t)=f(abs(t))/sqrt(2), hence Aeven=q+glue.
No interval arithmetic or continuum eigenvalue certification. The singular
quadrature is deliberately used only to diagnose order-one negative modes.
"""
import json
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander

T = 0.8
C0 = -np.euler_gamma - np.pi/2 - 3*np.log(2) - np.log(np.pi)
contacts = [(np.log(n), lam/np.sqrt(n)) for n, lam in
            [(2,np.log(2)), (3,np.log(3)), (4,np.log(2))]]

for degree, order in [(16,128), (24,256), (24,512), (32,512)]:
    z, w = leggauss(order)
    def quadrature(a, b):
        return (a+b)/2+(b-a)*z/2, (b-a)*w/2
    def basis(x):
        x = np.asarray(x)
        ans = legvander(2*x/T-1, degree)*np.sqrt((2*np.arange(degree+1)+1)/T)
        return ans*((x>0)&(x<T))[:,None]
    def integrate_gram(a,b):
        x,v = quadrature(a,b)
        B = basis(x)
        return B.T@(v[:,None]*B)
    x,v = quadrature(0,T)
    B = basis(x)
    distance = abs(x[:,None]-x[None,:])
    np.fill_diagonal(distance, 1.)
    kernel = np.exp(-distance/2)/(-np.expm1(-2*distance))
    np.fill_diagonal(kernel,0.)
    total = x[:,None]+x[None,:]
    kernel += np.exp(-total/2)/(-np.expm1(-2*total))
    # A diagonal choice has zero effect on the graph energy.
    W = v[:,None]*kernel*v[None,:]
    lap = np.diag(W.sum(axis=1))-W
    def tail_integral(u):
        t = np.exp(-u/2)
        return np.arctanh(t)+np.arctan(t)
    tail = tail_integral(T-x)+tail_integral(T+x)
    N = B.T@lap@B+B.T@((v*tail)[:,None]*B)
    q = C0*np.eye(degree+1)+N
    glue = np.zeros_like(q)
    for length, weight in contacts:
        if length<T:
            t,u = quadrature(length,T)
            cross = basis(t).T@(u[:,None]*basis(t-length))
            q -= weight*(cross+cross.T)
        q -= weight*integrate_gram(0,min(length,T))
        edges = sorted(set([0.,length]+[p for p in (T,length-T) if 0<p<length]))
        for a,b in zip(edges,edges[1:]):
            t,u = quadrature(a,b)
            D = basis(t)-basis(length-t)
            glue += (weight/2)*(D.T@(u[:,None]*D))
    moment = B.T@(v*np.cosh(x/2))
    Z = np.linalg.qr(moment[:,None],mode='complete')[0][:,1:]
    qr = Z.T@q@Z
    br = Z.T@glue@Z
    eigen, U = np.linalg.eigh((qr+qr.T)/2)
    k = int(np.sum(eigen<0))
    total = np.diag(eigen)+U.T@br@U
    low = total[:k,:k]
    if 0<k<len(eigen):
        mixed = total[:k,k:]
        complement = total[k:,k:]
        solved = np.linalg.solve(complement,mixed.T)
        complement_min = float(np.linalg.eigvalsh(complement)[0])
        solve_residual = float(np.linalg.norm(complement@solved-mixed.T))
        transfer = mixed@solved
        schur = low-transfer
    else:
        transfer = np.zeros_like(low)
        schur = low
        complement_min = None
        solve_residual = None
    print(json.dumps(dict(degree=degree,order=order,negative_count=k,
          regional_eigenvalues=eigen[:min(k+2,len(eigen))].tolist(),
          retained_min=float(np.linalg.eigvalsh(low)[0]) if k else None,
          transfer_norm=float(np.linalg.norm(transfer,2)) if k else None,
          complement_min=complement_min, solve_residual=solve_residual,
          schur_eigenvalues=np.linalg.eigvalsh(schur).tolist(),
          full_min=float(np.linalg.eigvalsh(total)[0]))),flush=True)

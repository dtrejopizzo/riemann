"""Floating diagnostic of BUILD083 low/high matrices after singular extraction.

No interval certificate and no estimate of the full L2 residual R*R.
The exact S_Z is an upper bound; floating outputs are not certified bounds.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
import mpmath as mm
from regional_bases import stable_split

def remainder(u):
    u = np.asarray(u)
    result = np.empty_like(u)
    small = u<0.05
    x = u[small]
    result[small] = (0.25-x/48-x*x/32+7*x**3/11520+5*x**4/1536
                    -31*x**5/1935360-61*x**6/184320
                    +127*x**7/309657600+1385*x**8/41287680)
    x = u[~small]
    result[~small] = np.exp(-x/2)/(-np.expm1(-2*x))-1/(2*x)
    return result

def tail_remainder(u):
    x = np.asarray(u)/4
    t = np.tanh(x)
    return 0.5*np.log(x/t)-np.arctan(t)

def logarithmic_matrix(degree):
    H = np.concatenate([[0.],np.cumsum(1/np.arange(1,2*degree+2))])
    matrix = np.empty((degree+1,degree+1))
    for n in range(degree+1):
        for m in range(degree+1):
            if n==m:
                matrix[n,m] = 2*H[n]-2*H[2*n+1]+1/(2*n+1)
            else:
                matrix[n,m] = -np.sqrt((2*n+1)*(2*m+1))/(abs(n-m)*(n+m+1))
    return matrix,H[:degree+1]

def full_matrices(T,degree,order):
    if abs(T-0.8)>1e-15:
        raise ValueError('This diagnostic is specialized to T=0.8 and contacts 2,3,4.')
    if order<=degree:
        raise ValueError('Use quadrature order greater than the polynomial degree.')
    z,w = leggauss(order)
    u=(z+1)/2
    w=w/2
    factors=np.sqrt(2*np.arange(degree+1)+1)
    def phi(t): return legvander(t*2-1,degree)*factors
    uu,vv=np.meshgrid(u,u,indexing='ij')
    weights=(w[:,None]*w[None,:]).ravel()
    uu,vv=uu.ravel(),vv.ravel()
    X=np.repeat(phi(u),order,axis=0)
    Y=phi(uu*vv)
    diff=X-Y
    direct_weight=weights*T*uu*remainder(T*uu*(1-vv))
    direct=diff.T@(direct_weight[:,None]*diff)
    mirror_weight=weights*(0.5/(1+vv)+T*uu*remainder(T*uu*(1+vv)))
    logmat,harmonic=logarithmic_matrix(degree)
    B=phi(u)
    tail=(-0.5*np.log1p(u)+tail_remainder(T*(1-u))+tail_remainder(T*(1+u)))
    common=(np.diag(harmonic-np.euler_gamma-np.log(2*np.pi*T))
            -0.5*logmat+direct+B.T@((w*tail)[:,None]*B))
    even=common+diff.T@(mirror_weight[:,None]*diff)
    plus=X+Y
    odd=common+plus.T@(mirror_weight[:,None]*plus)
    def physical(t): return phi(t/T)/np.sqrt(T)
    def quad(a,b): return a+(b-a)*u,(b-a)*w
    for n,prime in ((2,2),(3,3),(4,2)):
        length=np.log(n)
        weight=np.log(prime)/np.sqrt(n)
        if length<T:
            x,v=quad(length,T)
            cross=physical(x).T@(v[:,None]*physical(x-length))
            even-=weight*(cross+cross.T)
            odd-=weight*(cross+cross.T)
        x,v=quad(max(0,length-T),min(T,length))
        reflection=physical(x).T@(v[:,None]*physical(length-x))
        reflection=(reflection+reflection.T)/2
        even-=weight*reflection
        odd+=weight*reflection
    return (even+even.T)/2,(odd+odd.T)/2

def run(order,degree=111,N=95):
    T=0.8
    matrices=full_matrices(T,degree,order)
    records=[]
    mm.mp.dps=70
    for parity,A in zip(('even','odd'),matrices):
        _,low,high=stable_split(mm.mp,mm.mp.mpf(4)/5,N,parity,degree-N,interval=False)
        def columns(vectors):
            matrix=np.zeros((degree+1,len(vectors)))
            for j,v in enumerate(vectors):
                for i,c in v.items(): matrix[i,j]=float(c)
            return matrix
        E,W=columns(low),columns(high)
        P=E.T@A@E
        K=W.T@A@W
        D=W.T@A@E
        Z=np.linalg.solve(K,D)
        S=P-D.T@Z
        np.savez_compressed(Path(__file__).parent/f'blocks_{parity}_{order}.npz',
                            T=T,degree=degree,order=order,N=N,A=A,E=E,W=W,P=P,K=K,D=D,Z=Z,S=S)
        records.append(dict(parity=parity,order=order,degree=degree,low_dimension=N,
                            high_dimension=degree-N,high_min=float(np.linalg.eigvalsh(K)[0]),
                            solve_residual=float(np.linalg.norm(K@Z-D)),
                            low_eigenvalues=np.linalg.eigvalsh(P)[:4].tolist(),
                            corrected_eigenvalues=np.linalg.eigvalsh(S)[:4].tolist()))
    return records

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--orders',type=int,nargs='+',default=[128,160])
    parser.add_argument('--degree',type=int,default=111)
    args=parser.parse_args()
    destination=Path(__file__).parent/'blocks_diagnostic.json'
    previous=json.loads(destination.read_text())['records'] if destination.exists() else []
    indexed={(r['parity'],r['order'],r['degree']):r for r in previous}
    for order in args.orders:
        result=run(order,degree=args.degree)
        for r in result: indexed[(r['parity'],r['order'],r['degree'])]=r
        print(json.dumps(result),flush=True)
    destination.write_text(json.dumps(
        dict(status='NUMERICAL_ONLY',full_L2_residual_certified=False,
             records=list(indexed.values())),indent=2)+'\n')

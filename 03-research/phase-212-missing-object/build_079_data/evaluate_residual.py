"""Numerical functional residual of the fixed BUILD083 finite corrector.

Not an interval enclosure of R*R. Endpoint logarithms remain in the outer
L2 quadrature. The exact sufficient test is S_Z-8R*R >= 0.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander
from scipy.special import lqmn
import mpmath as mm
from evaluate_blocks import remainder,tail_remainder
from regional_bases import moment_coeff

def operator_basis(x,T,degree,parity,inner_order=160):
    factors=np.sqrt((2*np.arange(degree+1)+1)/T)
    def values(t): return legvander(2*np.asarray(t)/T-1,degree)*factors
    def zero_values(t):
        t=np.asarray(t)
        out=np.zeros((len(t),degree+1))
        mask=(t>0)&(t<T)
        out[mask]=values(t[mask])
        return out
    P=values(x)
    harmonic=np.concatenate([[0.],np.cumsum(1/np.arange(1,degree+1))])
    z=x/T
    multiplier=(-np.euler_gamma-np.log(2*np.pi*T)
                -.5*np.log1p(-z*z)+tail_remainder(T-x)+tail_remainder(T+x))
    result=P*(harmonic[None,:]+multiplier[:,None])
    sign=1 if parity=='even' else -1
    g,v=leggauss(inner_order)
    y=T*(g+1)/2
    weights=T*v/2
    Py=values(y)
    reflected_weight=remainder(x[:,None]+y[None,:])*weights[None,:]
    result+=P*reflected_weight.sum(axis=1)[:,None]-sign*(reflected_weight@Py)
    signs=(-1.)**np.arange(degree+1)
    for row,t in enumerate(x):
        Q=lqmn(0,degree,1+2*t/T)[0][0]
        reflected_integral=2*signs*factors*Q
        result[row]+=.5*(P[row]*(2*Q[0])-sign*reflected_integral)
        for a,b in ((0,t),(t,T)):
            yy=(a+b)/2+(b-a)*g/2
            ww=(b-a)*v/2*remainder(abs(t-yy))
            result[row]+=P[row]*ww.sum()-ww@values(yy)
    for n,prime in ((2,2),(3,3),(4,2)):
        length=np.log(n)
        weight=np.log(prime)/np.sqrt(n)
        result-=weight*(zero_values(x+length)+zero_values(x-length)+sign*zero_values(length-x))
    return result,P

def run(parity,outer_order,block_order=160,inner_order=160):
    folder=Path(__file__).parent
    with np.load(folder/f'blocks_{parity}_{block_order}.npz') as data:
        T=float(data['T']);degree=int(data['degree'])
        A,E,W,Z,S=[data[k] for k in ('A','E','W','Z','S')]
    corrected=E-W@Z
    edges=sorted(set([0.,T]+[p for n in (2,3,4) for p in (np.log(n),T-np.log(n),np.log(n)-T) if 0<p<T]))
    g,v=leggauss(outer_order)
    x=np.concatenate([(a+b)/2+(b-a)*g/2 for a,b in zip(edges,edges[1:])])
    weights=np.concatenate([(b-a)*v/2 for a,b in zip(edges,edges[1:])])
    action,basis=operator_basis(x,T,degree,parity,inner_order)
    source=action@corrected
    mm.mp.dps=70
    alpha=np.array([float(moment_coeff(mm.mp,mm.mp.mpf(4)/5,n,parity,interval=False)) for n in range(degree+1)])
    h=np.cosh(x/2) if parity=='even' else np.sinh(x/2)
    hnorm=(np.sinh(T)+(T if parity=='even' else -T))/2
    # The h projection moment is approximated by its degree-111 expansion.
    # Its omitted tail is not claimed to have been certified in this script.
    h_pairing=alpha@A@corrected
    low_pairing=E.T@A@corrected
    low_coeff=np.linalg.solve(E.T@E,low_pairing)
    residual=source-h[:,None]*(h_pairing/hnorm)[None,:]-(basis@E)@low_coeff
    gram=residual.T@(weights[:,None]*residual)
    lower=S-8*gram
    eigen,vec=np.linalg.eigh(S)
    bottom=vec[:,0]
    weighted_moment_error=np.linalg.norm((basis@E).T@(weights[:,None]*residual))
    records=dict(parity=parity,outer_order=outer_order,inner_order=inner_order,
                 block_order=block_order,degree=degree,
                 residual_gram_norm=float(np.linalg.norm(gram,2)),
                 sufficient_min=float(np.linalg.eigvalsh(lower)[0]),
                 sufficient_negative_count=int(np.sum(np.linalg.eigvalsh(lower)<0)),
                 S_bottom=float(eigen[0]),bottom_penalty=float(8*bottom@gram@bottom),
                 sampled_low_orthogonality_error=float(weighted_moment_error))
    np.savez_compressed(folder/f'residual_{parity}_{block_order}_{outer_order}.npz',gram=gram,lower=lower)
    return records

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--orders',type=int,nargs='+',default=[128,256])
    parser.add_argument('--blocks-order',type=int,default=160)
    parser.add_argument('--inner-order',type=int,default=None)
    args=parser.parse_args()
    records=[]
    for order in args.orders:
        for parity in ('even','odd'):
            record=run(parity,order,args.blocks_order,args.inner_order or args.blocks_order)
            records.append(record)
            print(json.dumps(record),flush=True)
    (Path(__file__).parent/f'residual_diagnostic_{args.blocks_order}.json').write_text(json.dumps(dict(
        status='NUMERICAL_ONLY',interval_enclosure=False,records=records),indent=2)+'\n')

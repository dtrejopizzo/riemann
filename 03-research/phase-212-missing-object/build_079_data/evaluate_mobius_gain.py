"""Floating diagnostic of the first Mobius seed and scalar-criterion gain.

No interval enclosure, positivity certificate, or global conclusion.
"""
import argparse,json
from pathlib import Path
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss
from evaluate_residual import operator_basis
from regional_bases import moment_coeff

FOLDER=Path(__file__).parent
C0=-np.euler_gamma-np.pi/2-3*np.log(2)-np.log(np.pi)

def tail(d):
    z=np.exp(-d/2)
    return .5*(np.log1p(z)-np.log(-np.expm1(-d/2)))+np.arctan(z)

def step_action(x,a,b,contacts):
    out=np.empty_like(x)
    inside=(x>a)&(x<b);left=x<a;right=x>b
    assert np.all(inside|left|right)
    out[inside]=C0+tail(x[inside]-a)+tail(b-x[inside])
    out[left]=-tail(a-x[left])+tail(b-x[left])
    out[right]=-tail(x[right]-b)+tail(x[right]-a)
    for length,weight in contacts:
        out-=weight*(((x+length>a)&(x+length<b)).astype(float)+((x-length>a)&(x-length<b)).astype(float))
    return out

def increment(d,sign):
    z=np.exp(-d/2)
    if sign==1:
        return -d-np.log1p(z)-.5*np.log1p(z*z)-np.arctan(z)+1.5*np.log(2)+np.pi/4
    return -np.log1p(z)+.5*np.log1p(z*z)-np.arctan(z)+.5*np.log(2)+np.pi/4

def exponential_action(x,T,sign,contacts):
    out=np.exp(sign*x/2)*(C0+tail(x+T)+tail(T-x)+increment(x+T,-sign)+increment(T-x,sign))
    for length,weight in contacts:
        for t in (x+length,x-length):
            out-=weight*np.where((t>-T)&(t<T),np.exp(sign*t/2),0.)
    return out

def run(parity,order,metric="scalar"):
    T=.8; sigma=1 if parity=='even' else -1
    rec=next(s for s in json.loads((FOLDER/'projected_mobius_seed.json').read_text())['sectors'] if s['parity']==parity)
    steps=[tuple(map(float,row)) for row in rec['steps']]
    c=np.array(list(map(float,rec['legendre_coefficients'])))
    kh=float(rec['h_coefficient'])
    contacts=[(np.log(n),np.log(p)/np.sqrt(n)) for n,p in ((2,2),(3,3),(4,2))]
    edges=[0.,T]
    for a,b,_ in steps:
        for endpoint in (a,b,-a,-b,-T,T):
            for shift in [0.]+[s*l for l,_ in contacts for s in (-1,1)]:
                point=endpoint+shift
                if 0<point<T: edges.append(point)
    merged=[]
    for point in sorted(edges):
        if not merged or point-merged[-1]>1e-12: merged.append(point)
    nodes,weights=leggauss(order)
    x=np.concatenate([(a+b)/2+(b-a)*nodes/2 for a,b in zip(merged,merged[1:])])
    weights=np.concatenate([(b-a)*weights/2 for a,b in zip(merged,merged[1:])])
    AP,P=operator_basis(x,T,111,parity,inner_order=160)
    data=np.load(FOLDER/f'blocks_{parity}_160.npz')
    E,W=data['E'],data['W']; EV,WV=P@E,P@W
    h=np.cosh(x/2) if sigma==1 else np.sinh(x/2)
    hnorm=(np.sinh(T)+sigma*T)/2
    mp.mp.dps=70
    alpha=np.array([float(moment_coeff(mp.mp,mp.mpf(4)/5,n,parity,interval=False)) for n in range(96)])
    PV=P[:,:96];hlow=PV@alpha; low_norm=alpha@alpha
    def project(F):
        return F-PV@(PV.T@(weights[:,None]*F))+hlow[:,None]*((hlow*weights)@F/low_norm)[None,:]-h[:,None]*((h*weights)@F/hnorm)[None,:]
    raw=np.zeros_like(x);Ag=np.zeros_like(x)
    for a,b,coefficient in steps:
        raw+=coefficient*((x>a)&(x<b))
        Ag+=coefficient*(step_action(x,a,b,contacts)+sigma*step_action(x,-b,-a,contacts))
    Ah=(exponential_action(x,T,1,contacts)+sigma*exponential_action(x,T,-1,contacts))/2
    w=raw+PV@c+kh*h
    Aw=Ag+AP[:,:96]@c+kh*Ah
    C=project(AP@E);Y=project(AP@W);y=project(Aw[:,None])[:,0]
    K=WV.T@(weights[:,None]*Y);K=(K+K.T)/2
    epsilon=1e-12
    if metric=='modal':
        cT=C0+2*float(tail(np.array(T)))-3*np.log(2)/np.sqrt(2)-np.log(3)/np.sqrt(3)-np.log(2)/2
        harmonic=np.concatenate(([0.],np.cumsum(1/np.arange(1,113))))
        rho=1/(harmonic[112]+cT)
        diagonal=1/(harmonic[96:112]+cT)-rho
        assert np.all(diagonal>=0)
        def apply_metric(F):
            vector=F.ndim==1
            A=F[:,None] if vector else F
            result=(rho+epsilon)*A+WV@(diagonal[:,None]*(WV.T@(weights[:,None]*A)))
            return result[:,0] if vector else result
    else:
        def apply_metric(F): return 16.*F
    VY,VC,Vy=apply_metric(Y),apply_metric(C),apply_metric(y)
    G=Y.T@(weights[:,None]*VY)-K
    G=(G+G.T)/2
    G_eigen=np.linalg.eigvalsh(G)
    if G_eigen[0]<=0:
        return dict(parity=parity,order=order,metric=metric,status='NUMERICAL_METRIC_FAILURE',metric_min=float(G_eigen[0]))
    cross=Y.T@(weights*Vy)-WV.T@(weights*y)
    a=np.linalg.solve(G,cross)
    q=w-WV@a;Hq=y-Y@a
    VHq=apply_metric(Hq)
    d=np.dot(weights,Hq*VHq)-np.dot(weights,q*Hq)
    b=(weights*VHq)@C-(weights*q)@C
    assert d>0 and np.all(np.isfinite(b))
    low_block=EV.T@(weights[:,None]*(AP@E))
    low_block=(low_block+low_block.T)/2
    B=Y.T@(weights[:,None]*VC)-WV.T@(weights[:,None]*C)
    before=low_block-C.T@(weights[:,None]*VC)+B.T@np.linalg.solve(G,B)
    before=(before+before.T)/2
    gain=np.outer(b,b)/d
    after=before+gain
    eigen,vectors=np.linalg.eigh(before)
    eigen_after=np.linalg.eigvalsh(after)
    bottom=vectors[:,0]
    np.savez_compressed(FOLDER/f'mobius_{metric}_directional_{parity}_{order}.npz',
                        before=before,after=after,gain=gain,b=b,d=d)
    return dict(parity=parity,order=order,metric=metric,metric_min=float(G_eigen[0]),metric_condition=float(G_eigen[-1]/G_eigen[0]),pieces=len(merged)-1,nodes=len(x),
                seed_norm_squared=float(np.dot(weights,w*w)),source_norm_squared=float(np.dot(weights,y*y)),
                d=float(d),b_norm=float(np.linalg.norm(b)),gain_trace=float(b@b/d),
                criterion_min_before=float(eigen[0]),criterion_min_after=float(eigen_after[0]),
                negative_count_before=int(np.sum(eigen<0)),negative_count_after=int(np.sum(eigen_after<0)),
                gain_on_old_bottom=float((b@bottom)**2/d),
                metric_orthogonality=float(np.linalg.norm(Y.T@(weights*VHq)-WV.T@(weights*Hq))),
                input_low_orthogonality=float(np.linalg.norm(EV.T@(weights*w))),
                output_low_orthogonality=float(np.linalg.norm(EV.T@(weights*y))),
                input_moment=float(np.dot(weights,h*w)),output_moment=float(np.dot(weights,h*y)))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--orders',type=int,nargs='+',default=[96,128])
    parser.add_argument("--metric",choices=("scalar","modal"),default="scalar")
    args=parser.parse_args();records=[]
    for order in args.orders:
        for parity in ('even','odd'):
            record=run(parity,order,args.metric);records.append(record);print(json.dumps(record),flush=True)
    (FOLDER/f'mobius_{args.metric}_directional_diagnostic.json').write_text(json.dumps(dict(status='NUMERICAL_ONLY',interval_enclosure=False,scope='one enrichment direction and full criterion; no positivity certificate',records=records),indent=2)+'\n')

"""Numerical diagnosis only; saved Galerkin value is not a certified bound."""
import pickle
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss, legval
D=pickle.loads((Path(__file__).parent/'vec_T0.8.pkl').read_bytes())
T=float(D['T']); pieces=D['pieces']; coeff=np.array([float(r[0]) for r in D['vecs']['ev']])
def f(t):
    t=np.asarray(t); out=np.zeros_like(t); pos=0
    for aa,bb,d in pieces:
        a,b=float(aa),float(bb); c=coeff[pos:pos+d+1]*np.sqrt((2*np.arange(d+1)+1)/(b-a)); pos+=d+1
        mask=(t>a)&(t<b)
        out[mask]+=legval(2*(t[mask]-a)/(b-a)-1,c)
    return out
H=np.array([[2*np.sinh(T),2*T],[2*T,2*np.sinh(T)]])
alpha=1/(2*(1+1/np.sqrt(2)+1/np.sqrt(3)))
for order in (32,64,96):
    edges=sorted(set([-T,T]+[float(x)+shift for a,b,d in pieces for x in (a,b) for shift in (0,np.log(2),np.log(3)) if -T<float(x)+shift<T]))
    z,w=leggauss(order)
    t=np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges,edges[1:])]); weights=np.concatenate([(b-a)*w/2 for a,b in zip(edges,edges[1:])])
    ep=np.stack([np.exp(t/2),np.exp(-t/2)],axis=1)
    fv=f(t); moments=ep.T@(weights*fv)
    correction=np.linalg.solve(H,moments)
    def primitive(t):
        t=np.asarray(t); return f(t)-((abs(t)<T)*(np.exp(t/2)*correction[0]+np.exp(-t/2)*correction[1]))
    g=-primitive(t-np.log(2))/np.sqrt(2)-primitive(t-np.log(3))/np.sqrt(3)
    gm=ep.T@(weights*g); g-=ep@np.linalg.solve(H,gm)
    norm=weights@((fv-ep@correction)**2)
    wf2=alpha**2*(weights@g**2)
    print(dict(order=order,norm=norm,moments=moments.tolist(),WF_squared=wf2,stored_a=D['out']['ev'][0]))
# New candidate: remove explicit projected theta profile, never solver eigenvector.
def polya_M(t):
    t=np.abs(np.asarray(t)); out=np.zeros_like(t)
    for n in range(1,13):
        x=np.pi*n*n*np.exp(2*t)
        out+=np.exp(t/2-x)*(-16*x**4+112*x**3-164*x**2+36*x)
    return out
for order in (64,96):
    z,w=leggauss(order)
    t=np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges,edges[1:])]); weights=np.concatenate([(b-a)*w/2 for a,b in zip(edges,edges[1:])])
    ep=np.stack([np.exp(t/2),np.exp(-t/2)],axis=1)
    fc=np.linalg.solve(H,ep.T@(weights*f(t)))
    mc=np.linalg.solve(H,ep.T@(weights*polya_M(t)))
    def pm(t):
        t=np.asarray(t); return (abs(t)<T)*(polya_M(t)-np.exp(t/2)*mc[0]-np.exp(-t/2)*mc[1])
    def pf(t):
        t=np.asarray(t); return f(t)-(abs(t)<T)*(np.exp(t/2)*fc[0]+np.exp(-t/2)*fc[1])
    c=(weights@(pm(t)*pf(t)))/(weights@pm(t)**2)
    def filtered(t):return pf(t)-c*pm(t)
    raw=-filtered(t-np.log(2))/np.sqrt(2)-filtered(t-np.log(3))/np.sqrt(3)
    raw-=ep@np.linalg.solve(H,ep.T@(weights*raw))
    print(dict(theta_projection_order=order,WF_filtered_squared=alpha**2*(weights@raw**2),input_remaining_norm=weights@filtered(t)**2))
# BUILD080: diagnostic for contactwise arithmetic Wronskian.
for order in (64,96):
    z,w=leggauss(order)
    t=np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges,edges[1:])]); weights=np.concatenate([(b-a)*w/2 for a,b in zip(edges,edges[1:])])
    ep=np.stack([np.exp(t/2),np.exp(-t/2)],axis=1)
    fc=np.linalg.solve(H,ep.T@(weights*f(t)))
    mc=np.linalg.solve(H,ep.T@(weights*polya_M(t)))
    # pf and pm use the updated moment corrections.
    kf=-pf(t-np.log(2))/np.sqrt(2)-pf(t-np.log(3))/np.sqrt(3)
    kg=-pm(t-np.log(2))/np.sqrt(2)-pm(t-np.log(3))/np.sqrt(3)
    dg=pm(t)*kf-kg*pf(t)
    dg-=ep@np.linalg.solve(H,ep.T@(weights*dg))
    grid=np.linspace(-T,T,200001)
    sup_sampled=max(abs(pm(grid)))
    alpha_g=1/(2*(1+2*(1/np.sqrt(2)+1/np.sqrt(3))*sup_sampled))
    print(dict(wronskian_order=order,sup_g_sampled=sup_sampled,alpha_g=alpha_g,first_channel=alpha_g**2*(weights@dg**2)))
# BUILD081: two profiles, three shift samples.
def polya_Mprime(t):
    ts=np.asarray(t); a=np.abs(ts); out=np.zeros_like(a)
    for n in range(1,13):
        x=np.pi*n*n*np.exp(2*a)
        out+=np.exp(a/2-x)*(32*x**5-360*x**4+1056*x**3-810*x**2+90*x)
    return np.sign(ts)*out
for order in (64,96):
    z,w=leggauss(order)
    t=np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges,edges[1:])]); weights=np.concatenate([(b-a)*w/2 for a,b in zip(edges,edges[1:])])
    ep=np.stack([np.exp(t/2),np.exp(-t/2)],axis=1)
    fc=np.linalg.solve(H,ep.T@(weights*f(t)))
    mc=np.linalg.solve(H,ep.T@(weights*polya_M(t)))
    mpc=np.linalg.solve(H,ep.T@(weights*polya_Mprime(t)))
    def pmp(t):
        t=np.asarray(t);return (abs(t)<T)*(polya_Mprime(t)-np.exp(t/2)*mpc[0]-np.exp(-t/2)*mpc[1])
    def cof(t):
        a0,a1,a2=[pm(t-l) for l in (0,np.log(2),np.log(3))]
        b0,b1,b2=[pmp(t-l) for l in (0,np.log(2),np.log(3))]
        return [a1*b2-a2*b1,a2*b0-a0*b2,a0*b1-a1*b0]
    cs=cof(t)
    df=sum(c*pf(t-l) for c,l in zip(cs,(0,np.log(2),np.log(3))))
    df-=ep@np.linalg.solve(H,ep.T@(weights*df))
    cmax=sum(np.max(abs(c)) for c in cof(np.linspace(-T,T,200001)))
    alpha2=1/(2*(1+cmax))
    print(dict(two_profile_order=order,cofactor_sup_sum_sampled=cmax,first_channel=alpha2**2*(weights@df**2)))
